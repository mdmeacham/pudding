<template>
  <v-dialog width="300" v-model="show">
    <v-card>
      <v-card-title primary-title>{{ editorRoles }}</v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="editorFirstName"
            label="First Name"
            required
          ></v-text-field>
          <v-text-field
            v-model="editorLastName"
            label="Last Name"
            required
          ></v-text-field>
          <v-text-field
            v-model="editorTitle"
            label="Title"
            required
          ></v-text-field>

          <v-autocomplete
            v-model="editorRoles"
            :items="availableRoles"
            dense
            chips
            small-chips
            label="Roles"
            multiple
            solo
          ></v-autocomplete>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="onSaveClicked"> Save </v-btn>
        <v-btn
          color="primary"
          text
          @click="$emit('ContactDialogClosed', 'cancel')"
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
  props: ['show', 'currentFirstName', 'currentLastName', 'currentTitle'],
  mounted() {
    axios.get('http://localhost:8000/roles').then((response) => {
      this.availableRoles = response.data.map((role) => {
        return { text: role.role, value: role.id };
      });
    });
  },
  watch: {
    show: function () {
      //this.fetchCustomerSelections('');
    },
    currentFirstName: function () {
      this.editorFirstName = this.currentFirstName;
    },
    currentLastName: function () {
      this.editorLastName = this.currentLastName;
    },
    currentTitle: function () {
      this.editorTitle = this.currentTitle;
    },
    search(val) {
      console.log(val);
      //val !== this.select && this.fetchCustomerSelections(val);
    },
  },
  data() {
    return {
      editorFirstName: '',
      editorLastName: '',
      editorTitle: '',
      editorRoles: [],
      availableRoles: [],
      search: null,
    };
  },
  methods: {
    /*fetchCustomerSelections(searchTerm) {
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
    },*/
    onSaveClicked() {
      this.$emit(
        'ContactDialogClosed',
        'save',
        this.editorFirstName,
        this.editorLastName,
        this.editorTitle,
        this.editorRoles
      );
      /*let customer = {};
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
        }); */
    },
  },
};
</script>
<style scoped></style>
