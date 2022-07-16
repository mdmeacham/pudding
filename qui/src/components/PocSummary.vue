<script setup>
import { ref, reactive, defineEmits, onMounted } from "vue";
import { usePOCStore } from "../stores/pocs";
import { useCustomerStore } from "../stores/customers";

const pocStore = usePOCStore();
const customerStore = useCustomerStore();

const editorVars = reactive({});
const editorSelectedCustomer = ref({});
const emit = defineEmits(["summaryUpdated"]);

const props = defineProps({});

pocStore.$subscribe((mutation, state) => {
  setCustomerInSelect();
  resetEditorVars();
});

onMounted(async () => {
  await customerStore.fetchCustomers();
  setCustomerInSelect();
  resetEditorVars();
});

function setCustomerInSelect() {
  for (let i = 0; i < customerStore.customers.length; i++) {
    if (customerStore.customers[i].id == pocStore.selectedPOC.customer_id) {
      editorSelectedCustomer.value = customerStore.customers[i];
    }
  }
}

function resetEditorVars() {
  editorVars.id = pocStore.selectedPOC.id;
  editorVars.name = pocStore.selectedPOC.name;
  editorVars.stage_id = pocStore.selectedPOC.stage_id;
  editorVars.se_id = pocStore.selectedPOC.se_id;
  editorVars.customer_id = pocStore.selectedPOC.customer_id;
}

function summaryUpdated(key, value) {
  emit("summaryUpdated", key, value);
}
</script>
<template>
  <div>
    <div class="row">
      <div class="col">
        <q-input
          class="q-pa-md"
          v-model="editorVars.name"
          @update:model-value="
            (value) => {
              summaryUpdated('name', value);
            }
          "
          label="Name"
        />
      </div>
      <div class="col">
        <q-select
          class="q-pa-md"
          input-debounce="0"
          use-input
          hide-selected
          fill-input
          v-model="editorSelectedCustomer"
          label="Customer"
          @update:model-value="
            (value) => {
              summaryUpdated('customer_id', value);
            }
          "
          option-value="id"
          option-label="name"
          :options="customerStore.customers"
        >
          <template v-slot:selected>
            {{ editorSelectedCustomer.label }}
          </template>
        </q-select>
      </div>
    </div>
  </div>
</template>
