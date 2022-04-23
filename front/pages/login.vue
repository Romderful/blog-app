<template>

    <div>

        <Navbar />

        <div class="login-form">
            <form @submit.prevent="loginUser" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
                        Username
                    </label>
                    <input
                        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        id="username" type="text" placeholder="Username" v-model="username">
                </div>
                <div class="mb-6">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                        Password
                    </label>
                    <input
                        class="shadow appearance-none border border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                        id="password" type="password" placeholder="******************" v-model="password">
                </div>
                <div class="flex items-center justify-between">
                    <button
                        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        type="submit">
                        Sign In
                    </button>
                </div>
            </form>
        </div>

    </div>

</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";
import Navbar from "../components/navbar.vue";

export default Vue.extend({
    name: 'LoginPage',
    components: {
        Navbar,
    },

    data() {
        return {
            username: "",
            password: "",
        }
    },

    methods: {
        async loginUser() {
            const response = await axios.post("http://127.0.0.1:8000/api-v1/auth/login/", {
                username: this.username,
                password: this.password,
            });
            localStorage.setItem("access_token", response.data.access_token);
            localStorage.setItem("refresh_token", response.data.refresh_token);
            localStorage.setItem("username", response.data.user.username);
            localStorage.setItem("pk", response.data.user.pk);
            this.$router.push("/");
        },
    },

})
</script>

<style>
.login-form {
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
}
</style>