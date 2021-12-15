<template>
    <div class="img">
        <div>
            <Header />
        </div>
        <div class="formulario">
            <form>
                <h3>Iniciar Sesión</h3>
                <div class= "form_group">
                    <label>Email</label>
                    <input type="email" class="form-control form-control-lg"/>
                </div>
                <button type="submit" class="btn btn-dark btn-lg btn-block mt-2">Enviar</button>
            </form>
        </div>
    </div>
</template>

<script>
    import Header from '@/components/header.vue'

    export default{
        name: 'home',
        components: {
            Header
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