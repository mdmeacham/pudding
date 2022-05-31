<script setup>
defineProps({
  show: Boolean,
});
</script>

<template>
  <div class="modal" :class="{ showing: show }">
    <div class="modal-content">
      <slot> </slot>
      <div>
        <button @click="$emit('closed', 'cancel')">Cancel</button>
        <button @click="$emit('closed', 'save')">Save</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal {
  display: none;
  position: fixed;
  width: 100%;
  height: 100%;
  z-index: 1;
  left: 0;
  top: 0;
  background-color: rgba(0, 0, 0, 0.4);
}

.showing {
  display: block;
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}
</style>
