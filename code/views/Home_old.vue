<template>
  <div id="home">
    <el-carousel id='carousel' height="500px" interval=10000>
      <el-carousel-item v-for="bgitem in totalbg" :key="bgitem">
        <el-image
          style="width: 100%; height: 100%" 
          :src="require('../assets/images/home/home'+bgitem+'.png')" 
          fit="fill"></el-image>
      </el-carousel-item>
    </el-carousel>
    <div id="info">
      <el-image style="width: 90; height: 30px; top: 10px; margin: 0 30px; display: inline-block" 
                :src="require('../assets/images/logo/ecnu.png')" fit="fill"></el-image>
      <p id='text'>©2022 华东师范大学地理科学学院"生物多样性保护和管理"项目小组</p> 
      <!-- <p id='text'>©2022春 计算机综合实践第三小组</p>-->
    </div>
    <!-- <myfooter id='myfooter'></myfooter> -->
  </div>
</template>

<script>
export default {
  components: {  },
  data(){
		return {
			totalbg: 2,
		}
  },

  methods: {

  }
}
</script>

<style scoped>
html,
body{
  margin: 0;
  padding: 0;
  height: 1830px;
}

/* #home{
  position: absolute;
  top: 65px;
  left: 380px;
  width: 70%;
  height: 88%;
} */

#home{
  position: absolute;
  top: 65px;
  width: 100%;
  height: 81%;
  /* height: 1830px; */
}

#carousel{
  position: absolute;
  width: 100%;
}

button{
  width: 50px;
  height: 50px;
  display: inline-block;
}
#info{
  position: absolute;
  top: 500px;
  width: 100%;
  height: 50px;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}

#text{
  display: inline-block;
}

#myfooter{
  position: absolute;
  bottom: 0;
  height: 300px;
  width: 100%;
}
</style>
