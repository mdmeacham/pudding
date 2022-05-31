<script setup>
import Dialog from '@/lib/Dialog.vue';
import { reactive, defineEmits } from 'vue';
import { usePOCStore } from '@/stores/pocs';

const store = usePOCStore();
const emit = defineEmits(['closed']);

const editorPOC = reactive({
  id: 0,
  name: '',
  customer_id: 1,
  stage_id: 1,
  se_id: 1,
});

defineProps({
  show: Boolean,
});

function closed(action) {
  console.log('closed got here', action);
  if (action == 'save') {
    store.addPOC(editorPOC);
    emit('closed');
  } else {
    emit('closed');
  }
  editorPOC.name = '';
}
</script>

<template>
  <Dialog :show="show" @closed="closed">
    Name: <input v-model="editorPOC.name" />
  </Dialog>
</template>
