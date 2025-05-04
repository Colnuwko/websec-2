<template>

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

  </div>

</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      items: [],
      regions: [],
      selectedRegion: null,
      selectedStations: null
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

    fetchSchedule() {
      this.$emit('station-selected', this.selectedStations);
      console.log(this.selectedStations.code)
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