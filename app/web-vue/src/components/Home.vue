<template>
  <div class="container">

    <h1>Кинотеатры вашего города!</h1>

    <div class="search row">
      <div class="name col-sm-12 col-md-8 col-lg-6">
        <input type="text" class="form-control" placeholder="Введите название фильма" v-model="fname">
      </div>
      <div class="city col-sm-12 col-md-4 col-lg-6">
        <select class="form-control" v-on:change="getData($event.target.value)">
          <option id="cityData" v-for="town in cities" v-bind:value="town.id"> {{ town.city }}</option>
        </select>
      </div>
    </div>

    <div class="films">
      <div v-for="item in filtredItems" class="film">
        <a class="filmlink" :href="'/#/film/'+item.id">
          <img class="kartinka" :src="item.image">
          <div class="descr">{{item.text}}</div>
        </a>
      </div>

      <!--эти для заполнения последнего ряда-->
      <div class="film"></div>
      <div class="film"></div>
      <div class="film"></div>
      <div class="film"></div>
    </div>

  </div>
</template>

<script>
export default {

  data() {
    return {
      isClass1:true,
      items:[],
      fname:"",
      cities: [],
      filmId: 2,
    }
  },

  created() {
    this.getData(1);
    this.getCounties();
  },

  computed: {
    filtredItems() {
      let lowerFname = this.fname.toLowerCase();
      return this.items.filter(el => el.text.toLowerCase().indexOf(lowerFname) != -1);
    }
  },

  methods: {
    getData(cityId) {
      this.items = []
      const axios = require('axios');
      axios.get('http://localhost:8000/city/' + cityId + '/?format=json').then(resp => {
        var result = resp.data
        let idLinks = result.films
        const respFilm = links => {
          return links.map(element => {
            return axios.get('http://localhost:8000/film/' + element + '/?format=json').then(resp => {
              var result = resp.data
              this.items.push({
                  id:result.id, image:result.photo, text:result.title
              });
            });
          });
        }
        let response = respFilm(idLinks)
      }
      );
    },

    getCounties() {
      const axios = require('axios');
      axios.get('http://localhost:8000/city/?format=json').then(resp => {
      var result = resp.data
      this.cities = result.map((el)=>{
        return {id: el.id, city: el.city}
      });
      }
      );
    },
  }
}

</script>

<style>
body {
  background: cadetblue;
}

.films {
  margin:30px 0px;
  display:flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.film {
  width: 200px;
}

.filmlink {
  text-decoration: none;
  color: black;
}

.kartinka {
  border: 5px dashed;
  width: 144px;
  height: 214px;
}

.filmlink:hover .kartinka {
  border: 5px dashed red;
}

.descr {
  font-family:"Comic Sans MS";
  margin-bottom: 20px;
}


.filmlink:hover .descr {
  color:red;
}



.kartinka:hover~.filmlink {
    font-weight: bolder;
}

.search {
  margin: 20px 0px;
}

.search .name {
  outline: none;
}

.search .name input, .search .city select {
  width: 100%;
  box-sizing: border-box;
  border: 0px;
  border-bottom: 2px solid #fff;
  background: transparent;
  padding: 5px 0;
  padding-left: 5px;
  outline: none;
  font-weight: bold;
}


.class1 .fa{
  color: #ffffff;
  position: absolute;
  right: 15px;
  top: 15px;
  font-size: 22px;
  cursor: pointer;
}

</style>
