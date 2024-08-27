<template>
  <div class="nav-bar"></div>
  <div class="cart">Cart({{ cart }})</div>
  <div class="product-display">
    <div class="product-container">
      <div class="product-image">
        <img :src="product.image" alt="Product" />
      </div>
    </div>
    <div class="product-info">
      <a :href="product.url"
        ><h1>{{ product.name }}</h1></a
      >
      <p v-if="product.inventory > 10">In Stock</p>
      <p v-else-if="product.inventory > 0">Almost Sold Out!</p>
      <p v-else>Out of Stock</p>
      <p v-if="product.onSale">On Sale!</p>
      <p>{{ product.description }}</p>
      <ul>
        <li
          v-for="feature in product.features"
          :key="feature"
          class="product-feature"
        >
          {{ feature }}
        </li>
      </ul>
      <div class="product-variants-container">
        <div
          v-for="variant in variants"
          :key="variant.id"
          class="product-variant"
          @mouseover="updateImage(variant.image)"
          :style="{ backgroundColor: variant.color }"
        ></div>
      </div>
      <div class="product-sizes-container">
        <div v-for="size in sizes" :key="size">
          {{ size }}
        </div>
      </div>

      <p>Price: {{ product.price }}</p>
      <button
        class="button"
        :class="{ disabledButton: !inStock, outOfStockImg: !inStock }"
        :disabled="!inStock"
        @click="addToCart"
      >
        Add to Cart
      </button>
      <br />
      <button class="button" @click="removeFromCart">Remove from Cart</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cart: 0,
      product: {
        name: "Product Name",
        description: "Product Description",
        price: 0,
        inventory: 10,
        onSale: false,
        image: "https://via.assets.so/game.png?id=1&w=200&h=200",
        url: "https://example.com",
        features: ["Feature 1", "Feature 2", "Feature 3"],
      },
      inStock: false,
      brand: "Warren",
      variants: [
        {
          id: 1,
          color: "blue",
          image: "https://via.assets.so/game.png?id=2&w=200&h=200",
        },
        {
          id: 2,
          color: "red",
          image: "https://via.assets.so/game.png?id=3&w=200&h=200",
        },
      ],
      sizes: ["S", "M", "L"],
    };
  },
  methods: {
    addToCart() {
      this.cart += 1;
    },
    updateImage(image) {
      this.product.image = image;
    },
    removeFromCart() {
      if (this.cart > 0) {
        this.cart -= 1;
      }
    },
  },
};
</script>

<style scoped>
.cart {
  display: flex;
  justify-content: flex-end;
  margin-right: 20px;
}
.product-display {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 50px;
}
.product-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 20px;
}
.product-image img {
  width: 200px;
  height: 200px;
}
.product-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.product-feature {
  list-style-type: none;
}
.product-variants-container {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
.product-variant {
  width: 50px;
  height: 50px;
  margin-top: 8px;
  border: 2px solid #d8d8d8;
  border-radius: 50%;
}
.product-sizes-container {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
.disabledButton {
  background-color: #d8d8d8;
  cursor: not-allowed;
}
.outOfStockImg {
  filter: grayscale(100%);
}
</style>
