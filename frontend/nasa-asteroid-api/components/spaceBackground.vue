<template>
    <div class="absolute inset-0" ref="particles"></div>
  </template>
  
  <script>
  import particlesJS from 'vue3-particles';
  
  export default {
    mounted() {
      particlesJS.load('particles', '../assets/particles.json');
    },
  };
  </script>
  
  <style>
  .particles-js-canvas-el {
    position: absolute;
    width: 100% !important;
    height: 100% !important;
  }
  </style>
  