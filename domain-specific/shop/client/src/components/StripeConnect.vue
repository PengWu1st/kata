<template>
  <div class="container">
    <div class="banner">
      <h2>Trickleware</h2>
    </div>
    <div class="content">
      <h2 v-if="!connectedAccountId">Get ready for take off</h2>
      <p v-if="!connectedAccountId">
        Trickleware is the world's leading knowledge service platform: join our
        community of domain experts to build your own service for your clients.
      </p>
      <div v-if="!accountCreatePending && !connectedAccountId">
        <button @click="createAccount">Sign up</button>
      </div>
      <div id="embedded-onboarding-container" />
      <p v-if="error" class="error">Something went wrong!</p>
      <div
        v-if="connectedAccountId || accountCreatePending"
        class="dev-callout"
      >
        <p v-if="connectedAccountId">
          Your connected account ID is:
          <code class="bold">{{ connectedAccountId }}</code>
        </p>
        <p v-if="accountCreatePending">Creating a connected account...</p>
        <p v-if="onboardingExited">
          The Account Onboarding component has exited
        </p>
      </div>
      <div class="info-callout">
        <p>
          This is a sample app for Connect onboarding using the Account
          Onboarding embedded component.
          <a
            href="https://docs.stripe.com/connect/onboarding/quickstart?connect-onboarding-surface=embedded"
            target="_blank"
            rel="noopener noreferrer"
            >View docs</a
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { loadConnectAndInitialize } from "@stripe/connect-js";

export default {
  data() {
    return {
      accountCreatePending: false,
      onboardingExited: false,
      error: false,
      connectedAccountId: null,
      stripeConnectInstance: null,
      stripePublicKey: null,
    };
  },
  methods: {
    createAccount() {
      this.accountCreatePending = true;
      this.error = false;
      fetch("/api/account", {
        method: "POST",
      }).then((response) =>
        response.json().then((json) => {
          this.accountCreatePending = false;
          this.connectedAccountId = json.account;

          const fetchClientSecret = async () => {
            const response = await fetch("/api/account-session", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                account: this.connectedAccountId,
              }),
            });

            if (!response.ok) {
              // Handle errors on the client side here
              const { error } = await response.json();
              throw ("An error occurred: ", error);
            } else {
              const { client_secret: clientSecret } = await response.json();
              return clientSecret;
            }
          };

          this.stripeConnectInstance = loadConnectAndInitialize({
            publishableKey: this.stripePublicKey,
            fetchClientSecret,
            appearance: {
              overlays: "dialog",
              variables: {
                colorPrimary: "#635BFF",
              },
            },
          });

          const container = document.getElementById(
            "embedded-onboarding-container"
          );
          const embeddedOnboardingComponent =
            this.stripeConnectInstance.create("account-onboarding");
          embeddedOnboardingComponent.setOnExit(() => {
            console.log("User exited the onboarding flow");
          });
          container.appendChild(embeddedOnboardingComponent);
        })
      );
    },
    getStripePublishableKey() {
      if (!this.stripePublicKey) {
        fetch("/api/config")
          .then((result) => result.json())
          .then((data) => {
            // Initialize Stripe.js
            this.stripePublicKey = data.publicKey;
          });
      }
      console.log(this.stripePublicKey);
      return this.stripePublicKey;
    },
  },
  created() {
    this.getStripePublishableKey();
  },
};
</script>
