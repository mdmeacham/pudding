<template>
  <div class="poc-list">
    <v-treeview
      return-object
      hoverable
      :load-children="fetchPOCsForStage"
      activatable
      :active.sync="activePOCs"
      :items="pocs"
    >
      <template v-slot:label="{ item }">
        <div
          class="poc-label"
          :pocid="item.id"
          :pocname="item.name"
          :stagename="item.stage_name"
          menutype="something"
          @contextmenu="onShowMenu"
          @click="navToPOC(item.id)"
        >
          <!--button icon-->
          <template v-if="item.customer_name != undefined"
            >{{ item.customer_name }} -
          </template>
          {{ item.name }}
        </div>
      </template>
    </v-treeview>
    <v-menu
      v-model="showMenu"
      offset-y
      :position-x="x"
      :position-y="y"
      absolute
    >
      <v-list>
        <v-list-item
          v-for="menuItem in menuItems"
          :key="menuItem"
          @click="menuSelection(menuItem)"
        >
          <v-list-item-title>{{ menuItem }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <POCEditDialog
      :show="showEditDialog"
      :currentName="activePOCs[0] ? activePOCs[0].name : ''"
      :currentCustomerID="activePOCs[0] ? activePOCs[0].customer_id : ''"
      v-on:editDialogClosed="onEditDialogClosed"
    />
    <DeleteDialog
      :show="showDeleteDialog"
      :name="activePOCs[0] ? activePOCs[0].name : ''"
      v-on:deleteDialogClosed="onDeleteDialogClosed"
    />
  </div>
</template>

<script>
import axios from 'axios';
import POCEditDialog from './POCEditDialog.vue';
import DeleteDialog from './DeleteDialog.vue';

export default {
  components: {
    POCEditDialog,
    DeleteDialog,
  },

  data() {
    return {
      InExecution: [],
      InPreparation: [],
      OnHold: [],
      Completed: [],
      Canceled: [],
      showMenu: false,
      activePOCs: [],
      rightClickPOCID: -1,
      rightClickStageName: '',
      menuItems: [],
      showEditDialog: false,
      showDeleteDialog: false,
      x: 0,
      y: 0,
    };
  },

  computed: {
    pocs: function () {
      return [
        {
          name: 'In Execution',
          id: 'top1',
          children: this.InExecution,
        },
        {
          name: 'In Preparation',
          id: 'top2',
          children: this.InPreparation,
        },
        {
          name: 'On Hold',
          id: 'top4',
          children: this.OnHold,
        },
        {
          name: 'Completed',
          id: 'top3',
          children: this.Completed,
        },
        {
          name: 'Canceled',
          id: 'top5',
          children: this.Canceled,
        },
      ];
    },
  },

  mounted() {
    axios.get('http://localhost:8000/pocs/stage/1').then((response) => {
      this.InExecution = response.data;
    });
  },

  methods: {
    async fetchPOCsForStage(item) {
      let id = item.id.slice(-1);

      await axios
        .get('http://localhost:8000/pocs/stage/' + id)
        .then((response) => {
          this[item.name.replace(/\s+/g, '')] = response.data;
        });
    },
    onShowMenu(e) {
      this.menuItems = [];
      e.preventDefault();

      let el = e.target;
      this.rightClickPOCID = el.getAttribute('pocid');
      this.rightClickStageName = el.getAttribute('stagename');

      // determine if right click was on stage level rather than POC level
      if (!this.rightClickStageName) {
        this.rightClickStageName = 'stageLevel';
      }

      let clickedName = el.getAttribute('pocname');
      if (clickedName == 'In Execution' || clickedName == 'In Preparation') {
        this.menuItems = ['New POC for "' + clickedName + '"'];
      } else if (
        clickedName != 'On Hold' &&
        clickedName != 'Completed' &&
        clickedName != 'Canceled'
      ) {
        this.menuItems = ['Edit', 'Delete'];
      }

      this.showMenu = true;
      this.x = e.clientX;
      this.y = e.clientY;
    },

    menuSelection(selection) {
      if (this.rightClickStageName != 'stageLevel') {
        this.activePOCs = [
          this[this.rightClickStageName.replace(/\s+/g, '')].find(
            (poc) => poc.id == this.rightClickPOCID
          ),
        ];
      }

      switch (selection) {
        case 'Edit':
          this.showEditDialog = true;
          break;
        case 'Delete':
          this.showDeleteDialog = true;
          break;
        case 'New POC for "In Execution"':
          this.activePOCs = [];
          this.showEditDialog = true;
          break;
      }
    },

    onEditDialogClosed(action, newName, customerID, customer) {
      if (action != 'cancel') {
        if (this.activePOCs.length == 0) {
          axios
            .post('http://localhost:8000/pocs', {
              id: 0,
              name: newName,
              se_id: 1,
              stage_id: 1,
              customer_id: customerID,
            })
            .then((response) => {
              response.data.customer_name = customer.name;
              this.InExecution.push(response.data);
              this.activePOCs.push(response.data);
            });
        } else {
          axios
            .put('http://localhost:8000/pocs', {
              id: this.activePOCs[0].id,
              name: newName,
              customer_id: customerID,
              se_id: 1,
              stage_name: this.activePOCs[0].stage_name,
              stage_id: this.activePOCs[0].stage_id,
            })
            .then(() => {
              this.activePOCs[0].name = newName;
              this.activePOCs[0].customer_name = customer.name;
            });
        }
      }
      this.showEditDialog = false;
    },
    navToPOC(poc_id) {
      if (this.$route.params.poc_id != poc_id && typeof poc_id == 'number') {
        this.$router.push({ name: 'poc', params: { poc_id: poc_id } });
      }
    },
    onDeleteDialogClosed(action) {
      this.showDeleteDialog = false;
      if (action == 'delete') {
        axios
          .delete('http://localhost:8000/pocs/' + this.activePOCs[0].id)
          .then(() => {
            let index = this[
              this.rightClickStageName.replace(/\s+/g, '')
            ].findIndex((poc) => poc.id == this.activePOCs[0].id);
            this[this.rightClickStageName.replace(/\s+/g, '')].splice(index, 1);
            this.activePOCs.length = 0;
          });
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.poc-label {
  cursor: pointer;
}
</style>
