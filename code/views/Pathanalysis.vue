<template>
  <div class="common-layout">
    <h1 class="route">什么是省际贸易对濒危物种威胁图</h1>
    <div class='route_p'><p class='route_pp'><br/>
      相关数据来自世界自然保护联盟（IUCN）的红色物种濒危名录。使用投入产出分析（MRIO）计算得到中国省际贸易对濒危物种的威胁，图中的绿色省份表示起点省份，起点省份的本地最终产品及服务对需求目的省份的濒危物种造成了威胁，其程度通过分级设色表示，颜色越深越严重。
    <br/>其中最终产品及服务需求既包括了生产端也包括了消费端，因此这里分别提供生产端和消费端对濒危物种的威胁。
    </p></div><br/><br/>
        <h1 class="route">为什么要做省际贸易对濒危物种威胁图</h1>
    <div class='route_p2'><p class='route_pp'><br/>
      人类的经济活动对环境造成了显著的影响，并因此导致严重的生物多样性损失。全球贸易和全球价值链分工导致了生产和消费在地理空间上的分离，经济活动所引起的环境破坏和生物多样性威胁因而有很大一部分通过经济全球化向其他地区转移。一个地区对产品和服务的最终需求，将潜在地推动其供给地的经济活动扩张，并通过环境破坏的驱动因素，例如土地类型及其利用方式的改变（Land Use and Land Cover Change，LUCC），最终导致本地区之外的生物多样性威胁。研究表明，全球大约30%的生物多样性威胁由全球贸易导致（Lenzen，2012）。研究地区间贸易活动对生物多样性保护具有重要意义。濒危物种面临的生物多样性威胁最为严重，其中关键物种更是对生态系统的构成和稳定至关重要。
    </p></div><br/><br/><br/><br/><br/>
    <el-container>
      <el-header>
        <el-dropdown>
  <span class="el-dropdown-link">
    <h3>省际贸易下某省生产端造成的濒危物种威胁</h3>
  请选择查询省份（西藏、香港、台湾、澳门的数据缺失）
   <el-icon class="el-icon--right">
   <arrow-down />
   </el-icon>
   </span>
   <template #dropdown>
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      text-color="#999"
      background-color="#e3e4e5"
    >
      <el-menu-item
        v-for="(mitem, mindex) in menuList"
        :key="mindex"
        :index="mitem.index"
      >
        <el-dropdown @command="onClick" v-if="mitem.menu">
          <span class="el-dropdown-link" v-text="mitem.menuItem">
            <i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-container v-for="(items, index) in mitem.menu" :key="index">
              <el-main>
                <el-dropdown-item
                  v-if="items.sortTitle"
                  v-text="items.sortTitle"
                  disabled
                  class="dropdown-sortTitle"
                >
                </el-dropdown-item>
                <el-dropdown-item
                  v-for="(a, aindex) in items.dropdownItem"
                  :key="aindex"
                  :command="a.title"
                  v-text="a.title"
                ></el-dropdown-item>
              </el-main>
            </el-container>
          </el-dropdown-menu>
        </el-dropdown>
        <span
          class="el-dropdown-link"
          v-text="mitem.menuItem"
          slot="title"
          v-else
          @click="onClick(mitem.url)"
        >
        </span>
      </el-menu-item>
    </el-menu></template>
   </el-dropdown>
      </el-header>
      <el-main>
        <iframe id='map' v-bind:src="iframeUrl" frameBorder="0" scrolling="no"></iframe>
      </el-main>
    </el-container>
        <el-container>
      <el-header>
        <el-dropdown>
  <span class="el-dropdown-link">
    <h3>省际贸易下某省消费端造成的濒危物种威胁</h3>
  请选择查询省份（西藏、香港、台湾、澳门的数据缺失）
   <el-icon class="el-icon--right">
   <arrow-down />
   </el-icon>
   </span>
   <template #dropdown>
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      text-color="#999"
      background-color="#e3e4e5"
    >
      <el-menu-item
        v-for="(mitem, mindex) in menuList"
        :key="mindex"
        :index="mitem.index"
      >
        <el-dropdown @command="onClick2" v-if="mitem.menu">
          <span class="el-dropdown-link" v-text="mitem.menuItem">
            <i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-container v-for="(items, index) in mitem.menu" :key="index">
              <el-main>
                <el-dropdown-item
                  v-if="items.sortTitle"
                  v-text="items.sortTitle"
                  disabled
                  class="dropdown-sortTitle"
                >
                </el-dropdown-item>
                <el-dropdown-item
                  v-for="(a, aindex) in items.dropdownItem"
                  :key="aindex"
                  :command="a.title"
                  v-text="a.title"
                ></el-dropdown-item>
              </el-main>
            </el-container>
          </el-dropdown-menu>
        </el-dropdown>
        <span
          class="el-dropdown-link"
          v-text="mitem.menuItem"
          slot="title"
          v-else
          @click="onClick(mitem.url)"
        >
        </span>
      </el-menu-item>
    </el-menu></template>
   </el-dropdown>
      </el-header>
      <el-main>
        <iframe id='map' v-bind:src="iframeUrl2" frameBorder="0" scrolling="no"></iframe>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import scrollReveal from 'scrollreveal';
export default {
  name: "Pathanalysis",

  data() {
    return {
            activeIndex: "1",
      menuList: [
        {
          index: "1",
          menuItem: "查询",
          menu: [
            {
              sortTitle: "列1",
              dropdownItem: [
                { title: "北京", link: "/alert" },
                { title: "天津", link: "/alert" },
                { title: "河北", link: "/alert" },
                { title: "山西", link: "/alert" },
                { title: "内蒙古", link: "/alert" },
                { title: "辽宁", link: "/alert" },
                { title: "吉林", link: "/alert" },
                { title: "黑龙江", link: "/alert" },
              ],
            },
            {
              sortTitle: "列2",
              dropdownItem: [
                { title: "上海", link: "/alert" },
                { title: "江苏", link: "/alert" },
                { title: "浙江", link: "/alert" },
                { title: "安徽", link: "/alert" },
                { title: "福建", link: "/alert" },
                { title: "江西", link: "/alert" },
                { title: "山东", link: "/alert" },
                { title: "河南", link: "/alert" },
              ],
            },
            {
              sortTitle: "列3",
              dropdownItem: [
                { title: "湖北", link: "/alert" },
                { title: "湖南", link: "/alert" },
                { title: "广东", link: "/alert" },
                { title: "广西", link: "/alert" },
                { title: "海南", link: "/alert" },
                { title: "重庆", link: "/alert" },
                { title: "四川", link: "/alert" },
                { title: "贵州", link: "/alert" },
              ],
            },

            {
              sortTitle: "列4",
              dropdownItem: [
                { title: "云南", link: "/alert" },
                { title: "陕西", link: "/alert" },
                { title: "甘肃", link: "/alert" },
                { title: "青海", link: "/alert" },
                { title: "宁夏", link: "/alert" },
                { title: "新疆", link: "/alert" },
              ],
            },
            ],
            },],
                

      scrollReveal:scrollReveal(),
      iframeUrl: "map/北京的经济需求威胁到的各省的濒危物种个数.html",
      iframeUrl2: "map2/各省份由北京的最终产品和服务需求驱动的濒危物种威胁.html",
    };
  },

  mounted() {

  },

  methods: {
    onClick(command){
       this.iframeUrl=("map/"+command+"的经济需求威胁到的各省的濒危物种个数.html");
    },
    onClick2(command){
       this.iframeUrl2=("map2/各省份由"+command+"的最终产品和服务需求驱动的濒危物种威胁.html");
    },
    
  },
};
</script>

<style scoped>
html,body,#app{ height:100%; margin: 0px; padding: 0px; }

#pathanalysis,
#map {
  margin: 10px;
  padding: 0;
}


#map {
  background-color: #ffffff;
  overflow: hidden;
  border: hidden;
  width:60%;
  height:550px;
}

.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}

.route_p{
      position: relative;
    width: 70%;
    height: 125px;
    background-color: #EDE6DB;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    text-align: left;
            top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
}

.route_pp{
  margin-top:50px;
  margin-left:50px;
  margin-right:50px;
}

.route_p2{
        position: relative;
    width: 70%;
    height: 160px;
    background-color: #EDE6DB;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    text-align: left;
            top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
}

.el-dropdown-link {
  color: rgb(26, 25, 25);
}
.el-dropdown-menu > .el-container {
  width: 170px;
  float: left;
}
.dropdown-sortTitle {
  font-weight: 700;
  color: #666 !important;
  border-bottom: 1px solid #ececec;
}
</style>