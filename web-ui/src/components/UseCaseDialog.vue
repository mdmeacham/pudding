<template>
  <v-dialog v-model="show" persistent max-width="600px">
    <v-card>
      <v-card-title> </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Use case name"
                v-model="editorName"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Qty seats"
                v-model="editorSeats"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-textarea
                label="Description"
                v-model="editorDescription"
              ></v-textarea>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="blue darken-1"
          text
          @click="$emit('UseCaseDialogClosed', 'cancel')"
        >
          Cancel
        </v-btn>
        <v-btn
          color="blue darken-1"
          text
          @click="
            $emit(
              'UseCaseDialogClosed',
              'save',
              editorName,
              editorSeats,
              editorDescription
            )
          "
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  components: {},
  props: ['show', 'currentName', 'currentDescription', 'currentSeats'],
  watch: {
    currentName: function () {
      this.editorName = this.currentName;
      this.editorDescription = this.currentDescription;
      this.editorSeats = this.currentSeats;
    },
  },
  data() {
    return {
      editorName: '',
      editorDescription: '',
      editorSeats: 0,
    };
  },
  methods: {},
};
</script>
<style scoped></style>
