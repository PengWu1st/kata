import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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
    allow_origins=["http://localhost:5173"],
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

        return {'sessionId': checkout_session['id']}
    except Exception as e:
        return {'error': str(e)}
