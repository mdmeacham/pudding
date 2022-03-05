<template>
  <v-app>
    <v-system-bar app></v-system-bar>
    <v-navigation-drawer :width="350" app permanent>
      <POCList />
    </v-navigation-drawer>
    <v-main>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import POCList from './components/POCList.vue';
export default {
  components: {
    POCList,
  },
  data() {
    return {};
  },
};
</script>

<style scoped></style>
