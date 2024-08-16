<template>
  <tr>
    <td>{{ product.name }}</td>
    <td>{{ product.description }}</td>
    <td>
      <span v-if="product.liked">Yes</span>
      <span v-else>No</span>
    </td>
    <td>{{ product.price }}</td>
    <td>
      <div class="btn-group" role="group">
        <!-- <button type="button" class="btn btn-warning btn-sm">Update</button>
        <button
          type="button"
          class="btn btn-danger btn-sm"
          @click="onDeleteProduct(product)"
        >
          Delete
        </button> -->
        <button
          type="button"
          class="btn btn-warning btn-sm"
          @click="onPurchaseProduct(product, false)"
        >
          Purchase (Redirect)
        </button>
        <button
          type="button"
          class="btn btn-danger btn-sm"
          @click="onPurchaseProduct(product, true)"
        >
          Purchase (NewTab)
        </button>
        <router-link
          :to="`/checkout`"
          type="button"
          class="btn btn-primary btn-sm"
          >Purchase (InApp)</router-link
        >
      </div>
    </td>
  </tr>
</template>

<script>
export default {
  name: "ProductRow",
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
  methods: {
    onDeleteProduct(product) {
      this.$emit("delete-product", product);
    },
    onPurchaseProduct(product, newTab) {
      this.$emit("purchase-product", product, newTab);
    },
  },
};
</script>

<style scoped>
/* 在这里添加样式 */
</style>
