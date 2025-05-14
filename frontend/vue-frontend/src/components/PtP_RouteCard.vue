
<template>
  <div class="card mb-3 w-100">
    <table  class="table table-bordered mb-0">
      <tbody>
        <tr class="largeScreen">
          <td class="col-4">
            <h3 class="card-title text-primary">{{ route.thread.title }}</h3>
            <p><strong >Номер рейса:</strong> <span class="text-info">{{ route.thread.number }}</span></p>
            <p><strong>Тип транспорта:</strong> <span class="text-muted">{{ translate(route.thread.transport_type) }}</span></p>
          </td>
          <td class="col-2">
            <div>
            <div class="w-100"><strong>Отправление поезда:</strong></div>
            <div class="w-100"><span class="text-success">{{ formatDate(route.departure) }} ({{route.from.title}})</span></div>
          </div>
          </td>
          <td class="col-2">
            <div>
            <div class="w-100"><strong>Прибытие поезда:</strong></div>
            <div class="w-100"><span class="text-success">{{ formatDate(route.arrival) }} ({{ route.to.title }})</span></div>
          </div>
          </td>
          <td class="col-2">
            <div>
              <div><strong>Длительность:</strong></div> <div><span class="text-warning">{{ formatDuration(route.duration) }}</span></div>
              <p><strong>Пересадки:</strong> <span class="text-warning">{{ route.has_transfers ? 'Да' : 'Нет' }}</span></p>
            </div>
          </td>
          <td class="col-2">
            <div v-if="route.tickets_info">
              <h4 class="card-title text-primary">Информация о билетах:</h4>
              <ul>
                <li v-for="ticket in route.tickets_info.places" :key="ticket.name">
                  {{ ticket.price.whole }}.{{ ticket.price.cents }} ₽
                </li>
              </ul>
            </div>
          </td>
        </tr>

      <tr class="smallScreen">
          <td class="col-1">
            <p class="text-primary">{{ route.thread.title }}</p>
            <div><strong >Номер рейса:</strong> <span class="text-info">{{ route.thread.number }}</span></div>
            <div><strong>Тип транспорта:</strong> <span class="text-muted">{{ translate(route.thread.transport_type) }}</span></div>
            <div v-if="route.tickets_info">
              <p class=" text-primary">Информация о билетах:</p>
              <ul>
                <li v-for="ticket in route.tickets_info.places" :key="ticket.name">
                  {{ ticket.price.whole }}.{{ ticket.price.cents }} ₽
                </li>
              </ul>
            </div>
          </td>
          <td class="col-1">
            <div>
              <div class="w-100"><strong>Отправление поезда:</strong></div>
              <div class="w-100"><span class="text-success">{{ formatDate(route.departure) }} ({{route.from.title}})</span></div>
              <div class="w-100"><strong>Прибытие поезда:</strong></div>
              <div class="w-100"><span class="text-success">{{ formatDate(route.arrival) }} ({{ route.to.title }})</span></div>
              <div><strong>Длительность:</strong></div> <div><span class="text-warning">{{ formatDuration(route.duration) }}</span></div>
              <div><strong>Пересадки:</strong> <span class="text-warning">{{ route.has_transfers ? 'Да' : 'Нет' }}</span></div>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'PtP_RouteCard',
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
    },
    formatDuration(duration) {
      const hours = Math.floor(duration / 3600);
      const minutes = Math.floor((duration % 3600) / 60);
      return `${hours}ч ${minutes}мин`;
    },
  }
}
</script>

<style scoped>
@media only screen and (max-width: 960px) {
        .largeScreen {display: none;}
   }
 /* On larger resolutions, hide the text for Small screens */
@media only screen and (min-width: 960px) {
    .smallScreen {display: none;}
}
</style>