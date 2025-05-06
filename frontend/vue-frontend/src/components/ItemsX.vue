<template>
<div class="container mt-5">
    <h1 class="text-center">Страница 1</h1>
    <div class="text-center mb-4">
        <router-link to="/p2p_schedule" class="btn btn-primary">Перейти на страницу 2</router-link>
    </div>

    <div class="card mb-4">
        <div class="card-body">
            <h2 class="card-title">Расписание одинокой станции</h2>
            <div class="mb-3">
                <label for="regionSelect" class="form-label">Выберите регион:</label>
                <select id="regionSelect" v-model="selectedRegion" @change="fetchStations" class="form-select">
                    <option v-for="region in regions" :key="region.code" :value="region">
                        {{ region.title }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="stationSelect" class="form-label">Выберите станцию:</label>
                <select id="stationSelect" v-model="selectedStations" @change="fetchSchedule" class="form-select">
                    <option v-for="item in items" :key="item.code" :value="item">
                        {{ item.title }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <h3>Выберите дату</h3>
                <input type="date" v-model="selectedDate" class="form-control" />
                <p class="mt-2">{{ selectedDate }}</p>
            </div>
            <div class="text-center">
                <button @click="handleClick" class="btn btn-success">Дай расписание</button>
            </div>
        </div>
    </div>

    <div class="card">
        <div class="card-body">
            <h2 class="card-title">Расписание поездов</h2>
            <div class="flex flex-row">
                <RouteCard
                    v-for="(route, index) in routes"
                    :key="index"
                    :route="route"
                    class="col-md-6 mb-4"
                />
            </div>
        </div>
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