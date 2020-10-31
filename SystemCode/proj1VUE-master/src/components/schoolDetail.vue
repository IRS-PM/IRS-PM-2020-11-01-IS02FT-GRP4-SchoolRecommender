<template>
  <div class="detail_header">
    <div style="width:375px;height:120px;text-align:center">
      <span class="schoolname">{{this.school_name}}</span>
    </div>
    <div style="width:375px;height:100px;text-align:center">
      <img :src="school_icon" style="height:70px;margin-top:70px" />
    </div>
    <div style="width:375px;height:200px;margin-top:80px;text-align:center">
      <span class="title3">World’s best University Ranking</span>
      <div class="detailCell" style="height:200px">
        <div class="rankcell">
          <!-- <img :src="rank_icon" style="width:100px;height:150px;position:absolute;" /> -->
          <p class="rankfont" style="margin-top:40px;z-index:10">{{qs_rank}}</p>
          <p class="ranktitle" style="margin-top:30px">QS</p>
        </div>
        <div class="rankcell">
          <!-- <img :src="rank_icon" style="width:100px;height:150px;position:absolute;" /> -->
          <p class="rankfont" style="margin-top:40px;">{{times_rank}}</p>
          <p class="ranktitle" style="margin-top:30px;">TIMES</p>
        </div>
        <div class="rankcell">
          <!-- <img :src="rank_icon" style="width:100px;height:150px;position:absolute;" /> -->
          <p class="rankfont" style="margin-top:40px;">{{usnews_rank}}</p>
          <p class="ranktitle" style="margin-top:30px;">USNEWS</p>
        </div>
      </div>
    </div>
    <div style="width:375px;height:150px;margin-top:80px;text-align:center">
      <span class="title3">For More Info</span>
      <div class="detailCell" style="height:140px">
        <img
          :src="wiki_icon"
          style="width:100px;height:100px;display:inline-block"
          @click="jumpto(wiki_link)"
        />
        <img
          :src="homepage_icon"
          style="width:100px;height:100px;display:inline-block"
          @click="jumpto(homepage)"
        />
        <img
          :src="google_icon"
          style="width:100px;height:100px;display:inline-block"
          @click="jumpto(google_link)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import {getSchoolDetail} from "../axios/axios-api";

export default {
  name: "result",

  data() {
    return {
      school_id: this.$route.query.school_id,
      school_name: "",
      school_icon: require("../images/nus_icon.png"),
      rank_icon: require("../images/rank.png"),
      homepage_icon: require("../images/homepage.png"),
      wiki_icon: require("../images/wiki.png"),
      google_icon: require("../images/google.png"),
      qs_rank: 0,
      times_rank: 0,
      usnews_rank: 0,
      wiki_link:
        "https://en.wikipedia.org/wiki/National_University_of_Singapore",
      google_link:
        "https://www.google.com/search?q=national+university+of+singapore",
      homepage: ""
    };
  },
  methods: {
    jumpto(url) {
      console.log(url);
      window.location.href = url;
    },
   
    getschooldetail() {
      let param = {
        school_name: this.$route.query.school_name
      };
      console.log(JSON.stringify(param))
      let res = getSchoolDetail(param);
      res
        .then(res => {
          this.school_name = res.result.school_name;
          this.school_icon = res.result.icon;
          this.qs_rank = res.result.qsrank;
          this.times_rank = res.result.timesrank;
          this.usnews_rank = res.result.usnewsrank;
          this.homepage = res.result.homepage;
          if (!this.homepage.startsWith("http")){
           this.homepage = "https://"+this.homepage};
          console.log(this.homepage)
          this.wiki_link = "https://en.wikipedia.org/wiki/"+res.result.school_name;
          this.google_link = "https://www.google.com/search?q="+res.result.school_name;
        })
        .catch(reslove => {
          console.log("get School Detail Error");
        });
    }
  },
  mounted() {},
  created() {
    this.getschooldetail();
  }
};

</script>

<style>
.detail_header {
  height: 150px;
  width: 375px;
  background: #4c4ce7;
  border-width: 0px;
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 60px;
  border-bottom-left-radius: 60px;
  border-color: #000 #000 #000 #000;
}

.detail_header .schoolname {
  display: block;
  width: 300px;
  padding-top: 50px;
  padding-left: 70px;
  color: #f7f7fd;
  font-family: "Gill Sans";
  font-size: 20pt;
  font-weight: 400;
  word-wrap: break-word;
}
.title3 {
  /* margin-left: 30px; */
  height: 0.7rem;
  width: 300px;
  font-size: 18px;
  font-family: "Gill Sans";
  font-weight: 700;
  color: #3d3c3d;
}
.detailCell {
  display: flex;
  height: 200px;
  width: 340px;
  margin-top: 20px;
  margin-left: 18px;

  background: #f7f7fd;
  border-width: 0px;
  border-style: solid;
  border-radius: 28px;
  border-color: #000 #000 #000 #000;
  box-shadow: 0 0 30px 10px #e3e2ea;
  justify-content: space-between;
  padding: 20px;
}
.detailCell .rankfont {
  font-size: 32px;
  font-family: "Gill Sans";
  font-weight: 700;
  color: #232223;
  z-index:2;


}
.detailCell .ranktitle {
  font-size: 18px;
  font-family: "Gill Sans";
  font-weight: 400;
  color: #232223;
  z-index:2;
}
.detailCell .rankcell
{
width:100px;
height:150px;
display:inline-block;
background: url(../images/rank.png) no-repeat;
background-size: 100px 150px;
}
</style>
