<!-- Lets the user place a bid on an item  by sending the users credentials and the value of their bid -->
<script lang="ts">
    export default {
        props: ['itemId'],
        data() {
            return {
                getResult: null,
            }
        },
        methods: {
            async postBid() {
                const postData = {
                    bid: (this.$refs.post_bid as any).value,
                }
                try {
                    if (postData.bid != null) {
                        console.log((this.itemId as number));
                        const res = await fetch(`https://group43-web-apps-ec19115.apps.d.comp-teach.qmul.ac.uk/api/placeBid/${(this.itemId as number)}`, { 
                            method: "post", 
                            headers: {
                                "Content-Type": "application/json"
                            }, 
                            body : JSON.stringify(postData),
                            'credentials': "include",
                        });
                        if (!res.ok) {
                            
                            const message = `An error has occured: ${res.status} - ${res.statusText}`;
                            throw new Error(message);
                        }

                        const data = await res.json();

                        const result = {
                            status: res.status + "-" + res.statusText,
                            headers: {
                                "Content-Type": res.headers.get("Content-Type"),
                                "Content-Length": res.headers.get("Content-Length"),
                            },
                            data: data,
                        };

                        this.getResult = data;
                        (this.$refs.post_bid as any).value = null;
                        alert("Bid Placed")
                    }
                    else {console.warn("question is empty");}

                } catch (err) {
                    console.error(err);
                }
            },
        },
    }
</script>


<template>
  <header>
    <div class="bg-light rounded shadow p-3">
        <b>please enter your bid</b>
        <form id="postBid" action="" @submit.prevent="postBid">
            <div class="form-group shadow rounded">
                <input class="form-control" type="number" step=".01" name="bid" ref="post_bid" placeholder="10" required/>
            </div>
            <div class="form-group">
                <button class="btn btn-primary">SUBMIT BID</button>
            </div>
        </form>
      </div>
  </header>
</template>