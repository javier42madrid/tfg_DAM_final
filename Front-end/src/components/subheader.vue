<template>
    <div class="header col-12">
        <div class="row">
            <div class="col-1 logo">
                <a href="#"><img src="@/assets/rest-logo.png" style="width: 80px; height: 80px; opacity: 0%;"></a>
            </div>
            <div class="col-8 title d-flex justify-content-start mt-2">
                <h1><b>Fork Restaurant</b></h1>
            </div>
            <div class="button col-3 d-flex justify-content-center mt-4">
                <span style="color: white;">
                    <router-link to="/login"><button class="my_button">Cerrar sesión</button></router-link>
                </span>
            </div>
        </div>
    </div>
</template>

<style>
    .title {
        color:white;
        -webkit-text-stroke-width: 0.5px;
        -webkit-text-stroke-color: rgb(0, 0, 0);
    }

    .button {
        justify-content: center;
    }
    .header {
        text-align: center;
    }

    .my_button {
        background-color:white;
        border-block-color: black;
        border-radius: 5px;
    }
</style>