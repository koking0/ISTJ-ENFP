<script setup>
import HelloWorld from './views/HelloWorld.vue'
</script>

<template>
  <div>
    <a href="https://www.16personalities.com/istj-personality" target="_blank">
      <img src="./assets/istj-logistician.png" class="logo ISTJ" alt="ISTJ logo" />
    </a>
    <a href="https://www.16personalities.com/enfp-personality" target="_blank">
      <img src="./assets/enfp-campaigner.png" class="logo ENFP" alt="ENFP logo" />
    </a>
  </div>
  <HelloWorld msg="当 ISTJ 遇上 ENFP" />
</template>

<style scoped>
.logo {
  height: 20em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
</style>
