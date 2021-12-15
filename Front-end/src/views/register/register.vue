<template>
    <div class="img">
        <div>
            <Header />
        </div>
        <div class="formulario">
            <form
            @submit.prevent="register"
            method="post"
            >
                <h3>Registrarse</h3>
                <div class= "form_group">
                    <label>Email</label>
                    <input v-model="email" type="email" class="form-control form-control-lg"/>
                </div>
                <div class= "form_group">
                    <label>Contraseña</label>
                    <input v-model="contraseña" type="password" class="form-control form-control-lg"/>
                </div>
                <div class= "form_group">
                    <label>Repetir contraseña</label>
                    <input v-model="contraseña_rep" type="password" class="form-control form-control-lg"/>
                </div>
                <div style="background:gray;">
                    <p v-if="check_password == true" style="color:red;"><b>Las contraseñas no coinciden!</b></p>
                </div>
                <button :disabled=check_btn type="submit" class="btn btn-dark btn-lg btn-block mt-2">Registrarse</button>
                <p>Nota: Complete todos los campos correctamente para registrarse</p>
            </form>
        </div>
    </div>
</template>

<script>
    import Header from '@/components/header.vue'
    import axios from 'axios'
    import utils from '@/utils/utils'

    export default{
        name: 'register',
        components: {
            Header
        },
        data: () => ({
            email: '',
            contraseña: '',
            contraseña_rep: '',
            resp: ''
        }),
        computed: {
            check_password () {
                if (this.contraseña != this.contraseña_rep)
                    return (true)
                else
                    return (false)
            },
            check_btn () {
                if (this.check_password == true || (this.contraseña == '' && this.contraseña_rep == ''))
                    return (true)
                else
                    return (false)
            }
        },
        methods: {
            register() {
                const path = 'http://localhost:5000/api/v1.0/register'
                axios.get(path,{
                    params: {
                        email: this.email,
                        contraseña: this.contraseña,
                    }
                }).then((respuesta) => {
                   this.resp = respuesta.data
                   if (this.resp == true) {
                       console.log('Loggin exito')
                       this.$router.push({path: '/login'})
                       this.makeToast('SUCCESS', 'Se ha registrado correctamente!')
                   } else {
                       console.log('contraseña/usuario ya están en uso')
                       this.makeToast('ERROR', 'Se ha producido un error al registrarse, inténtelo de nuevo en unos minutos')
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
        opacity: 90%;
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