<template>
  <div class="ma-5">
    <v-row>
      <v-col cols="10">
        <v-data-table
          :headers="contactsHeaders"
          :items="customerContacts"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>{{ customer.name }} team</v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <v-dialog v-model="showContactDialog" max-width="500px">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    class="ma-5"
                    color="primary"
                    text
                    x-small
                    v-bind="attrs"
                    v-on="on"
                  >
                    New
                    <v-icon right dark> mdi-plus </v-icon>
                  </v-btn>
                </template>
              </v-dialog>
            </v-toolbar>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['customer_id'],
  components: {},

  mounted() {
    console.log('mounted in team happened', this.customer_id);
    this.fetchCustomerAndContacts();
  },

  watch: {
    customer_id: function () {
      console.log('watch in team happened');
      this.fetchCustomerAndContacts();
    },
  },

  data() {
    return {
      customer: {},
      showContactDialog: false,
      customerContacts: [],
      contactsHeaders: [
        {
          text: 'Name',
          align: 'start',
          sortable: false,
          value: 'full_name',
          width: '200',
        },
        { text: 'Title', value: 'title', width: '150' },
        { text: 'Role', value: 'role', width: '200' },
      ],
    };
  },

  methods: {
    fetchCustomerAndContacts() {
      axios
        .get('http://localhost:8000/customers/' + this.customer_id)
        .then((response) => {
          this.customer = response.data;
        });
      axios
        .get('http://localhost:8000/contacts/' + this.customer_id)
        .then((response) => {
          console.log('in Team contact fetch, data s', response.data);
          this.customerContacts = response.data;
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
