<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Products</h1>
        <hr />
        <br /><br />
        <Alert :message="message" v-if="showMessage"></Alert>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddProductModal"
        >
          Add Products
        </button>
        <br /><br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Description</th>
              <th scope="col">Liked?</th>
              <th scope="col">Price</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <ProductRow
              v-for="(product, index) in products"
              :key="index"
              :product="product"
              @purchase-product="handlePurchaseProduct"
            />
          </tbody>
        </table>
      </div>
    </div>
    <!-- add new product modal -->
    <div
      ref="addProductModal"
      class="modal fade"
      :class="{ show: activeAddProductModal, 'd-block': activeAddProductModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-name">Add a new product</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddProductModal"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addProductName" class="form-label">Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addProductName"
                  v-model="addProductForm.name"
                  placeholder="Enter name"
                />
              </div>
              <div class="mb-3">
                <label for="addProductDescription" class="form-label"
                  >Description:</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="addProductDescription"
                  v-model="addProductForm.description"
                  placeholder="Enter Description"
                />
              </div>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="addProductLiked"
                  v-model="addProductForm.Liked"
                />
                <label class="form-check-label" for="addProductLiked"
                  >Like?</label
                >
              </div>
              <div class="mb-3">
                <label for="addProductPrice" class="form-label">Price:</label>
                <input
                  type="number"
                  class="form-control"
                  id="addProductPrice"
                  v-model="addProductForm.price"
                  placeholder="Enter Price"
                />
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleAddSubmit"
                >
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleAddReset"
                >
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddProductModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "./Alert.vue";
import ProductRow from "./ProductRow.vue";

export default {
  data() {
    return {
      activeAddProductModal: false,
      addProductForm: {
        name: "",
        description: "",
        liked: false,
        price: 0,
      },
      message: "",
      products: [],
      showMessage: false,
      stripe: null,
    };
  },
  components: {
    Alert,
    ProductRow,
  },
  methods: {
    addProduct(payload) {
      axios
        .post("http://localhost:8000/products", payload)
        .then(() => {
          this.getProducts();
          this.message = "Products added successfully!";
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getProducts();
        });
    },
    getProducts() {
      axios
        .get("http://localhost:8000/products")
        .then((response) => {
          this.products = response.data.products;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getStripePublishableKey() {
      fetch("http://localhost:8000/config")
        .then((result) => result.json())
        .then((data) => {
          // Initialize Stripe.js
          this.stripe = Stripe(data.publicKey);
        });
    },

    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      this.toggleAddProductModal();
      let liked = false;
      if (this.addProductForm.liked) {
        liked = true;
      }
      this.addProduct({
        name: this.addProductForm.name,
        description: this.addProductForm.description,
        liked,
        price: this.addProductForm.price,
      });
      this.initForm();
    },
    handlePurchaseProduct(product) {
      console.log(product.id);
      fetch("http://localhost:8000/create-checkout-session", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ product_id: product.id }),
      })
        .then((result) => result.json())
        .then((data) => {
          console.log(data);
          // Redirect to Stripe Checkout
          return this.stripe.redirectToCheckout({ sessionId: data.sessionId });
        })
        .then((res) => {
          console.log(res);
        });
    },
    initForm() {
      this.addProductForm = {
        name: "",
        description: "",
        liked: false,
        price: 0,
      };
    },
    toggleAddProductModal() {
      const body = document.querySelector("body");
      this.activeAddProductModal = !this.activeAddProductModal;
      if (this.activeAddProductModal) {
        body.classList.add("modal-open");
      } else {
        body.classList.remove("modal-open");
      }
    },
  },
  created() {
    this.getProducts();
    this.getStripePublishableKey();
    this.showMessage = false;
  },
};
</script>
