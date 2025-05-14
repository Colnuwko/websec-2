<template>
<div class="card mb-3 w-100">
    <table  class="table table-bordered table-hover b-table-fixed mb-0">
      <tbody>
      <tr>
        <td class="col-4 largeScreen">
          <div>
            <h3 class="text-primary">{{ route.thread.title }} ({{ route.thread.number }})</h3>
            <p><strong>Перевозчик:</strong> <span class="text-info">{{ route.thread.carrier.title }}</span></p>
            <p><strong>Тип транспорта:</strong> <span class="text-muted">{{ translate(route.thread.transport_type) }}</span></p>
          </div>
        </td>
        <td class="col-2 largeScreen" >
          <div>
            <div class="w-100"><strong>Отправление поезда:</strong></div>
            <div class="w-100"><span class="text-success">{{ formatDate(route.departure) }}</span></div>
          </div>
        </td>
        <td class="col-2 largeScreen">
          <div>
            <div class="w-100"><strong>Прибытие поезда:</strong></div>
            <div class="w-100"><span class="text-success">{{ formatDate(route.arrival) }}</span></div>
          </div>
        </td>
        <td class="col-2 largeScreen">
          <div>
            <div class="w-100"><strong>Дни курсирования:</strong></div>
            <div class="w-100"><span class="text-warning">{{ route.days }}</span></div>
          </div>
        </td>

        <td class="col-4 smallScreen">
          <div>
            <p class="text-primary">{{ route.thread.title }} ({{ route.thread.number }})</p>
            <p><strong>Перевозчик:</strong> <span class="text-info">{{ route.thread.carrier.title }}</span></p>
            <p><strong>Тип транспорта:</strong> <span class="text-muted">{{ translate(route.thread.transport_type) }}</span></p>
          </div>
        </td>
        <td class="col-1 smallScreen" >
          <div>
            <div class="w-100"><strong>Отправление поезда:</strong></div>
            <div class="w-100"><span class="text-success">{{ formatDate(route.departure) }}</span></div>
            <div class="w-100"><strong>Прибытие поезда:</strong></div>
            <div class="w-100"><span class="text-success">{{ formatDate(route.arrival) }}</span></div>
            <div class="w-100"><strong>Дни курсирования:</strong></div>
            <div class="w-100"><span class="text-warning">{{ route.days }}</span></div>
          </div>
        </td>
      </tr>
      </tbody>
   </table>
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

@media only screen and (max-width: 960px) {
        .largeScreen {display: none;}

   }
 /* On larger resolutions, hide the text for Small screens */
@media only screen and (min-width: 960px) {
    .smallScreen {display: none;}
}
</style>