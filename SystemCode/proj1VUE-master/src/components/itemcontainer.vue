<template>
  <section>
    <div v-if="fatherComponent == 'home'">
      <div class="roundedRectangle">
        <p class="hometitle">SCHOOL&nbsp;RECOMMENDER</p>
        <div class="item_container_style" align="center">
          <img src="../images/home-1.png" class="home_logo" />
        </div>
      </div>
      <div class="namelist">
        <ul>
          <li>
            A0215516L&nbsp;&nbsp;Cao&nbsp;Wen
            <div class="dotline"></div>
          </li>
          <li>
            A0215403W&nbsp;&nbsp;Lin&nbsp;Xi
            <div class="dotline"></div>
          </li>
          <li>
            A0215461M&nbsp;&nbsp;Liu&nbsp;ChenXi
            <div class="dotline"></div>
          </li>
          <li>A020215414R&nbsp;&nbsp;Zheng&nbsp;Kai</li>
        </ul>
      </div>
      <div class="button" @click="start">START</div>

      <!-- <router-link to="item" class="start button_style" ></router-link> -->
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  components: {
  },
  name: "itemcontainer",
  data() {
    return {
      isstart: false //start question
    };
  },
  props: ["fatherComponent"],
  methods: {
    start(){
      this.$router.push({
        name: "country",
        query: {
        }
      });
    }
    
  },
  created() {
    //初始化信息
    if (this.fatherComponent == "home") {
      // this.initializeData();
      // document.body.style.backgroundImage = 'url(./static/img/1-1.jpg)';
    }
  }
};
</script>

<style lang="less">
.top_tips {
  position: absolute;
  height: 7.35rem;
  width: 3.25rem;
  top: -1.3rem;
  right: 1.6rem;
  // background: url(../images/WechatIMG2.png) no-repeat;
  // background-size: 100% 100%;
  z-index: 10;
  .num_tip {
    position: absolute;
    left: 0.48rem;
    bottom: 1.1rem;
    height: 0.7rem;
    width: 2.5rem;
    font-size: 0.6rem;
    font-family: "黑体";
    font-weight: 600;
    color: #a57c50;
    text-align: center;
  }
}
.hometitle {
  text-align: center;
  // position: absolute;
  margin-top: 0px;
  height: 0.7rem;
  // width: 2.5rem;
  font-size: 28px;
  font-family: "Gill Sans" ;
  font-weight: 400;
  color: #f7f7fd;
}

.roundedRectangle {
  width:375px;
  height: 250px;
  // width: 100px;
  margin-top: 0px;
  background: #4c4ce7; //背景色
  border-width: 0px; //边缘的宽度，如果要分别设置可以这样：border-width: 15px 5px 15px 5px;依次为上、右、下、左
  border-style: solid;
  //   border-radius: 15px; //圆角的大小
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 45px;
  border-bottom-left-radius: 45px;
  border-color: #000 #000 #000 #000; //边框颜色，依次为上、右、下、左
}

.roundedRectangle p {
  margin: 0px;
  padding-top: 100px;
  text-align: center;
  //   font-size: 20px;
  //   letter-spacing: 8px;
}
.namelist {
  height: 210px;
  width: 335px;
  margin-left:20px ;
  margin-top: 200px;

  background: #f7f7fd; //背景色
  border-width: 0px; //边缘的宽度，如果要分别设置可以这样：border-width: 15px 5px 15px 5px;依次为上、右、下、左
  border-style: solid;
  border-radius: 28px; //圆角的大小
  border-color: #000 #000 #000 #000; //边框颜色，依次为上、右、下、左
  box-shadow: 0 0 30px 20px #e3e2ea;
}
.namelist ul {
  > li {
    text-align: center;
    height: 10px;
    font-size: 20px;
    font-family: "Gill Sans" !important;
    font-weight: 350 !important;
    color: #4e4ef4!important;
    padding-top: 50px;
    &:first-child {
      padding-top: 20px;
      margin-top: 10px;
    }
    // &:nth-child(2) {
    //   margin-top: 30px;
    // }
    // &:last-child {
    //   margin-top: 35px;
    // }
  }
}
.dotline {
  width: 70%;
  margin-left: 15%;
  margin-top: 10px;
  border-top-style: dashed;
  border-top-color: #cccbce;
}

.button {
  height: 60px;
  width: 250px;
  margin-top: 50px;
  margin-left: 60px;
  background: #4c4ce7; //背景色
  border-width: 0px; //边缘的宽度，如果要分别设置可以这样：border-width: 15px 5px 15px 5px;依次为上、右、下、左
  border-style: solid;
  border-radius: 15px; //圆角的大小
  text-align: center;
  font-size: 22px;
  font-family: "Gill Sans";
  font-weight: 350;
  padding-top: 20px;
  color: #f7f7fd;
  box-shadow: 0 0 30px 20px #e3e2ea;
}
.item_container_style {
  height: 200px;
}
.home_logo {
  width: 90%;
  margin-top: 20%;
}
.item_list_container {
  position: absolute;
  height: 7rem;
  width: 8rem;
  top: 2.4rem;
  left: 3rem;
  -webkit-font-smoothing: antialiased;
}
.item_title {
  font-size: 0.65rem;
  color: #00e;
  line-height: 0.7rem;
}
.item_list {
  font-size: 0;
  margin-top: 0.4rem;
  width: 10rem;
  span {
    display: inline-block;
    font-size: 0.6rem;
    color: #00e;
    vertical-align: middle;
  }
  .option_style {
    height: 0.725rem;
    width: 0.725rem;
    border: 1px solid #fff;
    border-radius: 50%;
    line-height: 0.725rem;
    text-align: center;
    margin-right: 0.3rem;
    font-size: 0.5rem;
    font-family: "Arial";
  }
  .has_choosed {
    background-color: #ffd400;
    color: #575757;
    border-color: #ffd400;
  }
  .option_detail {
    width: 7.5rem;
    padding-top: 0.11rem;
  }
}
</style>
