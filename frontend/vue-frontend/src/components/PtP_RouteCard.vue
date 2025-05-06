
<template>
  <div class="card mb-3 shadow-sm w-100">
    <table  class="table table-bordered">
      <tbody>
        <tr>
          <td class="w-40">
            <h3 class="card-title text-primary">{{ route.thread.title }}</h3>
            <p><strong>Номер рейса:</strong> <span class="text-info">{{ route.thread.number }}</span></p>
            <p><strong>Тип транспорта:</strong> <span class="text-muted">{{ translate(route.thread.transport_type) }}</span></p>
          </td>
          <td class="w-15">
            <p><strong>Отправление:</strong> <span class="text-success">{{ formatDate(route.departure) }} ({{ route.from.title }})</span></p>
          </td>
          <td class="w-15">
            <p><strong>Прибытие:</strong> <span class="text-success">{{ formatDate(route.arrival) }} ({{ route.to.title }})</span></p>
          </td>
          <td class="w-15">
            <p><strong>Длительность:</strong> <span class="text-warning">{{ formatDuration(route.duration) }}</span></p>
            <p><strong>Пересадки:</strong> <span class="text-warning">{{ route.has_transfers ? 'Да' : 'Нет' }}</span></p>
          </td>
          <td class="w-15">
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

</style>