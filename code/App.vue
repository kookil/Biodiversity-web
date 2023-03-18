<template>

  <div id="app">
    <!-- 路由占位符 -->
    <router-view></router-view>
    <navimenu></navimenu>
  </div>
  
</template>

<script>
import Navimenu from './components/Navimenu.vue'
export default {
  name: 'App',
  components:{
    Navimenu
  }
}

</script>

<style>
html,
body,
#app{
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;  
}
</style>


