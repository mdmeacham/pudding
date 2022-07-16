import { defineStore } from "pinia";
import axios from "axios";

export const useCustomerStore = defineStore("customers", {
  state: () => ({
    customers: [],
  }),
  getters: {},
  actions: {
    async fetchCustomers() {
      const results = await axios.get("http://localhost:8000/customers");
      this.customers = results.data;
    },
  },
});
