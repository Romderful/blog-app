<template>

    <nav class="bg-white border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-800">
        <div class="container flex flex-wrap justify-between items-center mx-auto">
            <a href="/" class="flex items-center">
                <NuxtLink v-if="this.$route.name == 'index'" to="/login"
                    class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">
                    Authentication</NuxtLink>
                <NuxtLink v-else to="/" class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">
                    Blog-app</NuxtLink>
            </a>
            <div>
                <b v-if="currentUser" style="margin-right: 1.5rem;">{{ currentUser }}</b>
                <a href="/" @click="logOutUser" v-if="currentUser">Logout</a>
            </div>
        </div>
    </nav>

</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
    name: 'Navbar',

    data() {
        return {
            currentUser: localStorage.getItem("username"),
        }
    },

    methods: {
        logOutUser() {
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            localStorage.removeItem("username");
        }
    },

})
</script>

<style>
nav {
    margin-bottom: 5rem;
}
</style>