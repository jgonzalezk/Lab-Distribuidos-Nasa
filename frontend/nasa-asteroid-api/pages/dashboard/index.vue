<template>
    <div class="bg-[#1f2833] h-screen flex">
        <aside class="w-1/4 bg-gray-900 p-4">
            <div class="flex flex-col mb-4 space-y-4 mx-8">
                <a href="/" class="flex"><img src="~/assets/banner.png" alt="logo" class="mx-auto h-20 w-auto"></a>
                <a href="#" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información General</a>
                <a href="/dashboard/details" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información Detallada</a>
                <h1 class="text-white">Desde</h1>
                <VueDatePicker v-model="dateIni" placeholder="Comienzo del periodo" model-date="dd.MM.yyyy" :enable-time-picker="false" locale="es"/>
                <h1 class="text-white">Hasta</h1>
                <VueDatePicker v-model="dateFin" placeholder="Comienzo del periodo" model-date="dd.MM.yyyy" :enable-time-picker="false" locale="es"/>
                <div class="flex items-center">
                    <a v-on:click="console.log('sdfsd')" class="tracking-wider text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Filtrar</a>
                    <a v-on:click="console.log('sdfsd')" class="tracking-wider text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Limpiar filtro</a>
                </div>
            </div>
        </aside>

        <main class="flex-grow bg-space p-4">
            <!-- Contenido principal -->
            <div class="grid grid-cols-4 gap-4 justify-center">
                <!-- Tarjetas 1-8 -->
                <div v-for="(tarjeta,index) in tarjetas" :key="index" class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full p-5 bg-white rounded-md shadow-xl border-l-4 border-blue-300'>
		            <div class="flex justify-between w-full">
			            <div>
				            <div class="p-2">
					            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
						        <path stroke-linecap="round" stroke-linejoin="round"
							        d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" />
					            </svg>
				            </div>
			            </div>
                        <div>
                            <div style="padding-top: 0.1em; padding-bottom: 0.1rem" class="flex items-center text-xs px-3 bg-blue-200 text-blue-800 rounded-full">100%</div>
                        </div>
		            </div>
		            <div>
                        <div class="font-bold text-5xl">{{tarjeta.valor}}</div>
                        <div class="font-bold text-sm">{{tarjeta.nombre}}</div>
		            </div>
	            </div>
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
    data(){
        return{
            tarjetas: [
                {nombre: 'Asteroides', valor: 0},
                {nombre: 'Cometas', valor: 0},
                {nombre: 'Meteoritos', valor: 0},
                {nombre: 'Meteoros', valor: 0},
                {nombre: 'Meteoroides', valor: 0},
                {nombre: 'Satélites', valor: 0},
                {nombre: 'Estrellas fugaces', valor: 0},
                {nombre: 'Estrellas', valor: 0},
            ]
        }
    },
    computed:{

    },
    methods:{
    },
    async mounted(){
        const response = await axios.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY');
        console.log(response.data);
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