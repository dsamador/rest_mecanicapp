<template>
  <v-app id="app">
    <!-- Esta es la columna lateral -->
    <v-navigation-drawer v-model="drawer" app>
      <v-list >
        <template>
          <!-- Elemento inicio -->
          <v-list-item>
            <v-list-item-action>
              <v-icon>home</v-icon>
            </v-list-item-action>
            <v-list-item-title>
              Inicio
            </v-list-item-title>
          </v-list-item>
          <!-- Fin elemento inicio -->

        </template>
      </v-list>
    </v-navigation-drawer>
    <!-- Fin columna principal -->

    <v-app-bar app color="yellow darken-1">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Mecanicapp</v-toolbar-title>

      <v-spacer></v-spacer>
      
      <v-btn icon>
        <v-icon>logout</v-icon>
      </v-btn>

    </v-app-bar>

    <!-- Aquí va el contenido principal del centro -->
    <v-main>
      <v-container fluid full-height>
        <v-slide-y-transition mode="out-in">
          <router-view/><!-- Carga componentes teniendo en cuenta una ruta -->
        </v-slide-y-transition>
      </v-container>
    </v-main>

    <!-- Footer -->
    <v-footer height="auto">
      <v-layout justify-center>
        <v-flex text-xs-center>
          <v-card flat tile color="primery" class="white--text">
            <v-card-text justify-center class="white--text pt-0">
              David Amador
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-footer>
    <!-- Fin Footer -->
  </v-app>
</template>

<script>

export default {
  name: 'App', 

  data() {
    return {
      drawer:null,     
      
    }
  }
};
</script>
