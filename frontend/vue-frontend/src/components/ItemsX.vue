<template>
  <div>
    <h1>Страница 1</h1>
    <router-link to="/p2p_schedule">Перейти на страницу 2</router-link>
  </div>
  <div>
    <div>
      <h1>Расписание одинокой станции.</h1>
      <label for="region">Выберите станцию:</label>
      <select v-model="selectedStations" @change="fetchSchedule">
        <option v-for="item in items" :key="item.code" :value="item">
          {{ item.title }}
        </option>
      </select>
    </div>
    <div>
    <label for="region">Выберите регион:</label>
      <select v-model="selectedRegion" @change="fetchStations">
        <option v-for="region in regions" :key="region.code" :value="region">
          {{ region.title }}
        </option>
      </select>
    </div>
    <div>
      <h1>Выберите дату</h1>
      <input type="date" v-model="selectedDate" />
      <p>{{ selectedDate }}</p>
    </div>
    <div>
      <button @click="handleClick">Дай расписание</button>
    </div>
  </div>
  <div>
    <h1>Расписание поездов</h1>
    <div class="routes-list">
      <RouteCard
        v-for="(route, index) in routes"
        :key="index"
        :route="route"
      />
    </div>
  </div>

</template>

<script>
import RouteCard from "@/components/RouteCard.vue";
import axios from 'axios';

export default {
  components: {
    RouteCard
  },

  data() {
    return {
      items: [],
      regions: [],
      selectedRegion: null,
      selectedStations: null,
      selectedDate: "",
      station: {},
      routes: []
    };
  },
  created() {
    this.fetchRegions();
  },

  methods: {
    async fetchRegions() {
      const response = await axios.get('http://localhost:5000/get_countries'); // Подставьте ваш адрес API
      this.regions = response.data;
    },
    handleClick() {
      if (this.selectedRegion == null || this.selectedStations == null)
      {
        alert("Нельзя так, данные клацни")
      }
      else {
        axios.get('http://localhost:5000/get_schedule_for_one_station', {params: {code_station: this.selectedStations.code, date: this.selectedDate}})
            .then(response => {
              this.station = response.data['station']
              this.routes = response.data['schedule']
              console.log(this.routes)
            });
      }
    },
    fetchSchedule() {
      this.$emit('station-selected', this.selectedStations);
    },
    fetchStations() {
      this.$emit('region-selected', this.selectedRegion);
          axios.get('http://localhost:5000/stations', {params: {country: this.selectedRegion.title},})
      .then(response => {
        this.items = response.data;
        console.log(this.items)
      })
      .catch(error => {
        console.error('There was an error fetching the items:', error);
      });
    },
  },

};

</script>

<style scoped>

h1 {
  color: #42b983;
}

</style>