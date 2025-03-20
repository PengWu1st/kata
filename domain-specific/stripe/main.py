from stripe import StripeClient
import os

client = StripeClient(os.environ["STRIPE_SECRET_KEY"])

client.v2.core.events.retrieve(
    "sub_1QfaiiE1tzSax1Klthbt27vT",
)
