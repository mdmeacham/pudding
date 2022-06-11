<script setup>
import { ref } from 'vue';
import { usePOCStore } from '@/stores/pocs';
import TextInput from '@/lib/TextInput.vue';
import SelectItems from '@/lib/SelectItems.vue';
import Lookup from '@/lib/Lookup.vue';

const store = usePOCStore();
const testvar = ref('');
const testvar2 = ref('');
</script>

<template>
  <div class="poc-detail">
    <div class="poc-toolbar"></div>
    <div class="poc-form">
      <TextInput label="Name" v-model="testvar2" />
      <SelectItems
        label="Stage"
        v-model="testvar"
        :select-items="store.stages"
        item-key="name"
      />
      <Lookup label="Customer" />
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
