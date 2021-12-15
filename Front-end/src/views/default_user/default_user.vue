<template>
    <div class="img">
        <div>
            <Subheader />
        </div>
        <div class="content_maint col-11 mt-5">
            <h3 class="row justify-content-center">Web en mantenimiento</h3>
            <h5 class="row justify-content-center">Cooming soon.....</h5>
        </div>
    </div>
</template>

<script>

import Subheader from '@/components/subheader.vue'

export default{
    name: 'default_user',
    components: {
            Subheader
        }
}
</script>


<style>
    .img {
        width: 100%;
        height: 1000px;
        background-repeat:no-repeat;
        background:url('../../assets/img/background.png');
        background-size: cover;
    }
    .content_maint {
        margin-left: 10%;
        height: 80vh;
        opacity: 80%;
        background-color: gray;
        width: 80vw;
        box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
        padding: 40px 55px 45px 55px;
        border-radius: 15px;
        border-width: medium;
        border-style: solid;
        border-color: black;
    }
</style>