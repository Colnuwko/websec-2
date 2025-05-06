<template>
<div class="card mb-3 shadow-sm w-100">
    <table  class="table table-bordered">
      <tbody>
      <tr>
        <td class="w-40">
          <h3 class="card-title text-primary">{{ route.thread.title }} ({{ route.thread.number }})</h3>
          <p><strong>Перевозчик:</strong> <span class="text-info">{{ route.thread.carrier.title }}</span></p>
          <p><strong>Тип транспорта:</strong> <span class="text-muted">{{ translate(route.thread.transport_type) }}</span></p>
        </td>
        <td class="w-20">
          <p><strong>Отправление поезда:</strong> <span class="text-success">{{ formatDate(route.departure) }}</span></p>
        </td>
        <td class="20">
          <p><strong>Прибытие поезда:</strong> <span class="text-success">{{ formatDate(route.arrival) }}</span></p>
        </td>
        <td class="w-20">
          <p><strong>Дни курсирования:</strong> <span class="text-warning">{{ route.days }}</span></p>
        </td>
      </tr>
      </tbody>
   </table >
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