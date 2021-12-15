<template>
    <div class="img">
        <div>
            <Navegador />
        </div>
        <div class="content_maint col-11 mt-5">
            <div class="tabla">
                <b-table
                    id="tabla-res"
                    responsive
                    hover
                    :fields="res_fields"
                    :items="res_items"
                    :current-page="currentPage"
                    :per-page="10"
                >
                    <template v-slot:cell(nombre)="data">
                        <span>{{data.item.nombre}}</span>
                    </template>
                    <template v-slot:cell(fecha)="data">
                        <span>{{data.item.fecha}}</span>
                    </template>
                        <template v-slot:cell(email)="data">
                        <span>{{data.item.email}}</span>
                    </template>
                    <template v-slot:cell(asistentes)="data">
                        <span>{{data.item.asistentes}}</span>
                    </template>
                    <template v-slot:cell(id)="data">
                        <span>{{data.item.id}}</span>
                    </template>
                    </b-table>
                    <b-pagination
                        v-model="currentPage"
                        class="d-flex justify-content-center"
                        :total-rows="rows"
                        :per-page="perPage"
                        aria-controls="tabla-res" />
            </div>
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
            token: global_.token,
            currentPage: 1,
            perPage: 10,
            res_items: null,
            rows: null
        }),
        components: {
                Navegador
        },
        computed: {
            res_fields () {
                return [
                    { key: 'nombre', label: 'Nombre' },
                    { key: 'fecha', label: 'Fecha' },
                    { key: 'email', label: 'email' },
                    { key: 'asistentes', label: 'Asistentes' },
                    { key: 'id', label: 'id' },
                ]
            }
        },
        methods: {
            itemToTable (item) {
                let aux = {
                    nombre: item.nombre,
                    fecha: item.fecha,
                    email: item.email,
                    asistentes: item.asistentes,
                    id: item.id 
                }
                return aux
            },
            getMensaje () {
                const path = 'http://localhost:5000/api/v1.0/reservas'
                axios.get(path).then((respuesta) => {
                    this.res_items = []
                    this.mensaje = respuesta.data
                    for (let i in this.mensaje) {
                        let item = this.itemToTable(this.mensaje[i])
                        this.res_items.push(item)
                        this.rows = i
                    }
                    console.log(this.mensaje)
                })
                .catch((error) => {
                    console.log(error)
                })
            }
        },
        created () {
            this.getMensaje()
        },
        watch: {
            currentPage: {
                handler: function (val) {
                    this.currentPage = val
                    this.getMensaje()
                }
            }
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
    .tabla {
        background-color: white;
        border-radius: 15px;
        border-width: medium;
        border-style: solid;
        border-color: black;
    }
</style>