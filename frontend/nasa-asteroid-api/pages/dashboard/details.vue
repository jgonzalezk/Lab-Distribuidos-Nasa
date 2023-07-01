<template>
  <div class="flex h-screen">
    <aside class="w-1/4 bg-gray-900 p-4">
      <div class="flex flex-col mb-4 space-y-4 mx-8">
        <a href="/" class="flex"><img src="~/assets/banner.png" alt="logo" class="mx-auto h-20 w-auto"></a>
        <a href="/dashboard"
          class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información
          General</a>
        <a href="#" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información Detallada</a>
        <h1 class="text-white">Desde</h1>
        <VueDatePicker v-model="dateIni" placeholder="Comienzo del periodo" model-date="dd.MM.yyyy"
          :enable-time-picker="false" locale="es" />
        <h1 class="text-white">Hasta</h1>
        <VueDatePicker v-model="dateFin" placeholder="Comienzo del periodo" model-date="dd.MM.yyyy"
          :enable-time-picker="false" locale="es" />
      </div>
    </aside>
    <main class="flex-grow bg-gray-100 p-4">
      <!-- Contenido principal -->
      <div class="grid grid-cols-2 gap-4 justify-center">
        <div class="bg-white p-4">Tarjeta 1</div>
        <div class="bg-white p-4">Tarjeta 2</div>
        <div class="bg-white p-4">Tarjeta 3</div>
        <div class="bg-white p-4">Tarjeta 4</div>
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
      tarjetas: [
        { nombre: 'Asteroides', valor: 0 },
        { nombre: 'Cometas', valor: 0 },
        { nombre: 'Meteoritos', valor: 0 },
        { nombre: 'Meteoros', valor: 0 },
        { nombre: 'Meteoroides', valor: 0 },
        { nombre: 'Satélites', valor: 0 },
        { nombre: 'Estrellas fugaces', valor: 0 },
        { nombre: 'Estrellas', valor: 0 },
      ]
    }
  },
  computed: {

  },
  methods: {
  },
  async mounted() {
    const response = await axios.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY');
    console.log(response.data);
  }
}
</script>

<style scoped>
.uwu {
  overflow: auto hidden;
}

.bg-dashboard {
  background: radial-gradient(circle, #1f2833 0%, rgba(0, 0, 0, 0.5) 100%)
}</style>