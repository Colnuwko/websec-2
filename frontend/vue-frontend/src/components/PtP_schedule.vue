<template>
  <div class="container mt-5">
    <h1 class="text-center">Страница 2</h1>
    <div class="text-center mb-4">
      <router-link to="/" class="btn btn-primary">Вернуться на страницу 1</router-link>
    </div>

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title">Расписание между станциями.</h2>
        <div class="mb-3">
          <label for="region" class="form-label">Откуда:</label>
          <select v-model="selectedStationStart" @change="fetchStationStart" class="form-select">
            <option v-for="item in items" :key="item.code" :value="item">
              {{ item.title }}
            </option>
          </select>
        </div>

        <div class="mb-3">
        <label for="region" class="form-label">Куда:</label>
          <select v-model="selectedStationEnd" @change="fetchStationEnd" class="form-select">
            <option v-for="item in items" :key="item.code" :value="item">
              {{ item.title }}
            </option>
          </select>
        </div>

        <div class="mb-3">
          <h3>Выберите дату</h3>
          <input type="date" v-model="selectedDate" class="form-control"/>
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
          <PtP_RouteCard
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
import PtP_RouteCard from "@/components/PtP_RouteCard.vue";
import axios from 'axios';

export default {
  components: {
    PtP_RouteCard
  },

  data() {
    return {
      items: [],
      selectedStationStart: null,
      selectedStationEnd: null,
      selectedDate: "",
      station: {},
      routes: []
    };
  },
  created() {
    this.fetchStations();
  },

  methods: {
    handleClick() {
      if (this.selectedStationEnd == null || this.selectedStationStart == null) {
        alert("Нельзя так, данные клацни")
      } else {
        axios.get('http://localhost:5000/get_schedule_between_stations', {
          params: {
            start_code_station: this.selectedStationStart.code,
            end_code_station: this.selectedStationEnd.code,
            date: this.selectedDate
          }
        })
            .then(response => {
              this.station = response.data['search']
              this.routes = response.data['schedule']
            });
      }
    },
    fetchStationStart() {
      this.$emit('station-selected-start', this.selectedStationStart);
    },
    fetchStationEnd() {
      this.$emit('station-selected-end', this.selectedStationEnd);
    },
    fetchStations() {
      axios.get('http://localhost:5000/stations', {params: {country: "Россия"},}) // ограничимся только Российскими станциями.
          .then(response => {
            this.items = response.data;
          })
          .catch(error => {
            console.error('There was an error fetching the items:', error);
          });
    },
  },
}
</script>

<style scoped>
h1, h2, h3 {
  color: #42b983;
}
label {
  font-weight: bold;
}
</style>