<template>
  <v-app id="app">
    <!-- Esta es la columna lateral -->
    <v-navigation-drawer v-model="drawer" app dense>
      <v-list >

        <!-- Elemento inicio -->
        <template>
          <v-list-item :to="{name: 'Home'}">
            <v-list-item-action>
              <v-icon>home</v-icon>
            </v-list-item-action>
            <v-list-item-title>
              Inicio
            </v-list-item-title>
          </v-list-item>
        </template>
        <!-- Fin elemento inicio -->

        <!--  -->
        <template>

          <v-list-group>

            <v-list-item slot="activator">
              <v-list-item-content>
                <v-list-item-title>
                  Datos comunes
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item :to="{name:'tipolavado'}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Tipos de lavados
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item :to="{name:''}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Tipos de Manteminientos
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          
          </v-list-group>

        </template>
        <!--  -->

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
    <!-- <v-footer height="auto">
      <v-container>
        <v-row text-xs-center>
          <v-card flat tile color="primary" class="white--text">
            <v-card-text justify-center class="dark--text pt-0">
              David Amador
            </v-card-text>
          </v-card>
        </v-row>
      </v-container>
    </v-footer> -->
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
