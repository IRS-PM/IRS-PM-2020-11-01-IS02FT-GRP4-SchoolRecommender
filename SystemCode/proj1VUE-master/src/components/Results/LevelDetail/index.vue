<template>
  <div class="main2" @click="changePanel">
    <div v-for="(item,idx) in detailLevels" :key="idx">
      <div class="detail_level_score">
        <div class="score" :style="{background:item.score_color, width:item.score+'px'}"></div>
        <span class="level" :style="{color:item.color}">{{item.level}}</span>
        <span class="title">{{item.name}}</span>
      </div>
    </div>
  </div>
</template>

<script>
import {getEvaluateLevel, getLevelDetail} from "../../../axios/axios-api";

export default {
  name: "levelDetail",

  data() {
    return {
      detailLevels: [
        {
          name: "GRADUATION SCHOOL",
          level: "",
          color: "#1c1c67",
          score: "",
          score_color: "#1c1c67"
        },
        {
          name: "GPA",
          level: "",
          color: "#fec557",
          score: "",
          score_color: "#fec557"
        },
        {
          name: "TOFEL/IELTS",
          level: "",
          color: "#fe7f08",
          score: "",
          score_color: "#fe7f08"
        },
        {
          name: "ENTRANCE TEST",
          level: "",
          color: "#f0d4ca",
          score: "",
          score_color: "#f0d4ca"
        },
        {
          name: "OTHER",
          level: "",
          color: "#13c0ae",
          score: "",
          score_color: "#13c0ae"
        }
      ],
      scoremap:{
        S:'160',
        A:'130',
        B:'100',
        C:'70',
        D:'90'
      }
    };
  },
  methods: {
    changePanel() {
      this.$emit("changePanel_child", true);
    },

    getlevelDetail(){
      
      let res = getLevelDetail();
      res
        .then(res => {
          this.detailLevels[0].level= res.result.graduate_school;
          this.detailLevels[1].level= res.result.GPA;
          this.detailLevels[2].level= res.result.language;
          this.detailLevels[3].level= res.result.entrance_test;
          this.detailLevels[4].level= res.result.other;
          this.detailLevels[0].score= this.scoremap[res.result.graduate_school];
          this.detailLevels[1].score= this.scoremap[res.result.GPA];
          this.detailLevels[2].score= this.scoremap[res.result.language];
          this.detailLevels[3].score= this.scoremap[res.result.entrance_test];
          this.detailLevels[4].score= this.scoremap[res.result.other];

          


        })
    }
  },
};
</script>

<style>
.main2 {
  width: 375px;
  height: 200px;
  padding: 10px;
}
.detail_level_score {
  display: flex;
  height: 10px;
  margin-bottom: 30px;
  margin-left: 20px;
  width: 160px;
  background: #bfbec0;
  border-width: 0px;
  border-style: solid;
  border-radius: 28px;
  border-color: #000 #000 #000 #000;
  justify-content: space-between;
}
.detail_level_score .score {
  border-width: 0px;
  border-style: solid;
  border-radius: 28px;
  border-color: #000 #000 #000 #000;
  justify-content: space-between;
}
.detail_level_score span.level {
  margin-left: 280px;
  height: 20px;
  width: 50px;
  font-size: 15px;
  font-family: "Gill Sans";
  font-weight: 500;
  position: absolute;
}
.detail_level_score span.title {
  margin-left: 180px;
  height: 10px;
  width: 50px;
  font-size: 10px;
  font-family: "Helvetica Neue";
  font-weight: 500;
  color: darkgrey;
  position: absolute;
}

.detaillevel {
  display: flex;
  height: 10px;
  margin-top: 20px;
  margin-left: 20px;

}
</style>
