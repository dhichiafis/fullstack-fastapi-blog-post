<script setup>
import {RouterLink} from 'vue-router'

</script>
<template>
   <div>
    <header class="py-12 flex flex-row px-8 justify-between ">
        <div>
            <RouterLink to="/" class="hover:bg-gray-900 hover:text-white">home</RouterLink>

        </div>
        <div>
            <RouterLink to="/login" class="bg-gray-900 text-white py-2 px-4 rounded-md ">Login</RouterLink>
        </div>

    </header>
    <main>
        <slot></slot>
    </main>
    <footer>

    </footer>
   </div>
</template>