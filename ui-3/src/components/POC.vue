<script setup>
import { ref } from 'vue';
import { usePOCStore } from '@/stores/pocs';
import TextInput from '@/lib/TextInput.vue';

const store = usePOCStore();
const testvar = ref('');
</script>

<template>
  <div class="poc-detail">
    <div class="poc-toolbar"></div>
    <div class="poc-form">
      <TextInput input-type="simple" label="Name" v-model="testvar" />
      <TextInput input-type="lookup" label="Stage" />
      <TextInput input-type="lookup" label="Customer" />
    </div>
  </div>
</template>

<style scoped>
.poc-detail {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 24px;
}
</style>
