<script setup>
import { ref } from 'vue';

const props = defineProps({
  modelValue: String,
  label: String,
  selectItems: Array,
  itemKey: String,
});

const emit = defineEmits(['update:modelValue']);

function updateValue(value) {
  emit('update:modelValue', value);
}

const expand = ref(false);
const selectedItem = ref({});

function expandSelection() {
  expand.value = !expand.value;
}

function selectItem(item) {
  expand.value = false;
  selectedItem.value = item;
  updateValue(item[props.itemKey]);
}
</script>

<template>
  <div class="container">
    <input
      class="text-input"
      type="text"
      placeholder=" "
      :value="selectedItem[itemKey]"
    />
    <div class="label">{{ label }}</div>
    <div @click="expandSelection" class="pull-down">
      <span
        class="material-symbols-outlined expand-icon"
        :class="{ rotated: expand }"
      >
        expand_more
      </span>
    </div>
    <div class="expansion-box" :class="{ expand: expand }">
      <div
        @click="selectItem(item)"
        v-for="(item, i) in selectItems"
        :key="i"
        class="selection-items"
      >
        {{ item[itemKey] }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  position: relative;
  height: 40px;
  padding: 24px 0 24px 0;
  margin-bottom: 15px;
}

.label {
  position: absolute;
  top: 0;
  left: 0;
  margin: 0;
  transform-origin: 0 0;
  pointer-events: none;
  transform: translate3d(0, 30px, 0);
  font-size: 14px;
  line-height: 14px;
  text-transform: uppercase;
  transition: transform 0.2s;
}

.text-input {
  width: 100%;
  border: none;
  border-bottom: solid 1px grey;
  outline: none;
  font-size: 16px;
  line-height: 20px;
}

.text-input:focus + .label,
.text-input:not(:placeholder-shown) + .label {
  transform: translate3d(0, 10px, 0) scale(0.75);
}

.text-input:focus {
  border-bottom: solid 1px black;
}

.pull-down {
  position: absolute;
  right: 0;
  padding: 5px;
  margin: 5px;
  top: 15px;
  cursor: pointer;
}

.expand-icon {
  transition: transform 0.1s ease-in-out;
}

.expansion-box {
  position: absolute;
  cursor: pointer;
  top: 25px;
  left: 0;
  padding: 10px 0 10px 0;
  display: none;
  border-color: #fff;
  z-index: 1;
  background: #fff;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}

.expand {
  display: block;
}

.selection-items {
  padding: 5px 15px 5px 15px;
}

.selection-items:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.rotated {
  transform: rotate(180deg);
}
</style>
