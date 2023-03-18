<template>

  <div id="home">
    <div class="container">       
      <div id='blender'> </div>
      <!--<img :src="img_banner" class="img_banner" />-->
      <h1 class="main_title">
        濒危物种检索
      </h1>
      <h3 class="sub_title">
        &贸易角度的生物多样性保护
      </h3>
      <h4 class="text">
        <p>濒危物种的保护一直是人们关注的话题。立法、建立保护区、加强生态环境建设和生物多样性补偿等行政措施</p>
        <p>极大地改善了濒危物种的生存状况，但是，单靠政府的努力是远远不够的，还需要我们每个普通人从心底里萌</p>
        <p>发保护动物愿望和保护环境的观念，需要每个生产者严格规范日常的物料采集和生产行为。我们根据世界自然</p>
        <p>保护联盟（IUCN）的濒危物种红色名录，搜集濒危物种数据并搭建网站，提供了中国境内的濒危物种的基本信</p>
        <p>息和分布情况的查询服务，从而为濒危物种保护起到宣传和科普的作用。</p>
      </h4>
    </div>
    <!-- <div class="container">
      <div class="row">
        <div class="container_lefttext">
          <h2><span class='font_highlight bold'>濒危物种保护</span></h2><br/>
          <p class="bold indent">各省份濒危物种查询</p>
          <p class="indent">在交互式地图上点击省份，即可查询该省份的濒危物种清单</p><br />
          <p class="bold indent">濒危物种信息查询</p>
          <p class="indent">在控制栏点击某濒危物种，即可显示其具体信息，并在地图上展示该物种的分布范围</p>
        </div>
      </div>
	  </div>   -->          
    <!-- <p style="font-weight:bold;">濒危物种查询与各省份濒危物种清单查询</p>
          <p>在交互式地图上查询特定濒危物种的分布区域及具体信息，以及查询特定省份的濒危物种清单</p>
          <p style="font-weight:bold;">基于消费的濒危物种威胁路径可视化</p>
          <p>查看特定省份的本地最终产品及服务对中国各省份的濒危物种造成的威胁及其程度的流向图</p> -->
    <div class="container">
      <div class="row">
        <div class="container_leftimg">
          <ul>
          <li><img :src="img_search3" class="img_leftedge"/></li>
          <li><img :src="img_search3" class="img_leftedge"/></li>
          <li><img :src="img_search3" class="img_leftedge"/></li>
          </ul>
        </div>
        <br/>
        <div class="container_righttext">
          <br/><br/><br/>
          <h2><span class='font_highlight bold'>濒危物种</span>：查询服务</h2><br/>
          <p class="home_bold home_indent">各省份濒危物种查询</p>
          <p class="home_indent">在交互式地图上点击省份，即可查询该省份的濒危物种清单</p><br />
          <p class="home_bold home_indent">濒危物种信息查询</p>
          <p class="home_indent">在控制栏点击某濒危物种，即可显示其具体信息，并在地图上展示该物种的分布范围</p>
       <br/><br/>
          <h2><span class='font_highlight bold'>濒危物种</span>：可视化数据</h2><br/>
          <p class="home_bold home_indent">各省份濒危物种查询</p>
          <p class="home_indent">在交互式地图上点击省份，即可查询该省份的濒危物种清单</p><br />
          <p class="home_bold home_indent">濒危物种信息查询</p>
          <p class="home_indent">在控制栏点击某濒危物种，即可显示其具体信息，并在地图上展示该物种的分布范围</p>
          <p class="home_bold home_indent">濒危物种相关数据可视化</p>
          <p class="home_indent">目前提供四类相关数据的可视化</p>
        <br/><br/>
          <h2><span class='font_highlight bold'>濒危物种</span>：贸易影响</h2><br/>
          <p class="home_bold home_indent">贸易威胁计算</p>
          <p class="home_indent">检索省际贸易下各省市生产端的濒危物种威胁</p><br />
          </div>
      </div>
	  </div>
  <myfooter></myfooter>
  </div>
  
</template>

<script>
import Myfooter from '../components/Myfooter.vue'
import * as THREE from 'three'
import {Scene, PerspectiveCamera, WebGLRenderer, DirectionalLight,AmbientLight} from 'three';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader'                   
import {OrbitControls} from 'three/examples/jsm/controls/OrbitControls' 

/*export default {
  components: {Myfooter  },
  data(){
		return {
			totalbg: 2,
      img_banner: require('../assets/images/home/banner.jpg'),
      
		}
  },

  methods: {

  }
}*/
export default {
  name: 'Blender',
  components: {},
  data(){
    return{
        img_search1: require('../assets/images/home/home1.png'),
        img_search2: require('../assets/images/home/home2.png'),
        img_search3: require('../assets/images/home/home3.png'),
    }
    
  },
  mounted() {

    let scene = new Scene();

    let camera = new PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.set(0, 10, 50); 
    camera.lookAt(10, 50, 20); 
    camera.up.set(0, 1, 0); 
    let loader = new GLTFLoader();/*实例化加载器*/
    let renderer = new WebGLRenderer( {antialias: true,
        alpha: true});
    renderer.setSize(window.innerWidth, window.innerHeight);

    renderer.outputEncoding = THREE.sRGBEncoding

    let app = document.getElementById('blender')
    app.appendChild(renderer.domElement);
    //加载模型
    loader.load('models/forest1.gltf',function (obj) {

      obj.scene.position.y = 1;
      scene.add(obj.scene);

    },function (xhr) {

      console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );

    },function (error) {
      console.log('load error!'+error);

    });
    
    //加载场景控制插件
    let controls = new OrbitControls(camera,renderer.domElement);
    controls.enableDamping = true;
    controls.enableZoom = true;
    controls.autoRotate = false;
    controls.autoRotateSpeed = 3;
    controls.enablePan = true;
    controls.enableKeys = true;
    controls.keyPanSpeed = 7;
    controls.keys = {
      LEFT:37,
      UP:38,
      RIGHT:39,
      BOTTOM:40
    }
    this.controls =controls;
    //添加一个光源
    var point = new THREE.PointLight(0xffffff, 1) //光源设置
    point.position.set(200, 200, 100) //点光源位置
    scene.add(point) //将光源添加到场景中

    var point1 = new THREE.PointLight(0xffffff, 1) //光源设置
    point1.position.set(-200, -200, 100) //点光源位置
    scene.add(point1) //将光源添加到场景中

    var ambient = new THREE.AmbientLight(0xf8dfb7, 10) //环境光
    ambient.position.set(200, 300, 0) //点光源位置
    scene.add(ambient)

    var ambient1 = new THREE.AmbientLight(0xffffff, 10) //环境光
    ambient1.position.set(-200, -300, 0) //点光源位置
    scene.add(ambient1)

    var directionalLight = new THREE.DirectionalLight(0xffffff, 0.5) //方向光
    directionalLight.position.set(200, 200, 100)
    directionalLight.castShadow = true

    directionalLight.shadow.mapSize.height = 512 * 2
    directionalLight.shadow.mapSize.width = 512 * 2

    // 解决暗影
    // 0.00 <---> 0.05 最好的区间
    directionalLight.shadow.bias = 0.05 // 平面
    directionalLight.shadow.normalBias = 0.05 // 圆形表面，缩小受影响的网格，使其不会在自身上投射阴影

    scene.add(directionalLight)

    var directionalLight1 = new THREE.DirectionalLight(0xffffff, 1) //方向光
    directionalLight1.position.set(-200, -200, 100)
    scene.add(directionalLight1)

    var spotLight = new THREE.SpotLight(0xffffff, 1) //聚光灯
    spotLight.position.set(150, 200, 200)
    scene.add(spotLight)

    var hemisLight = new THREE.HemisphereLight( 0xffffff,0xffffff,1 );
    scene.add(hemisLight)

    camera.position.z = 5;

    
    //渲染场景
    let animate = function () {
      requestAnimationFrame(animate);

      renderer.render(scene, camera);
    };

    animate();

    
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

  .box{width: 800px;height: auto;margin: 0 auto;}
  .box ul{width: 800px;height: auto;margin: 0 auto;list-style-type: none;}
  .box ul li{width: 100%;height: auto;float: left;text-align: center;list-style-type: none;}
  .img_banner{
    position: absolute;
    left: 0;
    width: 100%;
    height: 550px;
  }

  .container{
    position: relative;
    width: 100%;
    height: 550px;
  }

  .blender{
    position: relative;
    width: 100%;
    height: 550px;
  }

  .container_leftimg{
    position: absolute;
    top: 35%;
    left: 7%;
    width: 25%;
    border: 3px, solid, red;
    display: flex;
  }

  .img_leftedge{
    position: relative;
    width: 75%;
  }

  .container_righttext{
    position: absolute;
    top: 30%;
    left: 45%;
    width: 55%;
    text-align: left;
  }

  .container_rightimg{
    position: absolute;
    top: 30%;
    left: 55%;
    width: 25%;
    border: 3px, solid, red;
    display: flex;
  }

  .img_rightedge{
    position: absolute;
    width: 120%;
  }

  .container_lefttext{
    position: absolute;
    left: 7%;
    top: 25%;
    width: 55%;
    text-align: left;
  }

  .font_highlight{
    color: rgb(68, 117, 68);
  }

  .home_bold{
    font-weight: bold;
  }

  .home_indent{
    text-indent: 2em;
  }

  .footer{
    position: relative;
    height: 75px;
    background-color: darkgray;
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
