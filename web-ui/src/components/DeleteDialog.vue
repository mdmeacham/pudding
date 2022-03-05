<template>
  <v-dialog width="300" v-model="show">
    <v-card>
      <v-card-title primary-title></v-card-title>
      <v-card-text>Delete {{ name }} permanently?</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="primary"
          text
          @click="$emit('deleteDialogClosed', 'delete')"
        >
          Delete
        </v-btn>
        <v-btn
          color="primary"
          text
          @click="$emit('deleteDialogClosed', 'cancel')"
        >
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  components: {},
  props: ['show', 'name'],
  data() {
    return {};
  },
  methods: {},
};
</script>
<style scoped></style>
