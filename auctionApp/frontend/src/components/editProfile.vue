
<!-- Lets the user update their User profile by updating their usernmae, email, DOB and Profile Image -->

<template>
    <div class="text-dark border rounded bg-light">
        <h1>
            Edit Profile
        </h1>
        <form id="putProfile" action="" @submit.prevent="editData">
            Username: 
            <input required v-model= user.username name = 'username' />
            <br>
            Email: 
            <input type = 'email' required v-model= user.email name = 'email' />
            <br>
            Date of Birth: 
            <input type = 'Date' required v-model= user.DOB name = 'DOB' />
            <br>
            Profile Image: 
            <input class="form-control" type="file" name="file" ref="post_image" accept="image/png, image/jpeg" @change="handleFileUpload( $event )"/>
            <button class="btn btn-primary">Update</button>
        </form>

        

    </div>
    

</template>

<script lang="ts">
import Vue from 'vue'  
var _user: {username: string, email: string, DOB: Date}
    export default {
        data(){
            return {
                user: _user,
                // Profile Imaage
                file: File,
            }
        },
        created(){
            this.fetchUser()
        },

        methods: {
            handleFileUpload(event : Event){
                if (event.target != null){
                    this.file = (event.target as any).files[0];
                }
            },

            // Fetches cookie
            getCookie(ck: String) {
                let cookieValue: string = "";
                if (document.cookie && document.cookie !== "") {
                    const cookies = document.cookie.split(";");
                    for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, ck.length + 1) === (ck + "=")) {
                        cookieValue = decodeURIComponent(cookie.substring(ck.length + 1));
                        break;
                    }
                    }
                }
                return cookieValue;
            },
            // Sends Put request to update user data
            async editData(e: any){
                // const form = document.getElementById('putProfile');
                // const formData = new FormData(form as any);
                // formData.append('file', (this.file as any));

                try{
                    e.preventDefault()   
                    let payload = {
                    username: this.user.username,
                    email: this.user.email,
                    DOB: this.user.DOB,
                }
                    console.log(payload)

                    let res = await fetch(`https://group43-web-apps-ec19115.apps.d.comp-teach.qmul.ac.uk/api/user`, {
                    'credentials': "include",
                    method: 'PUT',
                    headers: {
                        "X-CSRFToken": this.getCookie("csrftoken"),
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                    });
                    alert('Saved')
                    this.fetchUser();
                }
                catch(error){
                        console.log(error)
                    }
            
            },

            //Fetches user data and puts it in user[]
            async fetchUser(){
                try{
                    let response = await fetch('https://group43-web-apps-ec19115.apps.d.comp-teach.qmul.ac.uk/api/user',{
                    'credentials': "include",})
                    let data = await response.json()
                    this.user = data.cur_user_data
                    console.log(this.user);
                }
                    catch(error){
                        console.log(error)
                    }
                
            },

            
        }
    }

        

</script>