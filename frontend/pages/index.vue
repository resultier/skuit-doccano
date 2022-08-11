<template>
  <v-main>
    <the-top-banner />
    <feature-cards />
    <the-bottom-banner />
  </v-main>
</template>

<script>
import FeatureCards from '@/components/layout/FeatureCards'
import TheTopBanner from '@/components/layout/TheTopBanner'
import TheBottomBanner from '@/components/layout/TheBottomBanner'

export default {
  components: {
    FeatureCards,
    TheTopBanner,
    TheBottomBanner
  }
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
  *{
    font-family: "Poppins","sans-serif" !important;
  }
</style>