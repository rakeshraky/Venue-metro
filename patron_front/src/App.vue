<template>
  <div id="app">
    <div class="container-fluid">
      <b-navbar type="dark" style="background-image: linear-gradient(rgb(5 193 223) 45%, rgb(78 158 182) 100%);">
        <b-navbar-brand>Advanced Patron Search</b-navbar-brand>
      </b-navbar>
      <div class="row">
        <div class="col-md-7">
          <b-card class="shadow" id="filters_card">
            <div class="ribbon-wrapper">
                <div class="ribbon blue">Search</div>
            </div>
            <b-form-group>
              <b-form-group class="filter_labels"
                label-cols-sm="2"
                label="SELECT TIER:"
                label-align-sm="left"
                label-for="tier_check"
              >
                <b-form-checkbox-group class="filter_inputs" id="tier_check" v-model="checked_tier">
                  <b-form-checkbox value="Unregistered">Unregistered</b-form-checkbox>
                  <b-form-checkbox value="GUEST">Guest</b-form-checkbox>
                  <b-form-checkbox value="Bronze">Bronze</b-form-checkbox>
                  <b-form-checkbox value="SILVER">Silver</b-form-checkbox>
                  <b-form-checkbox value="GOLD">Gold</b-form-checkbox>
                  <b-form-checkbox value="PLATINUM">Platinum</b-form-checkbox>
                  <b-form-checkbox value="Diamond Plus">Diamond Plus</b-form-checkbox>
                  <b-form-checkbox value="Registered">Registered</b-form-checkbox>
                  <b-form-checkbox value="DIAMOND">Diamond</b-form-checkbox>
                  <b-form-checkbox value="Test Tier">Test Tier</b-form-checkbox>
                  <b-form-checkbox value="X Diamond Ex">X Diamond Ex</b-form-checkbox>
                  <b-form-checkbox value="Notier">Notier</b-form-checkbox>
                  <b-form-checkbox value="Active">Active</b-form-checkbox>
                  <b-form-checkbox value="Suspended">Suspended</b-form-checkbox>
                  <b-form-checkbox value="Edit">Edit</b-form-checkbox>
                  <b-form-checkbox value="Bronzeedit">Bronzeedit</b-form-checkbox>
                </b-form-checkbox-group>
              </b-form-group>
              <br>
              <b-form inline>
                <b-form-group>
                  <b-input v-model="name_input" 
                    class="mb-2 mr-sm-2 mb-sm-0 filter_inputs"
                    placeholder="Name/Badge/Account/Card"
                  ></b-input>
                  <b-input v-model="post_input"
                    class="mb-2 mr-sm-2 mb-sm-0 filter_inputs"
                    placeholder="Enter Postal Code"
                  ></b-input>
                </b-form-group>
              </b-form>
              <br>
            
                <div>
                  <b-form-group class="filter_labels" label-cols-sm="4"
                                label="STATUS:"
                                label-align-sm="left"
                                label-for="status_check">
                    <b-form-checkbox-group class="filter_inputs" style="margin-left:-16%;margin-top-1%;" align="left" id="status_check" v-model="checked_status">
                      <b-form-checkbox value="ACTIVE">Active</b-form-checkbox>
                      <b-form-checkbox value="INACTIVE">Inactive</b-form-checkbox>
                      <b-form-checkbox value="REUSED">Reused</b-form-checkbox>
                    </b-form-checkbox-group>
                  </b-form-group>
                
                <b-form-group class="filter_labels" label-cols-sm="4"
                              label="GENDER:"
                              label-align-sm="left"
                              label-for="gender_check">
                  <b-form-checkbox-group class="filter_inputs" style="margin-left:-16%;margin-top-1%;" align="left" id="gender_check" v-model="checked_gender">
                    <b-form-checkbox value="M">Male</b-form-checkbox>
                    <b-form-checkbox value="F">Female</b-form-checkbox>
                    <b-form-checkbox value="U">Unknown</b-form-checkbox>
                  </b-form-checkbox-group>
                </b-form-group>
              <div>
                <b-form-group class="filter_labels" label-cols-sm="4"
                                  label="AGE:"
                                  label-align-sm="left"
                                  label-for="slider">
                  <div>
                  <vue-slider width="77%" id="slider" align="left" v-model="value"></vue-slider>
                  <div class="filter_inputs" style="margin-left:-55%;">{{value[0]+" - "+value[1]}}</div>
                  </div><div v-on:click="reset"><b-button class="resetbutton" variant="outline-primary">Reset All</b-button></div>
                </b-form-group>
              </div>  
              <div style="margin-top:-6%">
                <b-form-group class="filter_labels" label-cols-sm="4"
                                  label="In/Out:"
                                  label-align-sm="left"
                                  label-for="check_in">
                <b-form-checkbox style="margin-left: -77%;margin-top: 1%;" @change='updatecount()' id="check_in" v-model="checked" name="check-button" switch>
                  {{count_text}}
                </b-form-checkbox>
                </b-form-group>
              </div>
              <div>
                <b-form-group class="filter_labels" label-cols-sm="4"
                                  label="Select Postal Code:"
                                  label-align-sm="left"
                                  label-for="post_code_select">
                <b-form-select  style="margin-left:-20%" id="post_code_select" v-model="post_selected" :options="options" multiple :select-size="4"></b-form-select>
                <div class="mt-3">Selected Postal Codes: <strong>{{ post_selected }}</strong></div>
                </b-form-group>
              </div>
              </div>
            </b-form-group>
          </b-card>
        </div>
        <div class="col-md-5">
          <GmapMap class="map" ref="mapRef"
              :center="coordinates"
              :zoom="7" 
              style="width: auto; height: 500px"
            >

              <GmapCircle
                :center="coordinates"
                :radius="100000"
                :visible="true"
              ></GmapCircle>

              <GmapMarker :key=m.id v-for="m in members"
                :position = "{lat:m.latitude,lng:m.longitude}"
                :clickable="true"
                :draggable="false"
              />
              
              <gmap-polygon 
              :paths="postalpath" :options="polygonoptions"
              >
              </gmap-polygon>

            </GmapMap>
            <p>Total Count : {{totalcount}}</p>
        </div>
      </div>
        <div v-if="loading" style="margin-top:10px;margin-bottom-10px">
            <div class="text-center">
              <b-spinner variant="info" label="Spinning"></b-spinner>
            </div>
        </div>
      <template>
          <b-row class="rows" cols-lg="4" cols-md="4" cols-sm="2" cols-xs="1">
              <b-col v-bind:key="member.accountid" v-for="member in filteredMembers.listitems">
                  <patron :member="member"></patron>
                </b-col>
          </b-row>
            <b-pagination
              pills :total-rows="filteredMembers.totalrows" 
              v-model="currentPage"
              :per-page="perPage"
              first-text="First"
              prev-text="Prev"
              next-text="Next"
              last-text="Last"
              align="center"
            />
      </template>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import patron from './components/patron'
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
// import {gmapApi} from 'vue2-google-maps'


export default {
  
  data(){
     return{
       polygonoptions:{strokeWeight: 2.0, fillColor: 'red'},
       loading: false,
       value: [1, 100],
       members:[], 
       marker_count: "",
       out_count: "",
       totalcount: "",
       checked: false,
       checked_tier: [],
       checked_gender: [],
       checked_status: [],
       options: [],
      post_selected:[],
       name_input: "",
       post_input: "",
       coordinates:{
         lat:0, 
         lng:0
       },
       map: null,
      bounds: {},
      mapName: "map",
      estates: [],
      markers: [] ,
      currentPage: 1,
      perPage: 8,
      count_text:"",
      postalpath: [],
      postal_codes: {},
  }
},
  components:{
       patron,
       VueSlider
  },
  methods:{
      getmembers(coords){
          this.loading = true
          axios.get("http://127.0.0.1:8000/search/",  {
    params: {
      lat: coords.lat,
      lng: coords.lng
    }
  })
          .then(res => {
            var data = JSON.parse(res.data.data)
            var postvalues = []
            this.postal_codes = res.data.postcodes
            Object.keys(res.data.postcodes).forEach(function(key) {
                postvalues.push({value:parseInt(key), text:key})
            });
            this.options = postvalues
            this.totalcount = data.length
            this.out_count = data.length - res.data.count
            this.marker_count = res.data.count
            this.count_text = "Total count within radius: " + this.marker_count
            for (var i = 0; i < data.length; i++) {
                          this.members.push(data[i].fields)
                        }
          })
          .catch(err => console.log(err))
          .finally(() => (this.loading = false))
      },
      reset() {
        this.checked_tier = [];
        this.checked_gender = [];
        this.checked_status = [];
        this.name_input = "";
        this.post_input = "";
        this.value = [1,100]
        this.post_selected = []
        this.postalpath = []
        },
        clickCallback (pageNum) {
          console.log(pageNum)
        },
        updatecount(){
          if (this.checked){
            this.count_text = "Total count within radius: " + this.marker_count
          }else{
            this.count_text = "Total count outside radius: " + this.out_count
          }
        }
//         testGoogleMaps(){
//           this.$gmapApiPromiseLazy().then(() => {
//           var latnew1 = new google.maps.LatLng(10.508742,78.120850)
//           var latnew2 = new google.maps.LatLng(11.508742,72.120850)
//           var heading = google.maps.geometry.spherical.computeHeading(latnew1,latnew2)
//           console.log(heading)
// });}
      
  },
  created(){
      this.$getLocation({})
                    .then(coordinates => {
                        this.coordinates = coordinates;
                        this.coordinates = {"lat": -33.9286, "lng": 150.9180}
                        this.getmembers(this.coordinates)
                        this.updatecount(this.marker_count)
                    })
                    .catch(error => alert(error));
      // this.testGoogleMaps()
  },
  computed:{
    // google:gmapApi,
      filteredMembers: function(){
          var result_cards = this.members.filter((member) => {
                var post_match = member.firstname.toLowerCase().match(this.name_input.toLowerCase()),
                   name_match = member.firstname.toLowerCase().match(this.name_input.toLowerCase());
                   var tier_match = true
                   var status_match = true
                   var gender_match = true
                   var postal_code_match = true
                   var start_age = this.value[0]
                   var end_age = this.value[1]
                   var age_list = []
                   for(var i=start_age;i<=end_age;i++){
                     age_list.push(i)
                   }
                  //  var age_match = age_list.includes(parseInt(member.age))
                   if (this.checked_tier.length > 0){tier_match = this.checked_tier.includes(member.tiergamingcategory)}
                   if (this.checked_status.length > 0){status_match = this.checked_status.includes(member.membership_status)}
                   if (this.checked_gender.length > 0){gender_match = this.checked_gender.includes(member.gender)}
                   if (this.post_selected.length > 0){
                     this.postalpath = []
                     for (var p=0;p<this.post_selected.length;p++){
                       this.postalpath.push(this.postal_codes[this.post_selected[p]])
                     }
                     postal_code_match = this.post_selected.includes(member.postal_code)
                     }
              return post_match && name_match && tier_match && gender_match && status_match && postal_code_match
              //  && age_match 
          })
          const items = result_cards
          return {"listitems":items.slice(
            (this.currentPage - 1) * this.perPage,
            this.currentPage * this.perPage
          ), "totalrows":items.length}
      }
      // ,  
      //  mapcoordinates(){
      //    if (!this.map) {
      //      return{
      //        lat:0,
      //        lng:0
      //      };
      //    }
      //    return{
      //     lat:this.map.getBounds(),
      //      lng:this.map.getBounds(),
      //    }
      //  }
    },
  mounted(){
  // this.$refs.mapRef.$mapPromise.then(map => this.map = map
  //       );
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.card, .map{
      margin-top: 10px;
      margin-bottom: 10px;
  }

#filters_card{
  height: 500px;
  background-image: linear-gradient(rgb(255 255 255) 45%, rgb(239 243 248) 100%);
}


  h6{
      color:#19c4ac;
  }
 
.rows{
    margin-top: 10px;
   
}
.btn-search{
    margin:10px;
}
.card_animation {
  padding: 15px; /* JUST TO LOOK COOL */
  border: 1px solid #eee;  /* JUST TO LOOK COOL */
  box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px;
  transition: all .3s ease-in-out;
}

.card_animation:hover {
  box-shadow: rgba(0, 0, 0, 0.22) 0px 19px 43px;
  transform: translate3d(0px, -1px, 0px);
}
#slider{
    width: 77%;
    height: 4px;
    margin-left: -16%;
    margin-top: 1%;
}
.resetbutton{
  margin-left: 57%;
  margin-top: -16%;
}
.labels{
  color: gray;
}
.values{
  color: black;
}
.filter_labels{
  font-weight: 600;
  color: cadetblue;
}
.filter_inputs{
  color: gray;
  font-weight: 100;
}
.ribbon.blue {
    background-color: #1a8bbc;
    background-image: -webkit-linear-gradient(top, #177aa6 45%, #1a8bbc 100%);
    background-image: -o-linear-gradient(top, #177aa6 45%, #1a8bbc 100%);
    background-image: linear-gradient(to bottom, #177aa6 45%, #1a8bbc 100%);
    background-repeat: repeat-x;
    filter: progid: DXImageTransform.Microsoft.gradient(startColorstr='#177aa6', endColorstr='#ff1a8bbc', GradientType=0)
}

.ribbon.blue:before,
.ribbon.blue:after {
    border-top: 3px solid #115979
}
 .ribbon-wrapper {
    width: 85px;
    height: 88px;
    overflow: hidden;
    position: absolute;
    top: -3px;
    right: -3px
}
.ribbon {
    font-size: 11px;
    font-weight: bold;
    color: #FFF;
    text-transform: uppercase;
    font-family: 'Montserrat Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    letter-spacing: .05em;
    line-height: 15px;
    text-align: center;
    text-shadow: 0 -1px 0 rgba(0, 0, 0, .4);
    -webkit-transform: rotate(45deg);
    -moz-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    -o-transform: rotate(45deg);
    transform: rotate(45deg);
    position: relative;
    padding: 7px 0;
    right: -11px;
    top: 10px;
    width: 100px;
    height: 28px;
    -webkit-box-shadow: 0 0 3px rgba(0, 0, 0, .3);
    box-shadow: 0 0 3px rgba(0, 0, 0, .3);
    background-color: #dedede;
    background-image: -webkit-linear-gradient(top, #ffffff 45%, #dedede 100%);
    background-image: -o-linear-gradient(top, #ffffff 45%, #dedede 100%);
    background-image: linear-gradient(to bottom, #ffffff 45%, #dedede 100%);
    background-repeat: repeat-x;
    filter: progid: DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#ffdedede', GradientType=0)
}

.ribbon:before,
.ribbon:after {
    content: "";
    border-top: 3px solid #9e9e9e;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    position: absolute;
    bottom: -3px
}

.ribbon:before {
    left: 0
}

.ribbon:after {
    right: 0
}

</style>
