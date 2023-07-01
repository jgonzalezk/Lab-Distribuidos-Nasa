<template>
    <div class="flex h-screen">
      <aside class="w-1/4 bg-gray-200 p-4">
        <!-- Contenido de la barra lateral -->
        <div class="flex flex-col mb-4">
          <img src="/path/to/logo.png" alt="Logo" class="mb-4" />
          <button class="bg-blue-500 text-white px-4 py-2 mb-2">Botón 1</button>
          <button class="bg-blue-500 text-white px-4 py-2 mb-2">Botón 2</button>
          <input type="text" placeholder="Input 1" class="border p-2 mb-2" />
          <input type="text" placeholder="Input 2" class="border p-2 mb-2" />
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
  
  <style>
  html,
  body {
    overflow: hidden;
  }
  </style>