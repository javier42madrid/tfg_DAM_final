<template>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                <a class="nav-item nav-link active" href="#">Reservas</a>
                <a class="nav-item nav-link" href="#">Ventas</a>
                <a class="nav-item nav-link" href="#">Compras</a>
                <a class="nav-item nav-link" href="#">Empleados</a>
                </div>
            </div>
            <span style="color: white;">
                <router-link to="/login"><button class="my_button">Cerrar sesión</button></router-link>
            </span>
        </nav>
</template>

<style>
</style>