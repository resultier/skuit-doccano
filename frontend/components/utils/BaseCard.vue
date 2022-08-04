<template>
  <v-card class="box--transparent">
    <!-- 
    <v-toolbar color="primary white--text" flat>
      <v-toolbar-title>{{ title }}</v-toolbar-title>
    </v-toolbar>
    -->
    <div class="text-center">
      <img
        src="~/assets/images/SKU-it-logo.png"
      />
    </div>
    <h1 class="text-center my-5 bold">
      Train Your AI
    </h1>
    <v-card-text class="text--primary mt-3">
      <slot name="content" />
    </v-card-text>
    <v-card-actions class="px-0">
      <v-spacer />
      <v-btn
        v-if="cancelText"
        class="text-capitalize"
        text
        color="primary"
        data-test="cancel-button"
        @click="cancel"
      >
        {{ cancelText }}
      </v-btn>
      <v-btn
        v-if="agreeText"
        :disabled="disabled"
        class="text-none text-uppercase mt-4"
        block
        data-test="delete-button"
        @click="agree"
      >
        {{ agreeText }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    title: {
      type: String,
      default: '',
      required: true
    },
    cancelText: {
      type: String,
      default: ''
    },
    agreeText: {
      type: String,
      default: ''
    },
    disabled: {
      type: Boolean,
      default: false
    }
  },

  methods: {
    agree() {
      this.$emit('agree')
    },
    cancel() {
      this.$emit('cancel')
    }
  }
})
</script>

<style scoped>
  .box--transparent{
    background: transparent !important;
    box-shadow: none  !important;
  }
  .v-btn{
    background-color: #739BF5 !important;
    color: white !important;
    border-radius: 0;
    box-shadow: none;
    font-family: 'Poppins';
  }
  .v-card__text {
    padding: 0;
  }
  h1{
    color: #4D4D4D;
    font-weight: 700;
  }
  h1,h2,h3,h4,h5,h6{
    font-family: 'Poppins';
  }
  div> img{
    width: 150px;
  }
</style>
