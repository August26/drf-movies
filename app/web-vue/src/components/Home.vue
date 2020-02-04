<template>
  <div>
    <h1>Кинотеатры вашего города!</h1>
    <div :class="{class1:isClass1}">
      <input placeholder="Введите название фильма" size="100" v-model="fname">
    </div>
    <div id="filedForData">
      <div v-for="item in filtredItems">
        <img class="kartinka" :src="item.image">
        <a :href="item.link">{{item.text}}</a>
      </div>
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
    }
  },

  created() {
    this.getData();
  },

  computed: {
  filtredItems() {
    return this.items.filter(el => el.text.indexOf(this.fname) != -1);
  }
  },

  methods: {

    getData() {

      const axios = require('axios');
      axios.get('http://localhost:8000/Movie/?format=json').then(resp => {
      var result = resp.data
      let i = result.length;
      while (i) {

      this.items = result.map((el)=>{

      console.log("http://localhost:8000/Movie/" + el.id);

      return {
        id:el.id, image:"https://img04.rl0.ru/kassa/c144x214q80i/s1.kassa.rl0.ru/StaticContent/P/Aimg/2001/03/200103072509375.jpg?1576764116",
        link: "http://localhost:8000/Movie/" + el.id + "?format=json",
        text:el.title}
      });
        i--;
       }
      }
      );
    }
  }
}

</script>

<style>
body {
  background:pink;
}

</style>
