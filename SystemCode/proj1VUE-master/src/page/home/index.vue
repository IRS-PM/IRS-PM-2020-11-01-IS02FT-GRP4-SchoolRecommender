<template>
  	<div class="home_container">
              <itemcontainer father-component="home"></itemcontainer>

        <!-- <country father-component="home"></country> -->
<!--      <personal-info father-component="home"></personal-info>-->
    </div>
</template>

<script>
import itemcontainer from '../../components/itemcontainer'
import results from '../../components/Results'

export default {
	name: 'home',
  	components: {
          itemcontainer,
          results
  	},
    created(){
        
    }
}
</script>

<style lang="less" scoped>
    .home_container{

    }
</style>
