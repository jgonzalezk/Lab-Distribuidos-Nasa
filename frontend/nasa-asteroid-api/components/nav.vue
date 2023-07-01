<template>
    <div class="bg-[#0b0c10]">
        <nav class="mx-auto flex max-w items-center justify-between p-3 lg:px-8" aria-label="Global">
            <div class="flex lg:flex-1">
                <a href="/" class="-m-1.5 p-1.5">
                    <span class="sr-only">Steen Space</span>
                    <img class="h-14 w-auto" src="../static/logo.png" alt="" />
                </a>
            </div>
            <div class="flex lg:hidden">
                <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-[#66fcf1]"
                    @click="mobileMenuOpen = true">
                    <span class="sr-only">Abrir menu principal</span>
                    <Bars3Icon class="h-6 w-6" aria-hidden="true" />
                </button>
            </div>
            <div class="hidden lg:flex lg:flex-1 lg:justify-end">
                <a href="#" class="text-sm font-semibold leading-6 text-[#66fcf1]">Log in <span
                        aria-hidden="true">&rarr;</span></a>
            </div>
        </nav>
    </div>
</template>

<script setup>
// import { ref } from 'vue'
import { Bars3Icon } from '@heroicons/vue/24/outline'
const mobileMenuOpen = ref(false)
</script>