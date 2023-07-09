<template>
    <div class="bg-[#1f2833] h-screen flex">
        <aside class="w-1/4 bg-gray-900 p-4">
            <div class="flex flex-col mb-4 space-y-4 mx-8">
                <a href="/" class="flex"><img src="~/assets/banner.png" alt="logo" class="mx-auto h-20 w-auto"></a>
                <a href="#" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información General</a>
                <a href="/dashboard/details" class="tracking-wider uppercase text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Información Detallada</a>
                <h1 class="text-white">Desde:</h1>
                <VueDatePicker v-model="dateIni" placeholder="Comienzo del periodo" model-date="dd.MM.yyyy" :enable-time-picker="false" locale="es"/>
                <h1 class="text-white">Hasta:</h1>
                <VueDatePicker v-model="dateFin" placeholder="Fin del periodo" model-date="dd.MM.yyyy" :enable-time-picker="false" locale="es"/>
                <div class="flex items-center space-x-5">
                    <a v-on:click="console.log('sdfsd')" class="tracking-wider text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Filtrar</a>
                    <a v-on:click="limpiar_filtro" class="tracking-wider text-center bg-gray-800 ring-2 ring-[#66fcf1] text-white px-4 py-2 mb-2 font-bold hover:bg-gray-700 rounded-full">Limpiar filtro</a>
                </div>
            </div>
        </aside>
        
        <main class="flex-grow bg-space p-4 flex items-center justify-center w-max">
            <!-- Contenido principal -->
            <div class="grid grid-cols-3 gap-3 w-full max-w-screen-lg mx-auto">
                <h1 class="text-3xl leading-tight text-white font-bold mb-4 text-center col-span-3">Información general promedio del período</h1>
    <!-- Tarjetas 1-8 -->
                <!-- Tarjetas 1-6 -->
                <div v-for="(tarjeta,index) in tarjetas" :key="index" :class="{'border-green-500': !tarjeta.estado,'border-red-500': tarjeta.estado}" class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full p-5 py-6 bg-white rounded-md shadow-xl border-l-[5px] border-blue-300'>
		            <div class="text-center">
                        <div class="font-bold text-gray-800 text-5xl">{{tarjeta.valor}}</div>
                        <div class="font-bold text-gray-800 text-base">{{tarjeta.nombre}}</div>
                        <div class="font-bold text-gray-800 text-sm">{{ tarjeta.estado ? 'Potencialmente Peligrosos' : 'Inofensivos' }}</div>
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
                {nombre: 'Total', valor: 0, estado: false},
                {nombre: 'Velocidad', valor: 0, estado: false},
                {nombre: 'Tamaño', valor: 0, estado: false},
                {nombre: 'Total', valor: 0, estado: true},
                {nombre: 'Velocidad', valor: 0, estado: true},
                {nombre: 'Tamaño', valor: 0, estado: true},
            ]
        }
    },
    computed:{

    },
    methods:{
        limpiar_filtro() {
            this.dateIni = '';
            this.dateFin = '';
        },
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