import { defineStore } from 'pinia';
import axios from 'axios';

export const usePOCStore = defineStore('pocs', {
  state: () => ({
    stages: [],
    pocsByStage: [],
    selectedPOC: {},
  }),
  getters: {
    pocsForStage(state) {
      return (stageID) =>
        state.pocsByStage.find((stage) => stage.id == stageID).pocs;
    },
  },
  actions: {
    async fetchStages() {
      const results = await axios.get('http://localhost:8000/stages');
      this.stages = results.data;
      for (let i = 0; i < this.stages.length; i++) {
        this.pocsByStage.push({
          id: this.stages[i].id,
          name: this.stages[i].name,
          pocs: [],
        });
      }
    },
    addPOC(poc) {
      this.pocsByStage
        .find((stage) => stage.id === poc.stage_id)
        .pocs.push(poc);
    },
    savePOC(poc) {
      axios.post('http://localhost:8000/pocs', poc);
    },
    async fetchPOCsForStage(stageID) {
      const results = await axios.get(
        'http://localhost:8000/pocs/stage/' + stageID
      );
      this.pocsByStage.find((stage) => stage.id == stageID).pocs = results.data;
    },
    async deletePOC() {
      const results = await axios.delete(
        'http://localhost:8000/pocs/' + this.selectedPOC.id
      );
      if (results.data.result === 'success') {
        this.pocs = this.pocs.filter((poc) => poc.id !== this.selectedPOC.id);
        this.selectedPOC = {};
      }
    },
    selectPOC(poc) {
      this.selectedPOC = poc;
    },
  },
});
