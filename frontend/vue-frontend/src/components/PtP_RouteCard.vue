
<template>
      <h2 class="title">{{ route.thread.title }}</h2>
      <div class="route-card">
        <p><strong>Отправление:</strong> {{ formatDate(route.departure) }} ({{ route.from.title }})</p>
        <p><strong>Прибытие:</strong> {{ formatDate(route.arrival) }} ({{ route.to.title }})</p>
        <p><strong>Тип транспорта:</strong> {{ translate(route.thread.transport_type) }}</p>
        <p><strong>Номер рейса:</strong> {{ route.thread.number }}</p>
        <p><strong>Длительность:</strong> {{ formatDuration(route.duration) }}</p>
        <p><strong>Пересадки:</strong> {{ route.has_transfers ? 'Да' : 'Нет' }}</p>
        <div v-if="route.tickets_info">
          <h4>Информация о билетах:</h4>
          <ul>
            <li v-for="ticket in route.tickets_info.places" :key="ticket.name">
              {{ ticket.price.whole }}.{{ ticket.price.cents }} ₽
            </li>
          </ul>
        </div>
        <p><strong>Остановки:</strong> {{ route.stops || 'Нет остановок по пути' }}</p>
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