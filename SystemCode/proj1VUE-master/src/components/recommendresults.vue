<template>
  <div style="width: 375px; height: 300px">
    <div class="report_title">Recommand&nbsp;Report</div>
    <result v-show="showMainPanel" 
    @changePanel_child="changePanel"
    ref="cresult"
    ></result>
    <levelDetail
      v-show="!showMainPanel"
      @changePanel_child="changePanel"
      ref="cleveldetail"
    ></levelDetail>
    <!-- </div> -->
    <div style="width: 375px; height: 40px">
      <span class="title2">The Best School for You</span>
    </div>
    <div class="main" v-if="schoolList.length > 0">
      <div v-for="(item, idx) in schoolList" :key="idx">
        <div class="cell2" @click="toSchoolDetail(item.school)">
          <div class="leftcell">
            <span class="a">{{ item.school }}</span>
            <span class="b">{{ item.major }}</span>
            <span class="c">{{ item.location }}</span>
          </div>
          <div class="rightcell">
            <img :src="nexticon" alt />
            <div class="score" :style="{ background: item.color }">
              {{ item.score }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="emptyList" v-else>
      <img :src="emptyList" alt />
    </div>
  </div>
</template>

<script>
import result from "components/Results/Result";
import levelDetail from "components/Results/LevelDetail/";
import { getRecommendSchool, putUsersInfo } from "../axios/axios-api";

export default {
  components: {
    result,
    levelDetail,
  },
  name: "results",
  data() {
    return {
      showMainPanel: true,
      rotate_left: 0, //left circle rotate degree
      rotate_right: 0, //right circle rotate degree
      exceed_percent: 50,
      evaluation_level: "A",
      schoolList: [],
      emptyList: require("../images/emptyList.png"),
      nexticon: require("../images/next.png"),
    };
  },
  methods: {
    changePanel(data) {
      this.showMainPanel = data;
    },
    getleveldetail(){

    },
    toSchoolDetail(school) {
      this.$router.push({
        path: "/schoolDetail",
        query: {
          school_name: school,
        },
      });
    },

    getrecommendSchool() {
      let locations = {
        locations: this.$route.query.locations,
      };
      let res = getRecommendSchool(locations);

      res.then((res) => {
        for (var i = 0, len = res.result.length; i < len; i++) {
          if (Number(res.result[i].score) >= 80) {
            res.result[i]["color"] = "#22c278";
          } else if (Number(res.result[i].score) >= 60) {
            res.result[i]["color"] = "#f2af00";
          } else {
            res.result[i]["color"] = "#fd312f";
          }
          console.log(res.result[i]);
          this.schoolList.push(res.result[i]);
        }
      });
    },

    putusersInfo() {
      // pass all data the user typed in the back end
      var locations = this.$route.query.locations;
      var school = parseInt(this.$route.query.school);
      var major = parseInt(this.$route.query.major);
      var language = this.$route.query.language;
      var language_score = parseFloat(this.$route.query.language_score);
      var GPA_scale = parseFloat(this.$route.query.GPA_scale);
      var GPA_rank = parseFloat(this.$route.query.GPA_rank);
      var entrance = this.$route.query.entrance;
      var entrance_score = parseFloat(this.$route.query.entrance_score);

      var working_experience = this.$route.query.working_experience;
      var research_experience = this.$route.query.research_experience;
      var internship = this.$route.query.internship;
      var scholarship = this.$route.query.scholarship;
      var exchange = this.$route.query.exchange;
      var competition = this.$route.query.competition;

      // let param = {
      //   Country: ["America","Britain"],//locations,
      //   school: 2, //school,
      //   major: 4,//major,
      //   language_type : "TOEFL",//language,
      //   language_score: 100,//language_score,
      //   gpa_scale: 5,//GPA_scale,
      //   gpa_score: 5,//GPA_rank,
      //   entrance: "GMAT",//entrance,
      //   entrance_score: 325,//entrance_score,
      //   work: working_experience,
      //   paper: research_experience,
      //   intern: internship,
      //   scholarship: scholarship,
      //   exchange: exchange,
      //   competition: competition
      // }

      let param = {
        Country: locations,
        school: school,
        major: major,
        language_type: language,
        language_score: language_score,
        gpa_scale: GPA_scale,
        gpa_score: GPA_rank,
        entrance: entrance,
        entrance_score: entrance_score,
        work: working_experience,
        paper: research_experience,
        intern: internship,
        scholarship: scholarship,
        exchange: exchange,
        competition: competition,
      };
      let res = putUsersInfo(param);
      console.log("putuserinfo finished!!",res.msg);
      res.then((res)=>{
        this.getrecommendSchool();
        this.$refs.cresult.getevaluateLevel();
        this.$refs.cleveldetail.getlevelDetail();

      })
    },
  },
  created() {
    this.putusersInfo();
    // call this method when creating this page
  },
};
</script>

<style>
.scoreboard {
  display: inline-block;
  padding: 20px;
  position: absolute;
  height: 130px;
  width: 130px;
  margin-top: 20px;
  background: #f7f7fd;
  border-width: 0px;
  border-style: solid;
  border-radius: 28px;
  border-color: #000 #000 #000 #000;
  box-shadow: 0 0 60px 10px #e3e2ea;
  line-height: 20px;
  text-align: center;
}
.scoreboard span.a {
  display: block;
  font-size: 20px;
  font-family: "Gill Sans";
  font-weight: 600;
  color: #3d3c3d;
}
.scoreboard span.b {
  line-height: 50px;
  font-size: 35px;
  font-family: "Gill Sans";
  font-weight: 600;
  color: #232223;
}
.report_title {
  display: block;
  margin-top: 30px;
  margin-left: 20px;
  height: 40px;
  width: 375px;
  font-size: 25px;
  font-family: "Helvetica Neue";
  font-weight: 500;
  color: #232223;
}
.title2 {
  position: absolute;
  margin-left: 20px;
  height: 0.7rem;
  width: 300px;
  font-size: 18px;
  font-family: "Gill Sans";
  font-weight: 700;
  color: #1c1d66;
}
.loading2 {
  margin-left: 25px;
  margin-right: 50px;
  margin-top: 20px;
  width: 130px;
  height: 130px;
  position: relative;
}
.clock {
  position: relative;
  width: 130px;
  height: 130px;
  display: inline-block;
}
.loading2 .progress {
  position: absolute;
  width: 120px;
  height: 120px;
  background-color: white;
  border-radius: 50%;
  left: 5px;
  top: 5px;
  line-height: 30px;
  text-align: center;
  padding: 25px;
}
.progress span.a {
  font-size: 35px;
  margin-right: 1px;
  font-family: "Gill Sans";
  font-weight: 400;
  color: #f97050;
}
.progress span.b {
  display: block;
  font-size: 15px;
  font-family: "Gill Sans";
  font-weight: 100;
}
.progress span.c {
  font-size: 15px;
  font-family: "Gill Sans";
  font-weight: 400;
  color: #f97050;
}
.left,
.right {
  width: 65px;
  height: 130px;
  overflow: hidden;
  position: relative;
  float: left;
  background: #ebebeb;
}
.left {
  border-radius: 130px 0 0 130px;
}
.right {
  border-radius: 0 130px 130px 0;
}
.left div,
.right div {
  content: "";
  position: absolute;
  display: block;
  width: 65px;
  height: 130px;
  background-color: white;
  border-radius: 130px 0 0 130px;
  transition: all 0.1s;
  transform-origin: right center;
  transform: rotateZ(-180deg);
}
.right div {
  content: "";
  position: absolute;
  display: block;
  border-radius: 0 130px 130px 0;
  transform-origin: left center;
}
.clock:nth-child(1) .left div,
.clock:nth-child(1) .right div {
  background-color: #fc4b3e;
}
.main {
  height: 500px;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 10px;
}
.cell2 {
  display: flex;
  height: 120px;
  width: 340px;
  margin-top: 40px;
  background: #f7f7fd;
  border-width: 0px;
  border-style: solid;
  border-radius: 28px;
  border-color: #000 #000 #000 #000;
  box-shadow: 0 0 30px 10px #e3e2ea;
  justify-content: space-between;
  padding: 20px;
}
.cell2 .leftcell {
  position: flex;
  height: 80px;
  width: 240px;
}
.leftcell span.a {
  display: block;
  line-height: 18px;
  font-size: 15px;
  font-family: "Helvetica Neue";
  font-weight: 500;
  color: #232223;
}
.leftcell span.b {
  display: block;
  line-height: 18px;
  font-size: 14px;
  font-family: "Helvetica Neue";
  font-weight: 200;
  color: #232223;
}
.leftcell span.c {
  font-size: 14px;
  font-family: "Helvetica Neue";
  font-weight: 300;
  color: #807f7f;
  display: block;
  top: 2px;
  position: relative;
}
.cell2 .rightcell {
  width: 100px;
  height: 20px;
}
.rightcell img {
  margin-left: 50px;
  margin-top: 20px;
  width: 20px;
  height: 20px;
}
.cell2 .score {
  display: block;
  height: 40px;
  width: 100px;
  margin-top: 10px;
  border-width: 0px;
  border-style: solid;
  border-radius: 30px;
  border-color: #000 #000 #000 #000;
  font-size: 25px;
  font-family: "Gill Sans";
  font-weight: 500;
  color: #f7f7fd;
  text-align: center;
  padding-top: 5px;
}
</style>
