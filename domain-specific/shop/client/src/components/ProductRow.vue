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
        <button type="button" class="btn btn-warning btn-sm">Update</button>
        <button
          type="button"
          class="btn btn-danger btn-sm"
          @click="onDeleteProduct(product)"
        >
          Delete
        </button>
        <button
          type="button"
          class="btn btn-primary btn-sm"
          @click="onPurchaseProduct(product)"
        >
          Purchase
        </button>
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
    onPurchaseProduct(product) {
      this.$emit("purchase-product", product);
    },
  },
};
</script>

<style scoped>
/* 在这里添加样式 */
</style>
