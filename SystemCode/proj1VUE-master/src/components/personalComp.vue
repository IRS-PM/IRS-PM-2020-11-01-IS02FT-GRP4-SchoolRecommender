<template>
  <div>
    <div class="selection_header">
                <img
        alt="Vue logo"
        src="../images/process_bar_3.png"
        style="width:300px;height:35px;margin-left:35px;margin-top:35px"
      />
    </div>
    <div class="input_wrap" >
      <div style="width: 375px;height: 50px">
        <span style="width: 370px;font-size: 20px;height: 50px;" >   WORKING EXPERIENCE </span><input class="plus_button" type="button" @click="addLine_we">
      </div>
      <el-table :data="tableData_we" :header-row-style="{height:'40px'} " >
        <el-table-column prop="industry" label="Industry">
          <template slot-scope="scope">
            <el-input v-model="scope.row.industry" placeholder="" class="input2"></el-input>
          </template>
        </el-table-column>

        <el-table-column prop="working_years" label="Working Years">
          <template slot-scope="scope">
            <el-input v-model="scope.row.duration" placeholder="" class="input2" v-on:input="checkNumber"></el-input>

            <input class="sub_button" type="button" @click="handleDelete_we(scope.$index, scope.row)"></input>
          </template>
        </el-table-column>

      </el-table>


      <div style="width: 375px;height: 50px">
        <span style="width: 370px;font-size: 20px;height: 50px" >RESEARCH EXPERIENCE </span><input class="plus_button" type="button" @click="addLine_re">
      </div>
      <el-table :data="tableData_re">
        <el-table-column prop="paper_level" label="Paper Level" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.paper_level" placeholder="" class="input2"></el-input>
          </template>
        </el-table-column>

        <el-table-column prop="quantity" label="Quantity">
          <template slot-scope="scope">
            <el-input v-model="scope.row.quantity" placeholder="" class="input2" v-on:input="checkNumber"></el-input>
            <input class="sub_button" type="button" @click="handleDelete_re(scope.$index, scope.row)"></input>
          </template>
        </el-table-column>
      </el-table>

      <div style="width: 375px;height: 50px">
        <span style="width: 370px;font-size: 20px;height: 50px">Internship </span><input class="plus_button" type="button" @click="addLine_in">
      </div>
      <el-table :data="tableData_in" >
        <el-table-column prop="industry" label="Industry" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.industry" placeholder="" class="input2"></el-input>
          </template>
        </el-table-column>

        <el-table-column prop="duration" label="Duration">
          <template slot-scope="scope">
            <el-input v-model="scope.row.duration" placeholder="" class="input2" v-on:input="checkNumber"></el-input>
            <input class="sub_button" type="button" @click="handleDelete_in(scope.$index, scope.row)"></input>

          </template>
        </el-table-column>
      </el-table>

      <div style="width: 375px;height: 50px">
        <span style="width: 370px;font-size: 20px;height: 50px">Exchange </span><input class="plus_button" type="button" @click="addLine_ex">
      </div>
      <el-table :data="tableData_ex" >
        <el-table-column prop="school" label="School" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.school" placeholder="" class="input2"></el-input>
          </template>
        </el-table-column>

        <el-table-column prop="duration" label="Duration">
          <template slot-scope="scope">
            <el-input v-model="scope.row.duration" placeholder="" class="input2" v-on:input="checkNumber"></el-input>
            <input class="sub_button" type="button" @click="handleDelete_ex(scope.$index, scope.row)"></input>
          </template>
        </el-table-column>
      </el-table>


      <div style="width: 375px;height: 50px">
        <span style="width: 370px;font-size: 20px;height: 50px">Scholarship </span><input class="plus_button" type="button" @click="addLine_sp">
      </div>
      <el-table :data="tableData_sp" >
        <el-table-column prop="level" label="Level" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.level" placeholder="" class="input2"></el-input>
          </template>
        </el-table-column>

        <el-table-column prop="times" label="Times">
          <template slot-scope="scope">
            <el-input v-model="scope.row.duration" placeholder="" class="input2" v-on:input="checkNumber"></el-input>
            <input class="sub_button" type="button" @click="handleDelete_sp(scope.$index, scope.row)"></input>
          </template>
        </el-table-column>
      </el-table>

      <div style="width: 375px;height: 50px">
        <span style="width: 370px;font-size: 20px;height: 50px">Competition </span><input class="plus_button" type="button" @click="addLine_cp">
      </div>
      <el-table :data="tableData_cp" >
        <el-table-column prop="award" label="Award">
          <template slot-scope="scope">
            <el-input v-model="scope.row.award" placeholder="" class="input2" ></el-input>
          </template>
        </el-table-column>
        <el-table-column prop="times" label="Times">
          <template slot-scope="scope">
            <el-input v-model="scope.row.duration" placeholder="" class="input2" v-on:input="checkNumber"></el-input>
            <input class="sub_button" type="button" @click="handleDelete_cp(scope.$index, scope.row)"></input>
          </template>
        </el-table-column>
      </el-table>

    </div>
          <div class="td_content">
        <input class="button1" type="button" value="Submit >" @click="comp_submit">
      </div>
  </div >

</template>

<script>
import { putUsersInfo } from "../axios/axios-api";

export default {
  name: "personalComp",
  data() {
    return {
      tableData_we:[{
        industry: '',
        duration: '',

      }],
      tableData_re:[{
        paper_level: '',
        quantity: '',

      }],
      tableData_in:[{
        industry: '',
        duration: '',

      }],
      tableData_ex:[{
        school: '',
        duration: '',

      }],
      tableData_sp:[{
        level: '',
        times: '',

      }],
      tableData_cp:[{
        award:'',
        times:'',

      }],
    }
  },


  methods:{

    addLine_we(){ //添加行数
      var newValue = {
        industry: '',
        duration: '',
      };
      //添加新的行数
      this.tableData_we.push(newValue);
    },
    handleDelete_we(index){ //删除行数
      this.tableData_we.splice(index,1)
    },

    addLine_re(){ //添加行数
      var newValue = {
        paper_level: '',
        quantity: '',
      };
      //添加新的行数
      this.tableData_re.push(newValue);
    },

    handleDelete_re(index){ //删除行数
      this.tableData_re.splice(index,1)
    },

    addLine_in(){ //添加行数
      var newValue = {
        industry: '',
        duration: '',
      };
      //添加新的行数
      this.tableData_in.push(newValue);
    },

    handleDelete_in(index){ //删除行数
      this.tableData_in.splice(index,1)
    },

    addLine_ex(){ //添加行数
      var newValue = {
        school: '',
        duration: '',
      };
      //添加新的行数
      this.tableData_ex.push(newValue);
    },

    handleDelete_ex(index){ //删除行数
      this.tableData_ex.splice(index,1)
    },

    addLine_sp(){ //添加行数
      var newValue = {
        level:'',
        times: '',
      };
      //添加新的行数
      this.tableData_sp.push(newValue);
    },

    handleDelete_sp(index){ //删除行数
      this.tableData_sp.splice(index,1)
    },


    addLine_cp(){ //添加行数
      var newValue = {
        award:'',
        times:''
      };
      //添加新的行数
      this.tableData_cp.push(newValue);
    },

    handleDelete_cp(index){ //删除行数
      this.tableData_cp.splice(index,1)
    },
    checkNumber: function (input) {
          //check if the input is a number, if yes return true
          if (!(/^[0-9]*$/.test(input))) {
            this.$message({
              message: "Please type in numbers",
              type: 'error',
              offset: 300,
            })
          } 
        },

    comp_submit(){
      // console.log(JSON.stringify(this.tableData_we));
      // console.log(JSON.stringify(this.tableData_re));
      // console.log(JSON.stringify(this.tableData_in));
      // console.log(JSON.stringify(this.tableData_sp));
      // console.log(JSON.stringify(this.tableData_cp));
      // console.log(JSON.stringify(this.tableData_ex))
      var locations = this.$route.query.locations;
      var school = parseInt(this.$route.query.school);
      var major = parseInt(this.$route.query.major);
      var language = this.$route.query.language;
      var language_score = parseFloat(this.$route.query.language_score);
      var GPA_scale = parseFloat(this.$route.query.GPA_scale);
      var GPA_rank = parseFloat(this.$route.query.GPA_rank);
      var entrance = this.$route.query.entrance;
      var entrance_score = parseFloat(this.$route.query.entrance_score);

      var working_experience_origin = this.tableData_we;
      var research_experience_origin = this.tableData_re;
      var internship_origin = this.tableData_in;
      var scholarship_origin = this.tableData_sp;
      var exchange_origin = this.tableData_ex;
      var competition_origin = this.tableData_cp;

      // var working_experience = JSON.stringify(this.tableData_we);
      // var research_experience = JSON.stringify(this.tableData_re);
      // var internship = JSON.stringify(this.tableData_in);
      // var scholarship = JSON.stringify(this.tableData_sp);
      // var exchange = JSON.stringify(this.tableData_ex);
      // var competition = JSON.stringify(this.tableData_cp);

      var working_experience = []
      var research_experience = []
      var internship = []
      var scholarship = []
      var exchange = []
      var competition = []

      console.log(this.tableData_we)

      
      for (var i=0;i<working_experience_origin.length;i++){
        var notempty=false;
        for (var key in  working_experience_origin[i]) {
　　            if (working_experience_origin[i][key]!= ""){
                          notempty=true;break}} 
        if (notempty){
              working_experience.push(working_experience_origin[i])
              console.log("[DEBUG]working_experience_origin",working_experience_origin[i])
            }
      }

      for (var i=0;i<internship_origin.length;i++){
        var notempty=false;
        for (var key in  internship_origin[i]) {
　　            if (internship_origin[i][key]!= ""){notempty=true;break}} 
        if (notempty){
              internship.push(internship_origin[i])
            }
      }

      for (var i=0;i<research_experience_origin.length;i++){
        var notempty=false;
        for (var key in  research_experience_origin[i]) {
　　            if (research_experience_origin[i][key]!= ""){notempty=true;break}} 
        if (notempty){
              research_experience.push(research_experience_origin[i])
            }
      }

      for (var i=0;i<research_experience_origin.length;i++){
        var notempty=false;
        for (var key in  research_experience_origin[i]) {
　　            if (research_experience_origin[i][key]!= ""){notempty=true;break}} 
        if (notempty){
              research_experience.push(research_experience_origin[i])
            }
      }



      return this.$router.push({
        name: "results",
        query: {
          locations:locations,
          school:school,
          major:major,
          GPA_scale:GPA_scale,
          GPA_rank:GPA_rank,
          language:language,
          language_score:language_score,
          entrance:entrance,
          entrance_score:entrance_score,
          working_experience:working_experience,
          research_experience:research_experience,
          internship:internship,
          scholarship:scholarship,
          exchange:exchange,
          competition:competition
        }
      });


    }
  }
}

</script>

<style lang="scss">
.el-input__inner{
    border: 0px solid #ccc !important;
    background-color: #f7f7fd !important;
    border-radius: 5px !important;
    width: 100px !important;
}

.input_wrap {
  >>> .cell {
    width: 180px !important;
    height: 60px !important;
    margin-top: 0px !important;
    background: #f7f7fd !important;
    border-width: 0px !important;
    border-style: solid !important;
    border-radius: 28px !important;
    box-shadow: 0 0 0px 0px #e3e2ea !important;
    -ms-flex-pack: justify !important;
    justify-content: space-between !important;
    padding: 20px !important;
    border-color: #f7f7fd #f7f7fd #f7f7fd #f7f7fd !important;
    font: 'Gill Sans';
  }
}
.th{
  width: 200px !important;
  height: 100px !important;
}
.el-table td, .el-table th.is-leaf {
   border-bottom: 0px solid #EBEEF5 !important;
  padding: 5px 0px !important;
 }
// *{
//   font-size: 14px;
//   color: #1c1d66 !important;
//   font-family: "Gill Sans" !important;
//   font-weight: 700 !important;
// }

</style>

<style scoped >
*{  font-size: 14px;
  color: #1c1d66;
  font-family: "Gill Sans";
  font-weight: 700;
}

.input_wrap /deep/ .el-input{
  border: 0px solid #ccc ;
  /*background-color: #1c1d66 ;*/
  border-radius: 5px ;
  width: 100px ;
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
.button1{
  width: 120px;
  height: 50px;
  background: none;
  color: #23d082;
  border-radius: 8px;
  font-family: "Gill Sans";
  font-size: 26px;
  font-weight: 500;
  
}
.plus_button{
  width: 15px;
  height: 15px;
  background-size:15px 15px;
  background-image:url("../images/plus.png");
  background-color: transparent;
  background-repeat:no-repeat;
  border: 0;
}

.sub_button{
  width: 15px;
  height: 15px;
  background-size:15px 15px;
  background-image:url("../images/sub.png");
  background-color: transparent;
  background-repeat:no-repeat;
  border: 0;

}

dt{
  width: 100px;
}
.td_content{
  margin-top: 670px;
  margin-left:120px;
  text-align:center;
  color:#ffffff;
  position:absolute;
}

</style>

