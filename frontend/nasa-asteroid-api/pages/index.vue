<template>
    <div class="background-image">
        <!-- Crear una division responsive que tenga dos columnas, a la izquierda con texto y a la derecha nada -->
        <div class="flex h-screen justify-center container mx-auto px-10 py-8">
            <div class="flex flex-wrap -mx-4 content-center">
                <div class="w-full md:w-1/2 px-4">
                    <h1 class="text-4xl font-bold text-white leading-tight">Asteroids Near Earth</h1>
                    <!-- Quiero que el texto tenga solo el ancho de la columna, no toda la pantalla -->
                    <p class="text-xl break-normal text-gray-200 mt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit distinctio dolore velit repudiandae doloribus, eaque hic repellat ab, architecto accusantium, consectetur ex ipsa corrupti pariatur exercitationem esse iusto atque quos?</p>
                    <p class="text-xl break-normal text-gray-200 mt-4"> {{ counter.toLocaleString() }} Cercanos a la Tierra.</p>
                    <div class="mt-8">
                        <a href="dashboard" class="bg-white text-gray-800 font-bold rounded-full px-6 py-3 mr-1 shadow-lg uppercase tracking-wider hover:bg-gray-200">Free Trial</a>
                        <a href="#" class="bg-gray-800 text-white font-bold rounded-full px-6 py-3 ml-1 shadow-lg uppercase tracking-wider hover:bg-gray-700">Signup</a>
                    </div>
                </div>
                <div class="w-full md:w-1/2 px-4"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.background-image {
    background-size: cover;
    background-position: center;
    height: 100vh;
    z-index: 0;
}

.background-image::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("~/static/bg-astronaut.png");
    background-position: center;
    background-size: cover;
    z-index: -1;
    backdrop-filter: brightness(60%) blur(1.8px);
    -webkit-backdrop-filter: brightness(60%) blur(1.8px);
    pointer-events: none;
}

.background-image::after{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    backdrop-filter: brightness(60%) blur(1.8px);
    -webkit-backdrop-filter: brightness(60%) blur(1.8px);
    z-index: -1;
}
</style>

<script setup>
const counter = ref(578950)

setInterval(() => {
    if (counter.value < 600000) {
        counter.value += 50
    }
}, 13);


</script>