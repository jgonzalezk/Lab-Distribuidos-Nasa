<template>
    <div class="background-image">
        
    </div>
</template>

<style>
.background-image::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    backdrop-filter: brightness(60%) blur(1.8px);
    -webkit-backdrop-filter: brightness(60%) blur(1.8px);
    pointer-events: none;
}
.background-image {
    background-image: url("~/static/bg-astronaut.png");
    background-size: cover;
    background-position: center;
    height: 100vh;
}
</style>