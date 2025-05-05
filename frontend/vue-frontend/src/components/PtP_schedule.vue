<template>
  <div>
    <h1>Страница 2</h1>
    <router-link to="/">Вернуться на страницу 1</router-link>
  </div>
  <div>
    <div>
      <h1>Расписание между станциями.</h1>
      <label for="region">Откуда:</label>
      <select v-model="selectedStationStart" @change="fetchStationStart">
        <option v-for="item in items" :key="item.code" :value="item">
          {{ item.title }}
        </option>
      </select>
    </div>
    <div>
    <label for="region">Куда:</label>
      <select v-model="selectedStationEnd" @change="fetchStationEnd">
        <option v-for="item in items" :key="item.code" :value="item">
          {{ item.title }}
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
      <PtP_RouteCard
        v-for="(route, index) in routes"
        :key="index"
        :route="route"
      />
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
h1 {
  color: #42b983;
}

</style>