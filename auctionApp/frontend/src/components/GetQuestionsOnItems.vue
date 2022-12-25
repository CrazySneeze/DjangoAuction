<!-- Gets all questions asked about a given item -->
<script lang="ts">
import Answer from './Answer.vue';
import GetItem from './getItem.vue';
var _getResult: [{question: [{question: string}],answer: string, id: number}]
    export default {
    props: ["userId"],
    data() {
        return {
            getResult: _getResult,
        };
    },
    methods: {

        async getQuestionsAskedToUser() {
            try {
                const res = await fetch(`https://group43-web-apps-ec19115.apps.d.comp-teach.qmul.ac.uk/api/getQuestionsAskedToUser/${this.userId}`, { method: "get",
                        'credentials': "include", });
                if (!res.ok) {
                    const message = `An error has occured: ${res.status} - ${res.statusText}`;
                    throw new Error(message);
                }
                const data = await res.json();
                if (data.ObjectsFound){
                    delete data.ObjectsFound;
                    this.getResult = data;
                }
            }
            catch (err) {
                console.error(err);
            }
        },
    },
    created() {
        this.getQuestionsAskedToUser();
    },
    components: { Answer, GetItem }
}
</script>


<template>
  <header>
    <div class="">
        <h1>Questions asked about your items</h1>
        <div v-if="getResult" class="alert alert-secondary mt-2" role="alert">
            <div class="row" v-for="item in getResult">
                <div class="col-sm-12 text-center">
                    <div class="row" v-for="question in item.question">
                        <b class = "w-25 p-3">{{ question.question}}</b>
                    </div>
                </div>
                <div class="col-sm-12 text-center">
                    <b v-if="item.answer" class = "w-25 p-3">{{ item.answer }}</b>
                    <b v-else><Answer v-bind:questionId="item.id"/></b>
                </div>
            </div>
        </div>
        <div v-else>
            <b>You haven't been asked any questions about items you've listed</b>
        </div>
      </div>
  </header>
</template>