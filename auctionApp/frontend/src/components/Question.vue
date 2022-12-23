<!-- Gets all the questions about a given item and then contains the answer and post question vues. -->
<script lang="ts">
import Answer from './Answer.vue';
import PostQuestion from './postQuestion.vue';
var _getResult: {answer: [{question: string, answer: string, id: number},], isOwner: boolean}
export default {
    props: ["itemId"],
    data() {
        return {
            getResult: _getResult,
        };
    },
    methods: {
        async getQuestion() {
            try {
                const res = await fetch(`https://group43-web-apps-ec19115.apps.d.comp-teach.qmul.ac.uk/getQuestion/${this.itemId}`, { method: "get" ,
                            'credentials': "include",});
                if (!res.ok) {
                    const message = `An error has occured: ${res.status} - ${res.statusText}`;
                    throw new Error(message);
                }
                const data = await res.json();
                this.getResult = data;
                console.log(data.answer[0]);
            }
            catch (err) {
                console.error(err);
            }
        },
    },
    created() {
        this.getQuestion();
    },
    components: { Answer, PostQuestion }
}
</script>


<template>
  <header>
    <div class="">
        <div v-if="getResult" class="alert alert-secondary mt-2" role="alert">
            <ul v-for="question in getResult.answer">
                <li>
                    <b class = "w-25 p-3">{{ question.question }}</b>
                    <div v-if="question.answer">
                        <b class = "w-25 p-3">{{ question.answer }}</b>
                    </div>
                    <div v-else-if="getResult.isOwner">
                        <Answer v-bind:question-id="question.id"/>
                    </div>
                    <div v-else>
                        <b>- No answer yet. Check again later.</b>
                    </div>
                </li>
            </ul>
            <div v-if="!getResult.isOwner">
                <PostQuestion v-bind:itemId="itemId"/>
            </div>
        </div>
    </div>
  </header>
</template>