<template>
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
            @click="$emit('toggle-modal')"
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
            <div class="btn-group" role="group">
              <button
                type="button"
                class="btn btn-primary btn-sm"
                @click="$emit('add-submit')"
              >
                Submit
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="$emit('add-reset')"
              >
                Reset
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddProductModal",
  props: {
    activeAddProductModal: {
      type: Boolean,
      required: true,
    },
    addProductForm: {
      type: Object,
      required: true,
    },
  },
};
</script>
