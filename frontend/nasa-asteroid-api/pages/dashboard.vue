<template>
    <div class="bg-[#1f2833] h-screen flex">
        <aside class="w-1/4 bg-gray-200 p-4">
            <div class="flex flex-col mb-4 space-y-10">
                <a href="/" class="flex">
                    <img src="../static/banner.png" alt="logo" class="mx-auto h-20 w-auto" href="/">
                </a>
                <!-- <img src="/path/to/logo.png" alt="Logo" class="mb-4" /> -->
                <button class="bg-blue-500 text-white px-4 py-2 mb-2">Botón 1</button>
                <button class="bg-blue-500 text-white px-4 py-2 mb-2">Botón 2</button>
                <input type="text" placeholder="Input 1" class="border p-2 mb-2" />
                <input type="text" placeholder="Input 2" class="border p-2 mb-2" />
        </div>
        </aside>
            <div class="w-4/5 flex flex-wrap container content-center bg-dashboard">
                <!-- Contenido de la columna derecha -->
                <Particles
            id="tsparticles"
            :particlesInit="particlesInit"
            :particlesLoaded="particlesLoaded"
            url="../assets/particles.json"
        />
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
</template>

<script>
import { ref } from 'vue';
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import Particles from "vue3-particles";

// declare module "vue3-particles";
import { loadFull } from "tsparticles";

const particlesInit = async engine => {
    await loadFull(engine);
};

const particlesLoaded = async container => {
    console.log("Particles container loaded", container);
};

const date = ref();

export default {
    components: {
        VueDatePicker,
        Particles
    },
    setup() {
        return {
            date
        }
    }
}
</script>

<style scoped>
.uwu{
    overflow: auto hidden;
}
.bg-dashboard{
    background: radial-gradient(circle, #1f2833 0%, rgba(0,0,0,0.5) 100%)
}
</style>