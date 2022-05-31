import { defineStore } from 'pinia';

export const useVerticalStore = defineStore('verticals', {
  state: () => ({
    verticals: [
      { id: 1, name: 'Healthcare' },
      { id: 2, name: 'Retail' },
    ],
  }),
  actions: {
    addVertical(vertical) {
      this.verticals.push(vertical);
    },
  },
});
