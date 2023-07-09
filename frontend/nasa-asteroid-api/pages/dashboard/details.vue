<template>
  <div class="flex h-screen">
    <aside class="w-1/4 bg-gray-900 p-4">
      <div class="flex flex-col mb-4 space-y-4 mx-8">
        <a href="/" class="flex"><img src="~/assets/banner.png" alt="logo" class="mx-auto h-20 w-auto"></a>
        <div class="py-2"></div>
        <a href="/dashboard" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información General</a>
        <a href="#" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información Detallada</a>
        <div class="py-1"></div>
        <h1 class="text-white">Desde:</h1>
        <VueDatePicker v-model="dateIni" placeholder="Comienzo del periodo" model-type="yyyy-MM-dd" :enable-time-picker="false" locale="es" />
        <h1 class="text-white">Hasta:</h1>
        <VueDatePicker v-model="dateFin" placeholder="Fin del periodo" model-type="yyyy-MM-dd" :enable-time-picker="false" locale="es" />
        <div class="flex items-center space-x-5">
          <a v-on:click="filtrar" class="tracking-wider text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Filtrar</a>
          <a v-on:click="limpiar_filtro" class="tracking-wider text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Limpiar filtro</a>
        </div>
      </div>
    </aside>
    <main class="flex-grow p-4 bg-space">
      <!-- Contenido principal -->
      <div class="overflow-y-auto max-h-full">
        <ul class="space-y-4 mr-4">
          <li v-for="(item, index) in itemList" :key="index" class="bg-white p-4 py-5 mx-auto rounded-lg flex flex-row">
            <div class="grid grid-cols-3 gap-4 flex-grow mr-48">
              <div>
                <h1 class="text-lg font-bold">{{ item.Name }}</h1>
                <p><strong>Diametro estimado:</strong> {{ ((item.Estimated_diameter_met_max+item.Estimated_diameter_met_min)/2).toFixed(2).replace('.', ',') }} m</p>
              </div>
              <div>
                <p><strong>UUID:</strong> {{ item.ID }}</p>
                <p><strong>Velocidad relativa:</strong> {{ parseFloat(item.Relative_velocity_KpS).toFixed(2).replace('.', ',') }} km/s</p>
              </div>
              <div>
                <span class="bg-[#6AD9D1] text-[#2C5956] rounded-3xl px-3 font-bold">{{ new Date(item.Date).toLocaleDateString('es-ES').replace(/\//g, '-') }}</span>
                <p><strong>Cuerpo que Orbita:</strong> {{ item.Orbiting_body }}</p>
              </div>
            </div>
            <div class="flex items-center relative">
              <div class="w-8 h-8 rounded-full" :class="[ !item.Is_potentially_hazardous_asteroid ? 'bg-green-500' : 'bg-red-500']"
                @mouseover="item.hovered = true"
                @mouseleave="item.hovered = false"
              ></div>
              <span v-if="item.hovered" class="absolute right-10 -ml-40 bg-gray-800 text-white px-2 py-1 rounded">
                {{ !item.Is_potentially_hazardous_asteroid ? 'No es potencialmente peligroso' : 'Potencialmente peligroso' }}
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
      ]
    }
  },
  computed: {

  },
  methods: {
    limpiar_filtro() {
      this.dateIni = '';
      this.dateFin = '';
      this.itemList= []
    },

    async filtrar() {
      const axiosInstance = axios.create({
        headers: {
          "Access-Control-Allow-Origin": "*"
        }
      });
      let response = await axiosInstance.get("http://localhost:8080/total/"+ this.dateIni + "/"+ this.dateFin);
      console.log(response);
      this.itemList = response.data;     
      
    }
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