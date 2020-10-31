<template>
  
</template>

<script>
import result from "components/Results/Result";
import levelDetail from "components/Results/LevelDetail/";

export default {
  components: {
    result,
    levelDetail

  },
  name: "results",
  data() {
    return {
      showMainPanel:true,
      rotate_left: 0, //left circle rotate degree
      rotate_right: 0, //right circle rotate degree
      exceed_percent: 50,
      evaluation_level: "A",
      schoolList: [
        {
          school_id:"1",
          school_name: "National University of Singapore",
          major_name: "Intelligent System",
          location: "Singapore",
          score: 90,
          color: "#22c278"
        },
        {
          school_id:"2",
          school_name: "Kings College London",
          major_name: "EBAC",
          location: "United Kingdom",
          score: 75,
          color: "#f2af00"
        }
      ],
      emptyList: require("../../images/emptyList.png"),
      nexticon: require("../../images/next.png")
    };
  },
  methods:{
    changePanel(data){
      this.showMainPanel=data
    },
    toSchoolDetail(school_id) {
      this.$router.push({
        path: "/schoolDetail",
        query: {
          school_id: school_id,
        }
      });
    },
  }

};
</script>

<style>

</style>
