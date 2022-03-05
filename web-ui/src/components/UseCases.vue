<template>
  <div class="ma-5">
    <v-btn text x-small color="primary" @click="onNewUseCaseDialog">
      New
      <v-icon right dark> mdi-plus </v-icon>
    </v-btn>
    <div class="use-cases">
      <div v-for="(use, i) in uses" :key="i" class="case-container">
        <div class="case-header">
          <div class="case-name text-subtitle-2">
            <a href="#" @click="onUseSelect(use)">{{ use.name }}</a>
          </div>
          <div class="case-qty text-body-2">{{ use.seats }} seats</div>
          <div class="case-status text-body-2">3 of 5 criteria met</div>
        </div>
        <div class="case-description text-body-2">
          <p>
            {{ use.description }}
          </p>
        </div>
      </div>
    </div>
    <UseCaseDialog
      :show="showUseCaseDialog"
      v-on:UseCaseDialogClosed="onUseCaseDialogClosed"
      :currentName="selectedUse.name"
      :currentDescription="selectedUse.description"
      :currentSeats="selectedUse.seats"
    />
  </div>
</template>

<script>
import axios from 'axios';
import UseCaseDialog from './UseCaseDialog.vue';

export default {
  props: ['poc_id'],
  components: {
    UseCaseDialog,
  },

  mounted() {
    this.fetchUses();
  },

  watch: {
    poc_id: function () {
      this.fetchUses();
    },
  },

  data() {
    return {
      uses: [],
      showUseCaseDialog: false,
      selectedUse: {},
    };
  },

  methods: {
    fetchUses() {
      axios
        .get('http://localhost:8000/pocs/' + this.poc_id + '/uses')
        .then((response) => {
          this.uses = response.data;
          console.log('after fetch the uses is', this.uses);
        });
    },
    onNewUseCaseDialog() {
      this.selectedUse = {};
      this.showUseCaseDialog = true;
    },
    onUseCaseDialogClosed(action, name, seats, description) {
      if (action != 'cancel') {
        if (Object.keys(this.selectedUse).length === 0) {
          var newUse = {
            id: 0,
            name: name,
            description: description,
            seats: parseInt(seats),
            poc_id: parseInt(this.poc_id),
          };
          axios
            .post('http://localhost:8000/pocs/' + this.poc_id + '/uses', newUse)
            .then((response) => {
              this.uses.push(response.data);
            });
        } else {
          let updatedPOC = {
            id: this.selectedUse.id,
            name: name,
            description: description,
            seats: parseInt(seats),
            poc_id: parseInt(this.poc_id),
          };
          console.log('updated pOC about to send is', updatedPOC);
          axios
            .put(
              'http://localhost:8000/pocs/' + this.poc_id + '/uses',
              updatedPOC
            )
            .then((response) => {
              console.log(response);
              this.selectedUse.name = name;
              this.selectedUse.seats = seats;
              this.selectedUse.description = description;
            });
        }
      }
      this.showUseCaseDialog = false;
    },
    onUseSelect(use) {
      this.selectedUse = use;
      this.showUseCaseDialog = true;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.use-cases {
  margin-top: 10px;
}
.case-container {
  padding: 15px 10px 0 10px;
  display: flex;
  flex-direction: column;
}

.case-header {
  display: flex;
  width: max-content;
}

.case-qty {
  width: max-content;
  padding-left: 15px;
  overflow: hidden;
  text-overflow: ellipsis;
}
.case-status {
  width: max-content;
  padding-left: 15px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.case-description {
  padding-left: 15px;
  max-width: 600px;
}
</style>
