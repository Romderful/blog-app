<template>

    <div>

        <Navbar />

        <div @click="addToFavourites"
            class="article p-6 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
            style="position: relative;">
            <div v-if="currentUser" style="position: absolute; right: -0.5rem; top: -0.5rem;">
                <svg :fill="isFavourite ? 'red' : 'currentColor'" xmlns="http://www.w3.org/2000/svg" width="22"
                    height="22" class="bi bi-heart-fill" viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z" />
                </svg>
            </div>
            <div>
                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{ articleData.article_content }}</p>
            </div>
            <div>
                <i style="font-size: small;">This article has been liked {{ numberOfLikes }} times</i>
            </div>
        </div>

    </div>

</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";
import Navbar from "../../components/navbar.vue";

export default Vue.extend({
    name: 'DetailPage',
    components: {
        Navbar,
    },

    data() {
        return {
            currentUser: localStorage.getItem("username"),
            articleData: [],
            numberOfLikes: 0,
            isFavourite: false,
        }
    },

    methods: {
        async getArticleData() {
            const response = await axios.get(`http://127.0.0.1:8000/api-v1/article/${this.$route.params.id}/`);
            this.articleData = response.data;
        },


        async addToFavourites() {
            const response = await axios.get(`http://127.0.0.1:8000/api-v1/favourite/?user=${localStorage.getItem("pk")}&article=${this.$route.params.id}`);
            if (response.data.length === 0) {
                await axios.post("http://127.0.0.1:8000/api-v1/favourite/", {
                    user: localStorage.getItem("username"),
                    article: this.$route.params.id,
                });
                this.numberOfLikes++;
                this.isFavourite = true;
            } else {
                await axios.delete(`http://127.0.0.1:8000/api-v1/favourite/${response.data[0].id}/`);
                this.numberOfLikes--;
                this.isFavourite = false;
            }
        },

        async isInFavourites() {
            const response = await axios.get(`http://127.0.0.1:8000/api-v1/favourite/?user=${localStorage.getItem("pk")}&article=${this.$route.params.id}`);
            if (response.data.length === 0) {
                this.isFavourite = false;
            } else {
                this.isFavourite = true;
            }
        },

        async getNumberOfLikes() {
            const response = await axios.get(`http://127.0.0.1:8000/api-v1/favourite/?article=${this.$route.params.id}`);
            this.numberOfLikes = response.data.length;
        },

    },

    async created() {
        await this.isInFavourites();
        await this.getArticleData();
        await this.getNumberOfLikes();
    },

})
</script>