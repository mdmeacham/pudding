<script setup>
import { RouterView } from 'vue-router';
import { usePOCStore } from '@/stores/pocs';

const store = usePOCStore();
store.$reset();
</script>

<template>
  <div class="whole-window">
    <div class="window-remaining">
      <div class="window-nav"></div>
      <div class="window-nav-content">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<style>
@import '@/assets/base.css';

.btn {
  border: none;
  background-color: inherit;
  cursor: pointer;
  height: 28px;
  width: 28px;
  padding: 0;
  border-radius: 50%;
}

.btn:hover {
  background-color: rgb(239, 239, 239);
}

.btn-icon {
  vertical-align: middle;
  color: #fff;
}
</style>

<style scoped>
.whole-window {
  height: 100vh;
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: 1fr;
}

.window-header {
}

.window-remaining {
  display: grid;
  grid-template-columns: 40px auto;
  grid-template-rows: 1fr;
}

.window-nav {
  background-color: #28464b;
}

.window-nav-content {
  display: grid;
  grid-template-columns: 250px auto;
  grid-template-rows: 1fr;
}
</style>
