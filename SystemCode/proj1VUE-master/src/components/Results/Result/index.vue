<template>
  <div style="width:375px;height:200px;">
    <div class="loading" style="display:inline-block;">
      <div class="clock seconds">
        <div class="left">
          <div :style="{transform: 'rotateZ('+rotate_left+'deg)'}"></div>
        </div>
        <div class="right">
          <div :style="{transform: 'rotateZ('+rotate_right+'deg)'}"></div>
        </div>
        <div class="progress">
          <span class="b">Exceed</span>
          <span class="a">{{exceed_percent}}</span>
          <span class="c">%</span>
        </div>
      </div>
    </div>
    <div class="scoreboard" @click="changePanel">
      <span class="a">Evaluation Level</span>
      <span class="b">{{evaluation_level}}</span>
    </div>
  </div>
</template>

<script>
import {getEvaluateLevel} from "../../../axios/axios-api";

export default {
  name: "result",

  data() {
    return {
      rotate_left: 0, //left circle rotate degree
      rotate_right: 0, //right circle rotate degree
      exceed_percent: 70,
      evaluation_level: "A",
      emptyList: require("../../../images/emptyList.png"),
      nexticon: require("../../../images/next.png")
    };
  },
  props: ["broker_id_prop", "robot_id_prop", "token_prop", "visitimgurl"],
  mounted() {
    
  },
  methods: {
    changePanel() {
      this.$emit("changePanel_child", false);
    },
    rotationAngles() {
        if (this.exceed_percent<=50){
            this.rotate_left=180;
            this.rotate_right = (this.exceed_percent-50)/50*180;
        }
        else{
            this.rotate_right = 0;
            this.rotate_left = (this.exceed_percent-100)/50*180;
        }

    },

    getevaluateLevel(){
      let res = getEvaluateLevel();
      res
        .then(res => {
          this.exceed_percent = res.result.exceed_percent;
          this.evaluation_level = res.result.evaluation_level;
          this.rotationAngles();


        })
    }
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
.loading {
  /* margin: 100px auto; */
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
.loading .progress {
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
</style>
