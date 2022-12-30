<template>
  <div>

    <!--{{ $route.params.id }}-->

    <div id="containerFilm">
      <div id="containerData1">
        <img class="kartinka" :src="image">
        <h2> {{ titleFilm }} </h2>
        <p style="margin-top: 5%;"> <b> Выберите дату </b> </p>
      </div>
      <div>
        <ul class="list5b">
          <li id="filmDate" v-for="date in sortAsc" @click="getInfo(date)">
            {{ date.date }}
          </li>
        </ul>
      </div>
      <div class="selectSort">
        <select v-model="OrderingKey" @change="sortInfo">
          <option selected disabled hidden> Сортировать </option>
          <option value="-prices"> Цена по убыванию </option>
          <option value="prices"> Цена по возрастанию </option>
          <option value="-times"> Время по убыванию </option>
          <option value="times"> Время по возрастанию </option>
          <option value="-sessions"> Сеанс по убыванию </option>
          <option value="sessions"> Сеанс по возрастанию </option>
        </select>
      </div>
      <div>
        <section id="tableData">
          <table class="table_dark">
            <thead>
            <tr>
              <td> # </td>
              <td> Кинотеатр </td>
              <td> Адрес </td>
              <td> Сеанс </td>
              <td> Время </td>
              <td> Цена </td>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(record, index) of infoData" :key="record.id">
              <td> {{ index + 1 }} </td>
              <td> {{ record.places }} </td>
              <td> {{ record.addresses }} </td>
              <td> {{ record.sessions }} </td>
              <td> {{ record.times }} </td>
              <td> {{ record.prices + ' ₽' }} </td>
            </tr>
            </tbody>
          </table>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {

   data() {
      return {
        dates:[],
        image: "",
        idFilm: "",
        titleFilm: "",
        infoData: [],
        OrderingKey: "times",
        infoPresen: 1,
      }
   },

  computed: {
    sortAsc() {
      this.dates.sort(function(x, y) {
         return x.id - y.id;
       });
       return this.dates;

    },
  },

  created() {
    this.getData();
  },

  methods: {
    getData() {
      let self = this
      axios.get('http://localhost:8000/film/' + this.$route.params.id + '/?format=json').then(resp => {
        var result = resp.data
        self.image = result.photo
        self.idFilm = result.id
        self.titleFilm = result.title
        let idLinks = result.presentations
        const respFilm = links => {
          return links.map(element => {
            return axios.get('http://localhost:8000/presentation/' + element + '/?format=json').then(resp2 => {
              var result2 = resp2.data
              self.dates.push({
                  id:result2.id, date:result2.data_session, infoList:result2.informations
              });
            });
          });
        }
        return Promise.all(respFilm(idLinks)).then(() => {
          this.getInfo(self.dates[0]);
        })
        })
    },
    getInfo(date) {
      this.infoData = []
      this.infoPresen = date.id;
      date.infoList.forEach(element => {
        return axios.get('http://localhost:8000/info/' + element + '/?format=json').then(resp => {
          var result = resp.data
          this.infoData.push({
             places:result.place, addresses:result.address, sessions:result.session, times:result.time_session,
             prices:result.price
          });
        });
      });
    },

    sortInfo() {

      // может просто на клиенте сортировать? вот ты вверху получла данные в infoData потерялся :(
      let one = 1;
      let key = this.OrderingKey;
      if (key.startsWith("-")) {
        key = key.substr(1);
        one = -1;
      }

      console.log(one, key, this.infoData);

      this.infoData = this.infoData.sort((a,b) => {

        if (a[key] > b[key]) return one;
        else if (a[key] < b[key]) return -one;
        return 0;
      })

      //   this.infoData = []
      // console.log('http://localhost:8000/info/?format=json&info_presen=' + this.infoPresen + '&ordering=' + this.OrderingKey)
      // const axios = require('axios');
      // this.dates[idd].infoList.forEach(element => {
      //   return axios.get('http://localhost:8000/info/?format=json&info_presen=' + this.infoPresen + '&ordering=' + this.OrderingKey).then(resp => {
      //     var result = resp.data
      //     this.cities = result.map((el)=>{
      //     return { places:result.place, addresses:result.address, sessions:result.session, times:result.time_session,
      //       prices:result.price }
      //     });
      //   });
      // });
    },
  }
}

</script>

<style>

body {
  background: pink;
  width: 1000px;
  margin-left: 25%;
}

.table_dark {
  font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
  font-size: 14px;
  width: 640px;
  text-align: left;
  border-collapse: collapse;
  background: #252F48;
  margin: 10px;
}
.table_dark th {
  color: #EDB749;
  border-bottom: 1px solid #37B5A5;
  padding: 12px 17px;
}
.table_dark td {
  color: #CAD4D6;
  border-bottom: 1px solid #37B5A5;
  border-right:1px solid #37B5A5;
  padding: 7px 17px;
}
.table_dark tr:last-child td {
  border-bottom: none;
}
.table_dark td:last-child {
  border-right: none;
}
.table_dark tr:hover td {
  text-decoration: underline;
}

#containerData1 {
  margin-left: 43%;
  margin-top: 2%;
}

.list5b {
    padding:0;
    list-style: none;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}
.list5b li {
    position: relative;
    padding: 10px 30px;
    background: linear-gradient(to left, #EFEFEF 0%, #FFF, #EFEFEF);
    border: 2px solid #C0C0C0;
    color: #506a6b;
    box-shadow: 0 5px 5px 0 rgba(0,0,0, .2);
    margin-bottom: 5px;
    text-align:center;
    background-size: 100% 100%;
    z-index: 1;
}
.list5b li:hover {
    border: 2px solid #ADCEE9;
    cursor: pointer;
}
.list5b li:before {
    content: "";
    position:absolute;
    width: 0;
    height: 100%;
    top: 50%;
    left: 50%;
    background: linear-gradient(to left, #E2F0FA 0%, #FFF, #E2F0FA);
    opacity: 0;
    -webkit-transform: translateX(-50%) translateY(-50%);
    -moz-transform: translateX(-50%) translateY(-50%);
    -ms-transform: translateX(-50%) translateY(-50%);
    transform: translateX(-50%) translateY(-50%);
    -webkit-transition: all 0.3s;
    -moz-transition: all 0.3s;
    transition: all 0.3s;
    z-index: -1;
}
.list5b li:hover:before {
    width: 100%;
    opacity: 1;
}

.selectSort {
  margin-left: 40%;
}

</style>
