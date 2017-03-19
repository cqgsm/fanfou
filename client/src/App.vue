<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
@import '../static/scss/index.scss';
#app{
  max-width: 640px;
  margin: 0 auto;
}
</style>
