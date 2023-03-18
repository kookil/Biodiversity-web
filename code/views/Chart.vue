<template>
<div class='container1'>
  <el-row
  :gutter="24">
    <el-col
      
      :span="6"
      :offset="index > 0 ? 0 : 0"
    >
      <el-card :body-style="{ padding: '10px'}">
        <img
          src="../assets/images/chart/chart1.png"
          class="image"
        />
        <div style="padding: 14px">
          <span>中国濒危物种红色名录中各物种生存状态</span>
          <div class="bottom">
            <el-button type="text1" class="button" @click="cimsInputClick1">查看详情</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
        <el-col
      
      :span="6"
      :offset="index > 0 ? 0 : 0"
    >
      <el-card :body-style="{ padding: '10px'}">
        <img
          src="../assets/images/chart/chart2.png"
          class="image"
        />
        <div style="padding: 14px">
          <span>中国濒危物种红色名录中受贸易影响最大的前50种生物生存状态</span>
          <div class="bottom">
            <el-button type="text2" class="button" @click="cimsInputClick2">查看详情</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
        <el-col
      
      :span="6"
      :offset="index > 0 ? 0 : 0"
    >
      <el-card :body-style="{ padding: '10px'}">
        <img
          src="../assets/images/chart/chart3.png"
          class="image"
        />
        <div style="padding: 14px">
          <span>中国十大珍稀动物&中国十大珍稀植物</span>
          <div class="bottom">
            <el-button type="text3" class="button" @click="cimsInputClick3">查看详情</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
        <el-col
      
      :span="6"
      :offset="index > 0 ? 0 : 0"
    >
      <el-card :body-style="{ padding: '10px'}">
        <img
          src="../assets/images/chart/chart4.png"
          class="image"
        />
        <div style="padding: 14px">
          <span>各生态系统中不同种群数目变化趋势</span>
          <div class="bottom">
            <el-button type="text4" class="button" @click="cimsInputClick4">查看详情</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
  </div>
</template>


<script>
export default {
  data(){
		return {

		}
  },

  methods: {
    cimsInputClick1 () {
          let text1= this.$router.resolve({
            path: '/chart1'
          });
          
     // 打开一个新的页面     
     window.open(text1.href, '_blank')
    },
    cimsInputClick2 () {
          let text2= this.$router.resolve({
            path: '/chart2'
          });
          
     // 打开一个新的页面     
     window.open(text2.href, '_blank')
    },
    cimsInputClick3 () {
          let text3= this.$router.resolve({
            path: '/chart3'
          });
          
     // 打开一个新的页面     
     window.open(text3.href, '_blank')
    },
    cimsInputClick4 () {
          let text4= this.$router.resolve({
            path: '/chart4'
          });
          
     // 打开一个新的页面     
     window.open(text4.href, '_blank')
    },
  }
}
</script>

<style>

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 80%;
  display: block;
}

.container1{
  position: absolute;
	top: 100px;
	left: 0;
	right: 0;
	bottom: 0;
}

  .el-card {
    min-width: 380px;
    margin-right: 20px;
    transition: all .5s;
  }
  .el-card:hover{
    margin-top: -5px;
  }
</style>
