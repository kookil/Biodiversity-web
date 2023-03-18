<template>
  <div id="services">
    <div id="lmap"></div>
    <console ref="console" @console_query_name="getConsoleQueryName"></console>
    <specieslist v-if="showspecieslist" id="specieslist" :species_list_data='specieslist_passdata'></specieslist>
    <speciesinfo v-if="!showspecieslist" id="speciesinfo" :species_info_data='speciesinfo_passdata'></speciesinfo>
  </div>
</template>

<script>
import 'leaflet/dist/leaflet.css'
import  $L, { geoJSON } from 'leaflet'
import Console from '../components/Console.vue'
import Specieslist from '../components/Specieslist.vue'
import Speciesinfo from '../components/Speciesinfo.vue'

export default {
  name: 'Services',
  components:{
    Specieslist,
    Speciesinfo,
    Console,    
  },

  data(){
    Speciesinfo
    return {
      map: null,
      lastovergeom: null,
      lastclickgeom: null,
      specieslist_passdata: null,
      speciesinfo_passdata: {
        'photo': 'No Image.png',
        'info': ''
      },
      console_query_name: '',
      geojsonlayer: null,
      showspecieslist: true,
      defaultSpeciesStyle: {
        color: (0,0,0),
        fillColor: '#ff5809',
        fillOpacity: 0.8,          
      },
      defaultProvinceStyle: {
        color: '#000000',
        opacity: 0.3,
        fillColor: '#ffffff',
        fillOpacity: 0.8, 
      },
      overProvinceStyle: {
        color: '#ffffff',
        opacity: 0.3,
        fillColor: '#696969',
        fillOpacity: 0.8, 
      },
      focusProvinceStyle: {
        color: '#000000',
        opacity: 1,
        fillColor: '#ff8000',
        fillOpacity: 0.8, 
      },
      name_dict: {
        '新疆维吾尔自治区': 'Xinjiang',
        '甘肃省': 'Gansu',
        '青海省': 'Qinghai',
        '四川省': 'Sichuan',
        '内蒙古自治区': 'Neimenggu',
        '宁夏回族自治区': 'Ningxia',
        '云南省': 'Yunnan',
        '贵州省': 'Guizhou',
        '重庆市': 'Chongqing',
        '广西壮族自治区': 'Guangxi',
        '海南省': 'Hainan',
        '广东省': 'Guangdong',
        '湖南省': 'Hunan',
        '江西省': 'Jiangxi',
        '福建省': 'Fujian',
        '浙江省': 'Zhejiang',
        '江苏省': 'Jiangsu',
        '安徽省': 'Anhui',
        '上海市': 'Shanghai',
        '湖北省': 'Hubei',
        '河南省': 'Henan',
        '山西省': 'Shanxi',
        '山东省': 'Shandong',
        '河北省': 'Hebei',
        '北京市': 'Beijing',
        '天津市': 'Tianjin',
        '辽宁省': 'Liaoning',
        '吉林省': 'Jilin',
        '陕西省': 'Shaanxi',
        '黑龙江省': 'Heilongjiang'
      },
    }
  },

  created() {

  },

  mounted() {
    this.initmap()
  },

  methods:{
    highlightFeature: function(e){
      if (this.lastovergeom !== null){
        this.lastovergeom.setStyle(this.defaultProvinceStyle)
      }
      let geom = e.target
      if (geom == this.lastclickgeom){
        this.lastovergeom = null
        return
      }
      geom.setStyle(this.overProvinceStyle)
      geom.bringToFront()
      this.lastovergeom = geom
    },

    focusFeature: function(e){
      if (this.lastovergeom !== null){
        this.lastovergeom.setStyle(this.defaultProvinceStyle)
        this.lastovergeom = null
      }
      if (this.lastclickgeom !== null){
        this.lastclickgeom.setStyle(this.defaultProvinceStyle)
      }
      let geom = e.target
      geom.setStyle(this.focusProvinceStyle)
      geom.bringToFront()
      this.lastclickgeom = geom
    },

    queryProvinceList: async function(e){
      this.focusFeature(e)
      let province_name = e.target.feature.properties.name
      if (!this.name_dict.hasOwnProperty(province_name)){
        this.specieslist_passdata = null
        return
      }
      province_name = this.name_dict[province_name]
      let params = new URLSearchParams()
      params.append('province', province_name)
      const res = await this.$http.post('/query_provincial_list', params)
      if (res.data == 'error') return 'error'
      this.specieslist_passdata = res.data.data
      this.resetElements2List()
    },

    onEachFeature(feature, layer) {
      layer.on({
        mouseover: this.highlightFeature,
        click: this.queryProvinceList,
      })
    },

    initmap() {
      this.map = $L.map("lmap", {
        // center: [37.5, 105], 
        center: [37.5, 97.5], 
        zoom: 4, 
        zoomControl: false, 
        doubleClickZoom: false,
        attributionControl: false 
      });

      //EPSG: 3857
      let mapboxLayer = $L.tileLayer('https://api.mapbox.com/styles/v1/rosmontis/ckrsit0tv37dz17mxjon2vrm7/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoicm9zbW9udGlzIiwiYSI6ImNrbHp4ZDZnYTNvN3Eyb3Ftc2IycjM2c3UifQ.ko5Ak2Nopz5oyTPEAltt-g', {
        minZoom: 3,
        maxZoom: 8,            
      }).addTo(this.map);

      let chinesejson = require('../assets/geojson/Chinese.json')
      let chineseLayer = $L.geoJSON(chinesejson, { 
        style: {
          color: '#000000',
          opacity: 0.3,
          fillColor: '#ffffff',
          fillOpacity: 0.8,          
        },
        onEachFeature: this.onEachFeature
      }).addTo(this.map);
    },

    query_region: async function(species_name){
      let params = new URLSearchParams()
      params.append('species_name', species_name)
      const res = await this.$http.post('/query_region', params)
      if (res.data == 'failed'){
        alert('暂无分布数据!')
        this.map.removeLayer(this.geojsonlayer)
        this.geojsonlayer = null
        return
      }
      this.loadjson(res.data.data)
    },    

    loadjson(geojson) {
      // let geojson = require('../assets/geojson/' + species_name + '.json')
      // let geojson = require('../assets/geojson/test.json')
      if (this.geojsonlayer !== null){
        this.map.removeLayer(this.geojsonlayer)
      }
      this.geojsonlayer = $L.geoJSON(geojson, {style: this.defaultSpeciesStyle}).setZIndex(999);
      this.geojsonlayer.addTo(this.map)
    },

    get_species_info_data: async function(species_name){
      let params = new URLSearchParams()
      params.append('species_name', species_name)
      const res = await this.$http.post('/query_species_info_data', params)
      this.speciesinfo_passdata = {
        'photo': res.data.data.photo,
        'info': res.data.data.info
      }
      return
    },   

    resetElements2Info: function(){
      this.showspecieslist = false
      if (this.lastovergeom !== null){
        this.lastovergeom.setStyle(this.defaultProvinceStyle)
        this.lastovergeom = null
      }      
      if (this.lastclickgeom !== null){
        this.lastclickgeom.setStyle(this.defaultProvinceStyle)
        this.lastclickgeom = null
      }
    },

    resetElements2List: function(){
      if (this.geojsonlayer !== null){
        this.map.removeLayer(this.geojsonlayer)
        this.geojsonlayer = null
      }      
      this.speciesinfo_passdata = {
        'photo': 'No Image.png',
        'info': ''
      },
      this.showspecieslist = true
    },

    getConsoleQueryName: function(msg){
      this.console_query_name = msg
      this.resetElements2Info()
      this.query_region(this.console_query_name)
      this.speciesinfo_passdata = this.get_species_info_data(this.console_query_name)
    }
  }
};
</script>

<style scoped>
html,
body,
#services{
  margin: 0;
  padding: 0;
}

#lmap{
  position: absolute;
  top: 65px;
  left: 0;
  width: 76.5%;
  height: 89%;
  z-index: 1;
}

#specieslist{
  position: absolute;
  top: 65px;
  left: 76.5%;
  height: 89%;
  overflow-y: scroll;
}

#speciesinfo{
  position: absolute;
  top: 65px;
  left: 76.5%;
  height: 89%;
  overflow-y: scroll;
}

img{
  width: 252px;
}

</style>