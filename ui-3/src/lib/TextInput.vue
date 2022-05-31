<script setup>
defineProps({
  modelValue: String,
  label: String,
  inputType: String,
});

const emit = defineEmits(['update:modelValue']);

const updateValue = (event) => {
  emit('update:modelValue', event.target.value);
};
</script>

<template>
  <div class="input-container">
    <input
      class="text-input"
      type="text"
      placeholder=" "
      :value="modelValue"
      @input="updateValue"
    />
    <div class="label">{{ label }}</div>
  </div>
</template>

<style scoped>
.input-container {
  display: block;
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
  appearance: none;
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
</style>
