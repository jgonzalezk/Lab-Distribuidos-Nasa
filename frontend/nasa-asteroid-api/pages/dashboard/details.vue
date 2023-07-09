<template>
  <div class="flex h-screen">
    <aside class="w-1/4 bg-gray-900 p-4">
      <div class="flex flex-col mb-4 space-y-4 mx-8">
        <a href="/" class="flex"><img src="~/assets/banner.png" alt="logo" class="mx-auto h-20 w-auto"></a>
        <a href="/dashboard" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información General</a>
        <a href="#" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información Detallada</a>
        <h1 class="text-white">Desde:</h1>
        <VueDatePicker v-model="dateIni" placeholder="Comienzo del periodo" model-date="dd.MM.yyyy" :enable-time-picker="false" locale="es" />
        <h1 class="text-white">Hasta:</h1>
        <VueDatePicker v-model="dateFin" placeholder="Fin del periodo" model-date="dd.MM.yyyy" :enable-time-picker="false" locale="es" />
        <div class="flex items-center space-x-5">
          <a v-on:click="console.log('sdfsd')" class="tracking-wider text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Filtrar</a>
          <a v-on:click="limpiar_filtro" class="tracking-wider text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Limpiar filtro</a>
        </div>
      </div>
    </aside>
    <main class="flex-grow p-4 bg-space">
      <!-- Contenido principal -->
      <div class="overflow-y-auto max-h-full">
        <ul class="space-y-4">
          <li v-for="(item, index) in itemList" :key="index" class="bg-white p-4 py-5 rounded-lg flex flex-row">
            <div class="grid grid-cols-3 gap-4 flex-grow mr-48">
              <div>
                <h1 class="text-lg font-bold">{{ item.name }}</h1>
                <p><strong>Diametro estimado:</strong> {{ item.diameter }}</p>
              </div>
              <div>
                <p><strong>UUID:</strong> {{ item.id }}</p>
                <p><strong>Velocidad relativa:</strong> {{ item.velocity }}</p>
              </div>
              <div>
                <span class="bg-[#6AD9D1] text-[#2C5956] rounded-3xl px-3 font-bold">{{ item.date }}</span>
                <p><strong>Cuerpo que Orbita:</strong> {{ item.orbit }}</p>
              </div>
            </div>
            <div class="flex items-center relative">
              <div class="w-8 h-8 rounded-full" :class="[ item.status ? 'bg-green-500' : 'bg-red-500']"
                @mouseover="item.hovered = true"
                @mouseleave="item.hovered = false"
              ></div>
              <span v-if="item.hovered" class="absolute right-10 -ml-40 bg-gray-800 text-white px-2 py-1 rounded">
                {{ item.status ? 'No es potencialmente peligroso' : 'Potencialmente peligroso' }}
              </span>
            </div>
          </li>
        </ul>
      </div>
    </main>
  </div>
</template>
  
<script>
import axios from 'axios';
import { ref } from 'vue';
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

const dateIni = ref();
const dateFin = ref();


export default {
  components: {
    VueDatePicker,
  },
  setup() {
    return {
      dateIni,
      dateFin
    }
  },
  data() {
    return {
      itemList: [
        { name: 'Nombre 1', id: 12345, date: '2023-07-07', diameter: '10 km', velocity: '1000 km/h', weight: '1000 kg', orbit: 'Terrestre', status: true },
        { name: 'Nombre 2', id: 67890, date: '2023-07-08', diameter: '5 km', velocity: '500 km/h', weight: '500 kg', orbit: 'Lunar', status: false },
        // Agrega más elementos de la lista aquí si es necesario
      ]
    }
  },
  computed: {

  },
  methods: {
    limpiar_filtro() {
      this.dateIni = '';
      this.dateFin = '';
    },
  },
  async mounted() {
    // const response = await axios.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY');
    // console.log(response.data);
  }
}
</script>

<style scoped>
.bg-space {
  background-image: url('~/assets/bg-space.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>