<template>
    <div class="img">
        <div>
            <Header />
        </div>
        <div class="formulario">
            <form
            @submit.prevent="check_login"
            method="get"
            >
                <h3>Iniciar Sesión</h3>
                <div class= "form_group">
                    <label>email</label>
                    <input v-model="email" type="email" class="form-control form-control-lg"/>
                </div>
                <div class= "form_group">
                    <label>contraseña</label>
                    <input v-model="contraseña" type="password" class="form-control form-control-lg"/>
                </div>
                <button type="submit" class="btn btn-dark btn-lg btn-block mt-2">Iniciar sesión</button>
                <p class="mt-2 mb-4">
                <router-link style="color: blue;" to="/forgot_password">¿Contraseña olvidada?</router-link>
                </p>
            </form>
        </div>
    </div>
</template>

<script>
    import Header from '@/components/header.vue'
    import axios from 'axios'
    import utils from '@/utils/utils'

    export default{
        name: 'login',
        data: () => ({
            email: '',
            contraseña: '',
            resp: ''
        }),
        components: {
            Header
        },        
        methods: {
            check_login() {
                const path = 'http://localhost:5000/api/v1.0/check_login'
                axios.get(path,{
                    params: {
                        email: this.email,
                        contraseña: this.contraseña,
                    }
                }).then((respuesta) => {
                   this.resp = respuesta.data
                   if (this.resp == false) {
                       console.log('email/contraseña erroneos')
                       console.log(this.contraseña)
                       console.log(this.email)
                   } else if (this.resp == 'admin1234') {
                       console.log('exito admin')
                       this.$router.push({path: '/user'})
                       this.makeToast('SUCCESS', 'Se ha loggeado correctamente!')
                   } else {
                       this.$router.push({path: '/default_user'})
                       this.makeToast('SUCCESS', 'Se ha loggeado correctamente (como usuario normal)!')
                   }
                })
                .catch((error) => {
                    console.log(error)
                })
            },
            makeToast: utils.makeToast
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

    .formulario {
        height: 50vh;
        margin-left: 35%;
        margin-top: 5%;
        opacity: 80%;
        background-color: gray;
        width: 450px;
        box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
        padding: 40px 55px 45px 55px;
        border-radius: 15px;
        border-width: medium;
        border-style: solid;
        border-color: black;
    }
    </style>