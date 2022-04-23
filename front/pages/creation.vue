<template>

    <div>

        <Navbar />

        <form @submit.prevent="createArticle">
            <div class="mb-6">
                <input type="text" id="base-input" v-model="title"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Article's title">
            </div>
            <div>
                <textarea id="message" v-model="articleContent" rows="4"
                    class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 height:20rem"
                    placeholder="Write your content..."></textarea>
            </div>
            <div style="text-align: center;">
                <button type="submit"
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Create
                    article!</button>
            </div>
        </form>

    </div>

</template>

<script lang="ts">

import Vue from "vue";
import axios from "axios";
import Navbar from "../components/navbar.vue";

export default Vue.extend({
    name: 'CreationPage',
    components: {
        Navbar,
    },

    data() {
        return {
            title: "",
            articleContent: "",
        }
    },

    methods: {
        async createArticle() {
            await axios.post('http://localhost:8000/api-v1/article/', {
                author: localStorage.getItem("username"),
                title: this.title,
                article_content: this.articleContent,
            }, { headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` } })
            this.$router.push("/");
        },
    },

})
</script>

<style>
input {
    max-width: 70%;
    margin: auto;
}

textarea {
    max-width: 70%;
    margin: auto;
    margin-bottom: 2rem;
    height: 20rem;
}
</style>