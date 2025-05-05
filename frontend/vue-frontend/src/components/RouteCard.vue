<template>
  <div class="route-card">
    <h3>{{ route.thread.title }} ({{ route.thread.number }})</h3>
    <p><strong>Перевозчик:</strong> {{ route.thread.carrier.title }}</p>
    <p><strong>Отправление поезда:</strong> {{ formatDate(route.departure) }}</p>
    <p><strong>Прибытие поезда:</strong> {{ formatDate(route.arrival) }}</p>
    <p><strong>Дни курсирования:</strong> {{ route.days }}</p>
    <p><strong>Остановки:</strong> {{ route.stops }}</p>
    <p><strong>Тип транспорта:</strong> {{ translate(route.thread.transport_type) }}</p>

  </div>
</template>

<script>
export default {
  name: 'RouteCard',
  props: {
    route: Object
  },
  methods: {
    formatDate(dateString) {
      const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
      };
      if(dateString == null)
      {
        return "Нет данных"
      }
      return new Date(dateString).toLocaleString('ru-RU', options);
    },

    translate(word) { // надеюсь вы тоже в шоке с такого перевода)
      const dictionary = {
      plane: "самолет",
      train: "поезд",
      suburban: "электричка",
      bus: "автобус",
      water: "водный транспорт",
      helicopter: "вертолет"
    }
      return dictionary[word] || "Переводчик отказался работать за бесплатно";
    }
  }
}
</script>

<style scoped>
.route-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin: 8px;
  background-color: #f9f9f9;
}
</style>