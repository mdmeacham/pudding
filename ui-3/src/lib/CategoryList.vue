<script setup>
import { ref, defineEmits } from 'vue';

const props = defineProps({
  items: Array,
  expanded: Array,
  selectedItem: Object,
  categoryField: String,
  listField: String,
  itemField: String,
});

//const selectedItem = ref({});

const emit = defineEmits(['expand', 'select']);
const expandedCategories = ref(props.expanded);

function expand(i) {
  if (expandedCategories.value.includes(i)) {
    expandedCategories.value.splice(expandedCategories.value.indexOf(i), 1);
  } else {
    emit('expand', props.items[i].id);
    expandedCategories.value.push(i);
  }
}

function select(item) {
  //selectedItem.value = item;
  emit('select', item);
}
</script>

<template>
  <div>
    <div
      class="category-header"
      @click="expand(i)"
      v-for="(category, i) in items"
      :key="i"
    >
      <div class="header-items">
        <span
          class="material-symbols-outlined expand-icon"
          :class="{ rotated: expandedCategories.includes(i) }"
        >
          expand_more
        </span>
        <div class="category-name">{{ category[categoryField] }}</div>
      </div>
      <div
        class="category-list"
        :class="{ expand: expandedCategories.includes(i) }"
      >
        <div
          class="item"
          v-for="(item, j) in category[listField]"
          :key="j"
          :class="{ selected: item === selectedItem }"
          @click="select(item)"
          v-on:click.stop
        >
          {{ item[itemField] }}
        </div>
      </div>
    </div>
  </div>
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

.selected {
  background-color: #2c8c99;
}
</style>
