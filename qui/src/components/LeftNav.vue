<script setup>
import { onMounted, ref, reactive, computed } from "vue";
import { usePOCStore } from "../stores/pocs";
import { useRouter, useRoute } from "vue-router";
import CategoryList from "../lib/CategoryList.vue";

const store = usePOCStore();
const router = useRouter();
const route = useRoute();

onMounted(async () => {
  if (store.stages.length === 0) {
    await store.fetchStages();
  }
});

function selectPOC(poc) {
  store.selectPOC(poc);
  router.push({ name: "poc", params: { id: poc.id, caller: "nav" } });
}

function onStageExpand(stageID) {
  if (store.pocsByStage.find((stage) => stage.id === stageID).pocs.length === 0)
    store.fetchPOCsForStage(stageID);
}

function addPOC() {
  let newPOC = {
    id: 0,
    name: "New POC",
    stage_id: 1,
    se_id: 0,
    customer_id: 0,
  };
  store.addPOC(newPOC);
  store.selectPOC(newPOC);
  router.push({ name: "poc", params: { id: 0, caller: "nav" } });
}
</script>

<template>
  <q-list>
    <q-item-label header> POCs </q-item-label>
    <CategoryList
      :items="store.pocsByStage"
      :selectedItem="store.selectedPOC"
      :caller="route.params.caller"
      categoryField="name"
      listField="pocs"
      itemField="name"
      @select="selectPOC"
      @expand="onStageExpand"
    />
  </q-list>
</template>
