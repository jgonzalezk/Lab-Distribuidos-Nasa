<template>
    <div class="bg-[#1f2833] h-screen flex flex-col">
        <Nav></Nav>
        <div class="flex h-full">
            <div class="w-1/5 flex flex-wrap container justify-center">
                <!-- Contenido de la columna izquierda -->
                <div class="flex flex-wrap flex-col w-full">
                    <h1 class="text-4xl text-center font-bold text-white leading-tight">Seleccione la fecha</h1>
                    <VueDatePicker class="flex" v-model="date" placeholder="Comienzo del periodo" model-date="dd.MM.yyyy" :enable-time-picker="false" locale="es"/>
                </div>
                <div class="flex flex-wrap flex-col w-full">
                    <h1 class="text-4xl text-center font-bold text-white leading-tight">Seleccione la fecha</h1>
                    <VueDatePicker class="flex" v-model="date" placeholder="Comienzo del periodo" model-date="dd.MM.yyyy" :enable-time-picker="false" locale="es"/>
                </div>


            </div>
            <div class="w-4/5 flex flex-wrap container content-center bg-dashboard">
                <!-- Contenido de la columna derecha -->
                <div class="flex flex-wrap sm:flex-nowrap container items-center justify-center content-center space-x-8 my-4 mx-20">
                    <div class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full sm:w-1/4 p-5 bg-white rounded-md shadow-xl border-l-8 border-[#00a1e0]'>
		                <div class="flex justify-between w-full">
			                <div>
				                <div class="p-2">
					                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
						            <path stroke-linecap="round" stroke-linejoin="round"
							            d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" />
					                </svg>
				                </div>
			                </div>
		                </div>
		                <div>
                            <div class="font-bold text-5xl text-center">
                                4
                            </div>
                            <div class="font-bold text-sm">
                                Total Asteroides
                            </div>
		                </div>
	                </div> 
                    <!-- 2 -->
                    <div class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full sm:w-1/4 p-5 bg-white rounded-md shadow-xl border-l-4 border-blue-300'>
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
                            <div class="font-bold text-5xl">
                                4
                            </div>
                            <div class="font-bold text-sm">
                                Total
                            </div>
		                </div>
	                </div>
                    <!-- 3 -->
                    <div class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full sm:w-1/4 p-5 bg-white rounded-md shadow-xl border-l-4 border-blue-300'>
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
                            <div class="font-bold text-5xl">
                                4
                            </div>
                            <div class="font-bold text-sm">
                                Total
                            </div>
		                </div>
	                </div>
                    <!-- 4 -->
                    <div class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full sm:w-1/4 p-5 bg-white rounded-md shadow-xl border-l-4 border-blue-300'>
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
                            <div class="font-bold text-5xl">
                                4
                            </div>
                            <div class="font-bold text-sm">
                                Total
                            </div>
		                </div>
	                </div>
                </div>





                <div class="flex flex-wrap sm:flex-nowrap container items-center justify-center content-center space-x-8 my-4 mx-20">
                    <div class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full sm:w-1/4 p-5 bg-white rounded-md shadow-xl border-l-4 border-blue-300'>
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
                            <div class="font-bold text-5xl">
                                4
                            </div>
                            <div class="font-bold text-sm">
                                Total
                            </div>
		                </div>
	                </div> 
                    <!-- 2 -->
                    <div class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full sm:w-1/4 p-5 bg-white rounded-md shadow-xl border-l-4 border-blue-300'>
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
                            <div class="font-bold text-5xl">
                                4
                            </div>
                            <div class="font-bold text-sm">
                                Total
                            </div>
		                </div>
	                </div>
                    <!-- 3 -->
                    <div class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full sm:w-1/4 p-5 bg-white rounded-md shadow-xl border-l-4 border-blue-300'>
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
                            <div class="font-bold text-5xl">
                                4
                            </div>
                            <div class="font-bold text-sm">
                                Total
                            </div>
		                </div>
	                </div>
                    <!-- 4 -->
                    <div class='flex flex-wrap flex-row sm:flex-col justify-center items-center w-full sm:w-1/4 p-5 bg-white rounded-md shadow-xl border-l-4 border-blue-300'>
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
                            <div class="font-bold text-5xl">
                                4
                            </div>
                            <div class="font-bold text-sm">
                                Total
                            </div>
		                </div>
	                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

const date = ref();

export default {
    components: {
        VueDatePicker
    },
    setup() {
        return {
            date
        }
    }
}
</script>

<style scoped>
.bg-dashboard{
    background: radial-gradient(circle, #1f2833 0%, rgba(0,0,0,0.5) 100%)
}
</style>