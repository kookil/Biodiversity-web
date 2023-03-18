<template>
  <div id="home">
    <div class="container">
      <h1 style="text-align: center;">相关专业网站推荐</h1>
      <div class='internet'>
        世界自然保护联盟濒危物种红色名录：<a href="https://www.iucnredlist.org/" target="_blank">https://www.iucnredlist.org/</a><br/><br/>
        中国濒危动物物种信息系统(CESIS)：<a href="https://www.biodiversity-science.net/CN/10.17520/biods.1997050" target="_blank">https://www.biodiversity-science.net/CN/10.17520/biods.1997050</a><br/><br/>
        物种2000中国节点：<a href="http://www.sp2000.org.cn/" target="_blank">http://www.sp2000.org.cn/</a><br/><br/>
        中国动物主题数据库：<a href="http://www.zoology.csdb.cn/" target="_blank">http://www.zoology.csdb.cn/</a>
      </div>
	  </div>
        <div class="container">
      <h1 style="text-align: center;">联系我们</h1>
      <div class='internet'>
        <p @mouseover="yr" @mouseleave="yc" :style="active">地址：上海市闵行区吴泾镇东川路500号</p>
        <p @mouseover="yr" @mouseleave="yc" :style="active">邮箱1：kookil12020619@gmail.com</p>
        <p @mouseover="yr" @mouseleave="yc" :style="active">邮箱2：10193903417@stu.ecnu.edu.cn</p>
        <p @mouseover="yr" @mouseleave="yc" :style="active">邮箱3：2402732825@qq.com</p>
      </div>
	  </div>
  </div>
  
</template>

<script>
export default {
  name: "contact",
  data(){
    return{
      msg:'contact',
      active:''
    }
    
  },

  methods:{
    yr(){
      this.active="color:#006724"
    },
    yc(){
      this.active =''
    }
  }

}

</script>

<style scoped>
  html,
  body{
    margin: 0;
    padding: 0;
    height: 1830px;
    background-color: #EDE6DB;
  }

  #home{
    position: absolute;
    top: 65px;
    width: 100%;
    height: 81%;
    /* height: 1830px; */
  }

  .box{width: 800px;height: auto;margin: 0 auto;}
  .box ul{width: 800px;height: auto;margin: 0 auto;list-style-type: none;}
  .box ul li{width: 100%;height: auto;float: left;text-align: center;list-style-type: none;}
  .img_banner{
    position: absolute;
    left: 0;
    width: 100%;
    height: 550px;
  }

  
  .p{
    color: #1c1a17;
    line-height:10px;}

  .container{
    position: relative;
    width: 75%;
    height: 250px;
    background-color: #EDE6DB;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    text-align: left;
            top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
  }

  .internet{
    margin-left: 60px;
  }

  .container_righttext{
    position: absolute;
    top: 30%;
    left: 45%;
    width: 100%;
    text-align: left;
  }

  .img_rightedge{
    position: absolute;
    width: 100%;
  }

  .container_lefttext{
    position: absolute;
    left: 7%;
    top: 25%;
    width: 100%;
    text-align: left;
  }

  .font_highlight{
    color: rgb(68, 117, 68);
  }

  .bold{
    font-weight: bold;
  }

  .indent{
    text-indent: 2em;
  }
  
  .main_title{
    font-size: 64px;
    color: white;
    position:absolute;
    top:100px;
    left:20px;
    font-family:NSimSun;
    margin-left: 10px;
  }

  .sub_title{
    font-size: 32px;
    color: white;
    position:absolute;
    top:200px;
    left:20px;
    font-family:Microsoft YaHei;
    margin-left: 15px;
  }

  .text{
    font-size: 12px;
    color: white;
    position:absolute;
    top:300px;
    left:20px;
    font-family:Microsoft YaHei;
    margin-left: 25px;
    text-align: left;
  }

</style>
