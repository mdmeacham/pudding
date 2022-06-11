<script setup>
import { onMounted } from 'vue';
import { usePOCStore } from '@/stores/pocs';
import { useRouter } from 'vue-router';
import CategoryList from '@/lib/CategoryList.vue';

const store = usePOCStore();
const router = useRouter();

onMounted(() => {
  if (store.stages.length === 0) store.fetchStages();
});

function selectPOC(poc) {
  console.log('selected', poc);
  store.selectPOC(poc);
  router.push({ name: 'poc', params: { id: poc.id } });
}

function onStageExpand(stageID) {
  if (store.pocsByStage.find((stage) => stage.id === stageID).pocs.length === 0)
    store.fetchPOCsForStage(stageID);
}

function addPOC() {
  let newPOC = {
    id: 0,
    name: 'New POC',
    stage_id: 1,
    se_id: 0,
    customer_id: 0,
  };
  store.addPOC(newPOC);
  store.selectPOC(newPOC);
  router.push({ name: 'poc', params: { id: 0 } });
}
</script>

<template>
  <div class="left-list-pane">
    <div class="list-header">
      <div class="header-title">POCs</div>
      <div class="header-action">
        <button @click="addPOC" class="btn">
          <i class="material-symbols-outlined btn-icon"> add </i>
        </button>
      </div>
    </div>
    <CategoryList
      :expanded="[]"
      :items="store.pocsByStage"
      :selectedItem="store.selectedPOC"
      categoryField="name"
      listField="pocs"
      itemField="name"
      @expand="onStageExpand"
      @select="selectPOC"
    />
  </div>
  <div class="list-item-detail">
    <router-view />
  </div>
</template>

<style scoped>
.left-list-pane {
  background-color: #326771;
  color: #fff;
}
.selected {
  background-color: aliceblue;
}

.list-header {
  display: flex;
  padding: 2px 10px 2px 10px;
  color: #fff;
  flex-direction: row;
  align-items: center;
  background-color: #2c8c99;
  justify-content: space-between;
}

.list-item {
  cursor: pointer;
  padding-top: 5px;
  padding-bottom: 5px;
}

.list-item-detail {
  margin-left: 20px;
}
</style>
