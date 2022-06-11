<script setup>
import { watch, reactive, ref, computed, onMounted } from "vue";
import { useRoute } from "vue-router";
import { usePOCStore } from "../stores/pocs";

onMounted(async () => {
  // Check if following direct URL link to a POC
  if (
    route.params.id !== undefined &&
    Object.keys(store.selectedPOC).length === 0
  ) {
    await store.fetchAndSelectPOC(route.params.id);
  }
  initEditorPOC();
});

const store = usePOCStore();
const route = useRoute();

const editorPOC = reactive({});

const pocID = computed(() => {
  return route.params.id;
});

const saveDisabled = computed(() => {
  const keys = Object.keys(store.selectedPOC);
  var same = true;
  for (let i = 0; i < keys.length; i++) {
    if (store.selectedPOC[keys[i]] !== editorPOC[keys[i]]) {
      same = false;
    }
  }
  return same;
});

const tab = ref("summary");

watch(pocID, () => {
  initEditorPOC();
});

function initEditorPOC() {
  const keys = Object.keys(store.selectedPOC);
  for (let i = 0; i < keys.length; i++) {
    editorPOC[keys[i]] = store.selectedPOC[keys[i]];
  }
}
</script>

<template>
  <q-page>
    <q-toolbar class="text-primary">
      <q-btn
        :disabled="saveDisabled"
        flat
        round
        dense
        icon="save"
        class="q-mr-xs"
      />
    </q-toolbar>

    <div class="q-px-md">
      <q-tabs
        v-model="tab"
        class="text-grey"
        active-color="primary"
        indicator-color="primary"
        align="justify"
      >
        <q-tab name="summary" label="Summary" />
        <q-tab name="criteria" label="Criteria" />
        <q-tab name="notes" label="Notes" />
      </q-tabs>
    </div>

    <q-tab-panels v-model="tab" animated>
      <q-tab-panel name="summary">
        <q-input v-model="editorPOC.name" label="Name" />
      </q-tab-panel>

      <q-tab-panel name="criteria">
        <div class="text-h6">Criteria</div>
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
      </q-tab-panel>

      <q-tab-panel name="notes">
        <div class="text-h6">Notes</div>
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>
