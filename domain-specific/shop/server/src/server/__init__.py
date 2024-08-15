import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import stripe

load_dotenv()


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float


PRODUCTS = [
    Product(id=1, name='laptop', description='a laptop', price=1),
    Product(id=2, name='mouse', description='a mouse', price=1),
    Product(id=3, name='keyboard', description='a keyboard', price=1),
    Product(id=4, name='monitor', description='a monitor', price=1),
]

PRICEIDS = {
    'laptop': 'price_1PnhF2EWB1hJoCiyYyQaoW0z',
    'mouse': 'price_1PnhF2EWB1hJoCiyYyQaoW0z',
    'keyboard': 'price_1PnhF2EWB1hJoCiyYyQaoW0z',
    'monitor': 'price_1PnhF2EWB1hJoCiyYyQaoW0z',
}

# configure stripe
stripe_keys = {
    'secret_key': os.environ['STRIPE_SECRET_KEY'],
    'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY'],
}

stripe.api_key = stripe_keys['secret_key']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://checkout.stripe.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def pong():
    return "pong!"


@app.get("/products")
def all_products():

    return {'products': PRODUCTS}


@app.post("/products")
async def add_product(request: Request):
    data = await request.json()
    data['id'] = len(PRODUCTS) + 1
    product = Product(**data)
    PRODUCTS.append(product)
    return {'message': 'Product added successfully', 'status': 'success'}


@app.delete("/products/{id}")
async def delete_product(id: int):
    product = next((p for p in PRODUCTS if p.id == id), None)
    if product:
        PRODUCTS.remove(product)
        return {'message': 'Product deleted successfully', 'status': 'success'}
    return {'message': 'Product not found', 'status': 'failed'}


@app.get("/config")
def get_public_key():
    return {'publicKey': os.getenv('STRIPE_PUBLISHABLE_KEY')}


calcuateTax = False


@app.get('/create-payment-intent')
def create_payment():
    # Create a PaymentIntent with the amount, currency, and a payment method type.
    #
    # See the documentation [0] for the full list of supported parameters.
    #
    # [0] https://stripe.com/docs/api/payment_intents/create
    try:
        orderAmount = 1400
        intent: stripe.PaymentIntent

        if calcuateTax:
            taxCalculation = calculate_tax(orderAmount, "usd")
            intent = stripe.PaymentIntent.create(
                amount=taxCalculation['amount_total'],
                currency='usd',
                automatic_payment_methods={
                    'enabled': True,
                },
                metadata={
                    'tax_calculation': taxCalculation['id']
                }
            )
        else:
            intent = stripe.PaymentIntent.create(
                amount=orderAmount,
                currency='usd',
                automatic_payment_methods={
                    'enabled': True,
                }
            )

        # Send PaymentIntent details to the front end.
        return {'clientSecret': intent.client_secret}
    except stripe.StripeError as e:
        return {'error': {'message': str(e)}}, 400
    except Exception as e:
        return {'error': {'message': str(e)}}, 400


@app.post('/create-checkout-session')
def create_checkout_session(data: dict):
    domain_url = 'http://localhost:5173'

    try:
        # get product
        product_to_purchase = next(
            p for p in PRODUCTS if p.id == data['product_id']
        )

        # create new checkout session
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url +
            '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + '/canceled',
            mode='payment',
            line_items=[
                {"price": PRICEIDS[product_to_purchase.name], "quantity": 1}
            ],
        )
        if not checkout_session.url:
            return {'error': 'Invalid checkout session'}
        return {"url": checkout_session.url}

        # return {'sessionId': checkout_session['id']}
    except Exception as e:
        return {'error': str(e)}


def calculate_tax(orderAmount: int, currency: str):
    tax_calculation = stripe.tax.Calculation.create(
        currency=currency,
        customer_details={
            "address": {
                "line1": "10709 Cleary Blvd",
                "city": "Plantation",
                "state": "FL",
                "postal_code": "33324",
                "country": "US",
            },
            "address_source": "shipping",
        },
        line_items=[
            {
                "amount": orderAmount,  # Amount in cents
                "reference": "ProductRef",
                "tax_behavior": "exclusive",
                "tax_code": "txcd_30011000"
            }
        ],
        shipping_cost={"amount": 300}
    )

    return tax_calculation
