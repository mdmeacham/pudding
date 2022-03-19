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
                <template v-slot:activator="{}">
                  <v-btn
                    class="ma-5"
                    color="primary"
                    text
                    x-small
                    @click="onContactDialog"
                  >
                    New
                    <v-icon right dark> mdi-plus </v-icon>
                  </v-btn>
                </template>
              </v-dialog>
            </v-toolbar>
          </template>

          <template v-slot:item.roles="{ item }">
            <v-chip
              class="mr-2"
              x-small
              v-for="(role, i) in item.role_list"
              :key="i"
              dark
            >
              {{ role }}
            </v-chip>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <ContactDialog
      :show="showContactDialog"
      v-on:ContactDialogClosed="onContactDialogClosed"
    />
  </div>
</template>

<script>
import axios from 'axios';
import ContactDialog from './ContactDialog.vue';

export default {
  props: ['customer_id'],
  components: { ContactDialog },

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
        { text: 'Roles', value: 'roles', width: '200' },
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
          this.makeRoleArrays();
        });
    },
    makeRoleArrays() {
      this.customerContacts.forEach((contact) => {
        contact.role_list = contact.roles.split(',');
      });
      console.log('the contacts with role list', this.customerContacts);
    },
    onContactDialog() {
      this.showContactDialog = true;
    },
    onContactDialogClosed(action, first_name, last_name, title, roles) {
      console.log('action', action);
      console.log('first', first_name);
      console.log('last', last_name);
      console.log('title', title);
      console.log('roles', roles);
      this.showContactDialog = false;
      if (action === 'save') {
        var newContact = {
          id: 0,
          first_name: first_name,
          last_name: last_name,
          title: title,
          customer_id: this.customer_id,
          roles: roles,
        };
        axios
          .post('http://localhost:8000/contacts', newContact)
          .then((response) => {
            console.log('response from post of contact:', response.data);
          });
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
