<template>
  <div class="nav-bar"></div>
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
      <p>Price: {{ product.price }}</p>
      <button @click="addToCart">Add to Cart</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      product: {
        name: "Product Name",
        description: "Product Description",
        price: 0,
        inventory: 10,
        onSale: false,
        image: "https://via.placeholder.com/150",
        url: "https://example.com",
      },
    };
  },
  methods: {
    addToCart() {
      // Add logic to add the product to the cart
    },
  },
};
</script>

<style scoped>
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
  width: 150px;
  height: 150px;
}
.product-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
