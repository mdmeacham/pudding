<script setup>
import { defineEmits, onMounted, reactive, watch } from "vue";

onMounted(() => {});

const props = defineProps({
  items: Array,
  selectedItem: Object,
  caller: String,
  categoryField: String,
  listField: String,
  itemField: String,
});

watch(
  () => props.selectedItem,
  (selection, prevSelection) => {
    if (props.caller == "nav") return;
    for (let i = 0; i < props.items.length; i++) {
      for (let j = 0; j < props.items[i].pocs.length; j++) {
        console.log("going around", i, j);
        if (props.items[i].pocs[j] === selection) {
          expanded[i] = true;
        }
      }
    }
  }
);

const emit = defineEmits(["expand", "select"]);
const expanded = reactive([]);
function select(item) {
  emit("select", item);
}

function expand(i) {
  emit("expand", props.items[i].id);
}
</script>

<template>
  <q-list>
    <q-expansion-item
      v-for="(category, i) in items"
      @show="expand(i)"
      v-model="expanded[i]"
      :key="i"
      :label="category[categoryField]"
    >
      <q-list>
        <q-item
          clickable
          v-for="(item, j) in category[listField]"
          :key="j"
          :active="item === selectedItem"
          @click="select(item)"
          v-on:click.stop
        >
          <q-item-section class="q-pl-lg">{{ item[itemField] }}</q-item-section>
        </q-item>
      </q-list>
    </q-expansion-item>
  </q-list>
</template>

<style scoped>
.category-header {
  cursor: pointer;
}

.category-name {
  line-height: 24px;
}

.header-items {
  padding: 5px 5px 5px 0;
  font-weight: bold;
  display: flex;
  flex-direction: row;
  align-content: center;
}
.category-list {
  display: none;
  margin-left: 10px;
}

.expand-icon {
  transition: transform 0.1s ease-in-out;
}

.rotated {
  transform: rotate(180deg);
}

.expand {
  display: block;
}

.item {
  padding: 5px;
}
</style>
