<template>
  <div>
    <v-tabs v-model="tab">
      <v-tab>Status</v-tab>
      <v-tab>Use Cases</v-tab>
      <v-tab>Success Criteria</v-tab>
      <v-tab>Team</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item>
        <p>This will be status content</p>
      </v-tab-item>
      <v-tab-item>
        <UseCases :poc_id="poc_id" />
      </v-tab-item>
      <v-tab-item>
        <p>This is two</p>
      </v-tab-item>
      <v-tab-item> <Team :customer_id="poc.customer_id" /> </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import UseCases from './UseCases.vue';
import Team from './Team.vue';
import axios from 'axios';

export default {
  components: {
    UseCases,
    Team,
  },
  mounted() {
    this.fetchPOC();
  },
  watch: {
    $route: function () {
      console.log('in POC componente route watch hit');
      this.fetchPOC();
    },
  },

  data() {
    return {
      poc_id: 0,
      poc: {},
      tab: null,
    };
  },
  methods: {
    fetchPOC() {
      this.poc_id = this.$route.params.poc_id;
      axios
        .get('http://localhost:8000/pocs/' + this.poc_id)
        .then((response) => {
          this.poc = response.data;
          console.log(
            'Just changed company id in parent poc to',
            this.poc.customer_id
          );
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
