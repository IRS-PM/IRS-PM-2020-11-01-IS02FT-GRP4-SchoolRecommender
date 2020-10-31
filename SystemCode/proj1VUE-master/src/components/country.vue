<template>
  <div style="width:375px;">
    <div class="top">
      <img
        alt="Vue logo"
        src="../images/process_bar_1.png"
        style="width:300px;height:35px;margin-left:35px;margin-top:35px"
      />
      <div class="title_style2">
        <br />Choose Locations to Study in
      </div>
      <div class="chosenlist" v-show="isnull">
        <span
          v-show="isnull"
          v-for="(item) of checkedNames"
          v-bind:key="item"
          style="color:#232223; width: 200px; word-break: keep-all; font-family: 'Gill Sans'; font-weight:500;"
        >{{ " "+ item }}</span>
      </div>
    </div>

    <div class="newapp">
      <div class="namelist2">
        <br />
        <br />

        <div class="location_name">
          <input
            type="checkbox"
            id="United States"
            value="United States"
            v-model="checkedNames"
            style="zoom:150%;"
          />
          <label for="United States">United States</label>
          <br />
          <br />

          <input
            type="checkbox"
            id="United Kingdom"
            value="United Kingdom"
            v-model="checkedNames"
            style="zoom:150%;"
          />
          <label for="United Kingdom">United Kingdom</label>
          <br />
          <br />

          <input
            type="checkbox"
            id="Europe"
            value="Europe"
            v-model="checkedNames"
            style="zoom:150%;"
          />
          <label for="Europe">Europe</label>
          <br />
          <br />

          <input
            type="checkbox"
            id="Hong Kong"
            value="Hong Kong"
            v-model="checkedNames"
            style="zoom:150%;"
          />
          <label for="Hong Kong">Hong Kong</label>
          <br />
        </div>
        <div class="location_name2">
          <input
            type="checkbox"
            id="Australia"
            value="Australia"
            v-model="checkedNames"
            style="zoom:150%;"
          />
          <label for="Australia">Australia</label>
          <br />
          <br />

          <input
            type="checkbox"
            id="Canada"
            value="Canada"
            v-model="checkedNames"
            style="zoom:150%;"
          />
          <label for="Canada">Canada</label>
          <br />
          <br />

          <input
            type="checkbox"
            id="Singapore"
            value="Singapore"
            v-model="checkedNames"
            style="zoom:150%;"
          />
          <label for="Singapore">Singapore</label>
          <br />
        </div>
      </div>
      <div style="margin-top: 20px">
        <button @click="location_submit" id="location_button">Next ></button>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "location",

  data() {
    return {
      checked: false,
      checkedNames: []
    };
  },

  computed: {
    isnull: function() {
      return this.checkedNames.length != 0;
    }
  },
  methods: {
    location_submit: function(event) {
      var locations = JSON.stringify(this.checkedNames);
      if (this.checkedNames.length == 0) { // alert message
        this.$message({
          message: "Please select at least one location to continue",
          type: 'error',
          offset: 300,
        })
      }

      else {
        return this.$router.push({
          name: "personalInfo",
          query: {
            locations: locations
          }
        });

      }
    }
  },



};
</script>
<style>
/*.button {*/
/*  height: 40px;*/
/*  width: 50%;*/
/*  margin-top: 55px;*/
/*  margin-left: 25%;*/
/*  background: #4c4ce7;*/
/*  border-width: 0px;*/
/*  border-style: solid;*/
/*  border-radius: 15px;*/
/*  text-align: center;*/
/*  font-size: 25px;*/
/*  font-family: "Gill Sans";*/
/*  font-weight: 350;*/
/*  padding-top: 5%;*/
/*  color: #f7f7fd;*/
/*  box-shadow: 0 0 30px 20px #e3e2ea;*/
/*}*/
#location_button {
  width: 120px;
  height: 50px;
  background: none;
  color: #232223 !important;
  border-radius: 8px;
  font-family: "Gill Sans";
  font-size: 26px;
  font-weight: 500;
}
.newapp {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 270px;
  position: absolute;
}
.namelist2 {
  height: 400px;
  width: 330px;
  margin-left: 20px;
  background: #ffffff;
  border-width: 0px;
  border-style: solid;
  border-radius: 28px;
  border-color: #000 #000 #000 #000;
  box-shadow: 0 4px 10px 3px #dedde4;
  font-family: "Gill Sans";
  font-size: 18px;
  text-align: right;
}
.chosenlist {
  height: 50px;
  width: 90%;
  margin-left: 5%;
  /* border-width: 0px;
  border-style: solid;
  border-color: #000 #000 #000 #000;
  box-shadow: 0 3px 70px 0px #807f7f; */
  text-align: center;
  font-family: "Gill Sans";
  font-size: 25px;
}
.location_name {
  font-family: "Gill Sans";
  text-align: left;
  color: #807f7f;
  font-weight: 500;
  font-size: 20px;
  height: 0px;
  width: 160px;
  margin-left: 20px;
}
.location_name2 {
  font-family: "Gill Sans";
  text-align: left;
  color: #807f7f;
  font-weight: 500;
  font-size: 20px;
  height: 30px;
  width: 160px;
  margin-left: 190px;
}
/*#app {*/
/*  font-family: Avenir, Helvetica, Arial, sans-serif;*/
/*  -webkit-font-smoothing: antialiased;*/
/*  -moz-osx-font-smoothing: grayscale;*/
/*  text-align: center;*/
/*  color: #2c3e50;*/
/*  margin-top: 0px;*/
/*  margin:0;*/
/*  padding:0;*/
/*}*/
.top {
  position: absolute;
  width: 375px;
  height: 370px;
  display: inline-block;
  background: url(../images/background2.png) no-repeat;
  background-size: 375px 370px;
  margin-top: 0px;
  border-width: 0px;
  border-style: solid;
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 15px;
  border-bottom-left-radius: 15px;
  border-color: #000 #000 #000 #000;
  margin-top: 0px;
}

.title_style2 {
  text-align: center;
  margin-top: 0px;
  height: 100px;
  font-size: 28px;
  font-family: "Gill Sans";
  font-weight: 400;
  color: #1c1d66;
}
</style>

<style>
.el-message-box {
  width: 350px;
}
</style>
