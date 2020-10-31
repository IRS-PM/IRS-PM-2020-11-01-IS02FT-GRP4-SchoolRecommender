<template>
  <div>
  <div class="selection_header">
          <img
        alt="Vue logo"
        src="../images/process_bar_2.png"
        style="width:300px;height:35px;margin-left:35px;margin-top:35px"
      />
  </div>
    <div class="input_wrap">
      <div>
        <form id="info_form">

        <table>
          <tr>
            <dl>
              <dt>
                <span style="width: 370px;font-size: 20px;height: 50px"> Graduate School*</span>
              </dt>
              <dd>
                  <select class="select1"  ref="school">

                  <option selected="selected" disabled="disabled"  style='display: none' value=''></option>
                  <option value ="1">Tsinghua University/Beijing University</option>
                  <option value ="2">SJTU/FUDAN/NJU/ZJU/USTC</option>
                  <option value="3">HIT/XJTU</option>
                  <option value="4">BUPT/CUFE/SUFE/UIBE</option>
                  <option value="5">Other "985" universities</option>
                  <option value="6">Other "211" universities</option>
                  <option value="7">Overseas university</option>
                  <option value="8">Others</option>
                </select>

              </dd>
            </dl>
          </tr>

          <tr>
            <dl>
              <dt>
                <span style="width: 370px;font-size: 20px;height: 50px"> Major*</span>
              </dt>
              <dd>
                  <select class="select1" ref="major">
                  <option selected="selected" disabled="disabled"  style='display: none' value=''></option>
                  <option value ="1">Medical</option>
                  <option value ="2">Traditional engineering</option>
                  <option value="3">Business</option>
                  <option value="4">Computer Science/Electronic Engineering</option>
                  <option value="5">Liberal Arts</option>
                  <option value="6">Finance</option>
                  <option value="7">Science</option>
                  <option value="8">Others</option>
                </select>
              </dd>
            </dl>
          </tr>

          <tr>
            <td>
              <dl>
                <dt>
                  <span style="width: 370px;font-size: 20px;height: 50px"> GPA*</span>

                </dt>
                <dd>
                    <select class="select2" ref="GPA_scale">
                    <option selected="selected" disabled="disabled"  style='display: none' value=''></option>
                    <option value ="4">4</option>
                    <option value ="5">5</option>
                    <option value ="100">100</option>
                  </select>
                </dd>
              </dl>
            </td>

            <td>
              <dl>
                <dt>
                  <span style="width: 370px;font-size: 20px;height: 50px"> GPA Rank*</span>
                </dt>
                <dd>
                  <input class="input2" type="text" ref="GPA_rank" v-on:input="checkGPA">

                </dd>
              </dl>
            </td>
          </tr>

          <tr>

            <td><span style="width: 100px;font-size: 20px;height: 50px"> TOELF*</span>
              <input type="radio" value="TOEFL"  name="lg" v-model="language" checked></td>
            <td><span style="width: 100px;font-size: 20px;height: 50px"> IELTS*</span>
              <input type="radio" value="IELTS"  name="lg" v-model="language"></td>
          </tr>

          <tr>
            <td><span style="width: 100px;font-size: 20px;height: 50px"> Score*</span></td>
            <td><input width="150px" class="input2" type="text"  ref="language_score" v-on:input="checkLanguage"></td>

          </tr>

          <tr>
            <td>

              <dl>
                <dt>
                  <span style="width: 370px;font-size: 20px;height: 50px">  Entrance Test</span>

                </dt>
                <dd>
                  <select class="select2" ref="entrance">
                    <option selected="selected" disabled="disabled"  style='display: none' value=''></option>
                    <option value ="GRE">GRE</option>
                    <option value ="GMAT">GMAT</option>
                  </select>
                </dd>
              </dl>
            </td>

            <td>
              <dl>
                <dt>
                  <span style="width: 370px;font-size: 20px;height: 50px"> Score</span>
                </dt>
                <dd>

                  <input class="input2" type="text" ref="entrance_score">
                </dd>
              </dl>
            </td>
          </tr>

        </table>
        </form>
      </div>
    </div>
                  <div class="td_content">
                <button @click="info_submit" id="info_button">Next ></button>
              </div>
  </div>
</template>


<script>
export default {
  name: "personalInfo",

        data(){
            return{
              locations :"",
              school :"",
              major : "",
              GPA_scale : "",
              GPA_rank : "",
              entrance : "",
              entrance_score :"",
              language_score : "",
              language : "IELTS",
                }
        },
      created(){

      },

      methods: {

        info_submit: function (event) {
          this.locations = this.$route.query.locations;
          this.school = this.$refs.school.value;
          this.major = this.$refs.major.value;
          this.GPA_scale = this.$refs.GPA_scale.value;
          this.GPA_rank = this.$refs.GPA_rank.value;
          this.entrance = this.$refs.entrance.value;
          this.entrance_score = this.$refs.entrance_score.value;
          this.language_score = this.$refs.language_score.value;

          if(this.checkAll()) {
            return this.$router.push({
              name: "personalComp",
              query: {
                locations: this.locations,
                school: this.school,
                major: this.major,
                GPA_scale: this.GPA_scale,
                GPA_rank: this.GPA_rank,
                language: this.language,
                language_score: this.language_score,
                entrance: this.entrance,
                entrance_score: this.entrance_score,
              }
            });
          }
        },


        checkAll:function (){

          if(this.school=="")
          {
              this.$message({
                message: "Please select your graduate school",
                type: 'error',
                offset: 300,
              })
            return false
          }
          if(this.major=="")
          {
            this.$message({
              message: "Please select your major",
              type: 'error',
              offset: 300,
            })
            return false
          }

          if(this.GPA_scale=="")
          {
            this.$message({
              message: "Please select your GPA scale",
              type: 'error',
              offset: 300,
            })
            return false
          }

          if(this.GPA_rank=="")
          {
            this.$message({
              message: "Please input your GPA rank",
              type: 'error',
              offset: 300,
            })
            return false
          }

          if(this.language_score=="")
          {
            this.$message({
              message: "Please input your language score",
              type: 'error',
              offset: 300,
            })
            return false
          }

          if(!(this.checkNumber(this.GPA_rank)&&this.checkGPAScale(this.GPA_rank)))
          {
            this.$message({
              message: "Please check if you input right GPA scale",
              type: 'error',
              offset: 300,
            })
            return false
          }

          if(!(this.checkNumber(this.language_score)&&this.checkLanguageType(this.language_score)))
          {
            this.$message({
              message: "Please check if you input right language score",
              type: 'error',
              offset: 300,
            })
            return false
          }
          return true
        },

        checkGPA: function () {
          // check gpa input while typing
          var GPA_rank = this.$refs.GPA_rank.value
          if (!this.checkNumber(GPA_rank)) {
            this.$message({
              message: "Please type in numbers",
              type: 'error',
              offset: 300,
            })
          }

          if (!this.checkGPAScale(GPA_rank)) {
            this.$message({
              message: "GPA Rank must fit your selected GPA Scale",
              type: 'error',
              offset: 300,
            })
          }

        },

        checkNumber: function (input) {
          //check if the input is a number, if yes return true
          if ((/^[0-9]{1}([0-9]|[.])*$/.test(input))) {
            return true
          } else
            return false
        },

        checkGPAScale: function (input) {
          //check if the input rank fits the scale, if yes return true
          var scale = parseFloat(this.$refs.GPA_scale.value)
          input = parseFloat(input)
          if (input >= 0 && input <= scale)
            return true
          else
            return false
        },


        checkLanguage:function (){
          //check language input while typing
          var language_score = this.$refs.language_score.value
          if (!this.checkNumber(language_score)) {
            this.$message({
              message: "Please type in numbers",
              type: 'error',
              offset: 300,
            })
          }

          if(!this.checkLanguageType(language_score)){
            this.$message({
              message: "Language score must fit your selected language type",
              type: 'error',
              offset: 300,
            })
          }

        },

        checkLanguageType:function (input){
          // check if the input language score fit selected language type
          var language = this.language
          input = parseFloat(input)
          if(language=="IELTS"){
            if(input <= 9 && input >=0)
              return true
            else
              return false
          }

          else {
            if (input <= 120 && input >= 0)
              return true
            else
              return false
            }
          },




      }
}


</script>

<style scoped>
*{
  font-size: 14px;
  color: #1c1d66;
  font-family: "Gill Sans";
  font-weight: 700;
  text-align: left;
}

#info_button{
  width: 120px;
  height: 50px;
  background: none;
  color: #232223 !important;
  border-radius: 8px;
  font-family: "Gill Sans";
  font-size: 26px;
  font-weight: 500;
}
.selection_header{
  height: 300px;
  width: 375px;
  background-image: url(../images/background4.png);
  background-repeat:no-repeat;
  border-width: 0px;
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 60px;
  border-bottom-left-radius: 60px;
  border-color: #000 #000 #000 #000;
  position: absolute;
}
.input_wrap{
  height: 500px;
  width: 330px;
  margin-top:150px;
  margin-left:20px;
  padding: 15px;
  border: 0;
  background: #ffffff;
  border-width: 0px;
  border-style: solid;
  border-radius: 28px;
  border-color: #000 #000 #000 #000;
  box-shadow: 0 4px 10px 1px #dedde4;
  position: absolute;
  overflow-y: auto;
  overflow-x: hidden;
}
tr{
  height: 80px;
  width: 375px;
}
td{
  height: 80px;
  width: 183px;
}
dt{
  width: 170px;
}
dd{
  width: 170px;
}
span {
  display:block;
  float:left;
  width:100px;
}
.input1,.select1{
  border: 1px solid #ccc;
  background-color: #f7f7fd ;
  border-radius: 5px;
  width: 300px;
  height: 30px;
  margin-bottom: 15px;
}
.input2,.select2{
  border: 1px solid #ccc;
  background-color: #f7f7fd ;
  border-radius: 5px;
  width: 120px;
  height: 30px;
  margin-bottom: 15px;
}
.td_content{
  text-align:center;
  margin-top:670px;
  margin-left: 120px;
  position: absolute;
}
</style>
