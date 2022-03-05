<template>
  <v-dialog width="300" v-model="show">
    <v-card>
      <v-card-title primary-title></v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="editorPOCName"
            label="POC Name"
            required
          ></v-text-field>
          <v-autocomplete
            auto-select-first
            :items="customerNameItems"
            label="Customer Name"
            :search-input.sync="search"
            :value="customerID"
            v-model="customerID"
          ></v-autocomplete>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="onSaveClicked"> Save </v-btn>
        <v-btn
          color="primary"
          text
          @click="$emit('editDialogClosed', 'cancel')"
        >
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios';

export default {
  components: {},
  props: ['show', 'currentName', 'currentCustomerID'],
  watch: {
    show: function () {
      this.fetchCustomerSelections('');
    },
    currentName: function () {
      this.editorPOCName = this.currentName;
    },
    currentCustomerID: function () {
      this.customerID = this.currentCustomerID;
    },
    search(val) {
      val !== this.select && this.fetchCustomerSelections(val);
    },
  },
  data() {
    return {
      editorPOCName: '',
      customerID: '',
      search: null,
      customerNameItems: [],
    };
  },
  methods: {
    fetchCustomerSelections(searchTerm) {
      if (!searchTerm) {
        searchTerm = '';
      }
      //this.customerNameItems.length = 0;
      this.loading = true;
      if (searchTerm === '') {
        axios.get('http://localhost:8000/customers').then((response) => {
          this.customerNameItems = response.data.map((customer) => {
            return { text: customer.name, value: customer.id };
          });
        });
      } else {
        var encodedSearchTerm = searchTerm.replace(/'/g, '%27');
        axios
          .get('http://localhost:8000/customers/filtered/' + encodedSearchTerm)
          .then((response) => {
            console.log('response', response);
            this.customerNameItems = response.data.map((customer) => {
              return { text: customer.name, value: customer.id };
            });
          });
      }
    },
    onSaveClicked() {
      let customer = {};
      axios
        .get('http://localhost:8000/customers/' + this.customerID)
        .then((response) => {
          console.log('the response objec is', response);
          customer = response.data;
          this.$emit(
            'editDialogClosed',
            'save',
            this.editorPOCName,
            this.customerID,
            customer
          );
        });
    },
  },
};
</script>
<style scoped></style>
