<template>
    <div class="img">
        <div>
            <Navegador />
        </div>
        <div class="content_maint col-11 mt-5">
            <p>{{token}}</p>
            <b-btn @click="getMensaje">Click</b-btn>
            <p></p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import global_ from '@/store/global.vue'
    import Navegador from '@/components/navegador.vue'

    export default {
        name: 'Main',
        data: () => ({
            mensaje: '',
            token: global_.token
        }),
        components: {
                Navegador
        }, 
        methods: {
            getMensaje () {
                const path = 'http://localhost:5000/api/v1.0/reservas'
                axios.get(path).then((respuesta) => {
                    this.mensaje = respuesta.data
                    console.log(this.mensaje)
                })
                .catch((error) => {
                    console.log(error)
                })
            }
        },
        created () {
            const path = 'http://localhost:5000/api/v1.0/reservas'
                axios.get(path).then((respuesta) => {
                    this.mensaje = respuesta.data
                    console.log(this.mensaje)
                })
                .catch((error) => {
                    console.log(error)
                })
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