<template>
    <div class="img">
        <div>
            <Header />
        </div>
       <!-- <div class="body">
            <img src="@/assets/background.png" style="width: 100%; height: 800px">
        </div> -->
        <div class="content class row">
            <div class="col-1"></div>  
            <div class="info col-3 mt-5">
                <section>
                    <article class="articulo pt-2" style="height: 20vh;">
                        <h3 class="text-center"><b>¿Quienes somos?</b></h3>
                        <p class="text-center" style="color:white;">Fork Restaurant es un restaurante ficticio producto del trabajo de fin de grado de Javier Campanero belda. En la descripcion del restaurante podrás encontrar un breve resumen de lo que es ésta web</p>
                    </article>
                    <article class="articulo mt-3 pt-2" style="height: 20vh;">
                        <h3 class="text-center"><b>Contacto</b></h3>
                        <span class="row justify-content-center" style="color:white;">Dirección: c/de Puerta de Atocha, 15, Madrid</span>
                        <span class="row justify-content-center" style="color:white;">Telefono: +34 656296444</span>
                        <span class="row justify-content-center" style="color:white;">email: ForkRestaurant@gmail.com</span>
                   </article>
               </section>

           </div>
            <div class="menu col-3 pr-5 pt-2 pl-5 mt-5">
                <h3 class="text-center"><b>Menú del dia</b></h3>
                <span class="row text-center plato"><b>Primeros:</b></span><br>
                <span class="row justify-content-center plato">-Sopa de pescado y marisco</span>
                <span class="row justify-content-center plato">-Parrillada de verduras de temporada</span>
                <span class="row justify-content-center plato">-Pulpo a la parrila sobre parmentier de patata</span>
                <span class="row justify-content-center plato">-Calamares a la romana</span>
                <hr style="color:white; width:100%; height: 2px;">
                <span class="row text-center plato"><b>Segundos:</b></span><br>
                <span class="row justify-content-center plato">-Macarrones a la carbonara</span>
                <span class="row justify-content-center plato">-Solomillo de ternera con patatas</span>
                <span class="row justify-content-center plato">-Merluza de la casa</span>
                <hr style="color:white; width:100%; height: 2px;">
                <span class="row text-center plato"><b>Postres:</b></span><br>
                <span class="row justify-content-center plato">-Helado de frambuesa casero</span>
                <span class="row justify-content-center plato">-Tarta de Queso</span>
                <span class="row justify-content-center plato">-Flan de mango en nata</span>
                <span class="row justify-content-center plato">-Fruta de temporada</span>
            </div>
            <div class="reserva col-3 mt-5 pt-2">
               <h3 class="text-center"><b>Reservas</b></h3>
               <form
               @submit.prevent="reservar_mesa"
                method="post"
                >
                   <div class="mt-1">
                       <label><b>Nombre</b></label><br>
                       <input v-model="nombre" type="text" class="form-control form-control-lg"/>
                   </div>
                   <div class="mt-1">
                       <label><b>Fecha:</b></label><br>
                       <input v-model="fecha" type="date" min="2021-11-20" max="2023-12-31" class="form-control form-control-lg"/>
                   </div>
                   <div class="mt-1">
                       <label><b>Email:</b></label><br>
                       <input v-model="email" type="email" class="form-control form-control-lg"/>
                   </div>
                   <div class="mt-1">
                       <label><b>Asistentes</b></label><br>
                       <input v-model="asistentes" type="number" class="form-control form-control-lg" min="2" max="12"/>
                   </div>
                   <button type="submit" class="btn btn-dark btn-lg btn-block mt-2">Reservar</button>
               </form>
            </div>
        </div>
        </div>
</template>

<script>
    import Header from '@/components/header.vue'
    import axios from 'axios'
    import utils from '@/utils/utils'

    export default{
        name: 'home',
        components: {
            Header
        },
        data: () => ({
            nombre: '',
            fecha: '',
            email: '',
            asistentes: '',
            resp: ''
        }),
        methods: {
            reservar_mesa() {
                const path = 'http://localhost:5000/api/v1.0/reserva_mesa'
                axios.get(path,{
                    params: {
                        nombre: this.nombre,
                        fecha : this.fecha,
                        email: this.email,
                        asistentes: this.asistentes,
                    }
                }).then((respuesta) => {
                   this.resp = respuesta.data
                   if (this.resp == true) {
                       console.log('Reserva realizada con exito')
                       this.$router.push({path: '/'})
                       this.makeToast('SUCCESS', 'Se ha registrado correctamente su reserva!')
                   } else {
                       console.log('reserva fallida')
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
    
    .articulo {
       justify-content: center;
       background-color: gray;
       border-radius: 5px;
       padding-right: 10px;
       padding-left: 10px;
       margin-right: 10px;
       margin-left: 10px;
       border-color: black;
       border-width: 2px;
       opacity: 80%;
       border-width: medium;
       border-style: solid;
       border-color: black;
    }

    .menu {
       height: 60vh;
       background-color: gray;
       border-radius: 5px;
       padding-right: 10px;
       padding-left: 10px;
       margin-right: 10px;
       margin-left: 10px;
       border-color: black;
       border-width: 2px;
       opacity: 80%;
       border-width: medium;
       border-style: solid;
       border-color: black;
       }

    .reserva {
       height: 60vh;
       background-color: gray;
       border-radius: 5px;
       padding-right: 10px;
       padding-left: 10px;
       margin-right: 10px;
       margin-left: 10px;
       border-color: black;
       border-width: 2px;
       opacity: 80%;
       border-width: medium;
       border-style: solid;
       border-color: black;
    }

    .content {
        height: 80vh;
    }
    
    .plato {
        color: white;
        border-radius: 5px;
        font-family: Georgia, 'Times New Roman', Times, serif;
    }
</style>