<template>
    <v-layout align-start>
        <v-flex>
            <v-toolbar flat color="white">
                <v-toolbar-title>Tipos de lavados</v-toolbar-title>
                <v-divider
                class="mx-2"
                inset
                vertical
                ></v-divider>
                <v-spacer></v-spacer>
                <v-text-field class="text-xs-center" v-model="search" append-icon="search" 
                label="Búsqueda" single-line hide-details></v-text-field>
                <v-spacer></v-spacer>

                <v-dialog v-model="dialog" max-width="500px">
                    <template v-slot:activator="{ on }">
                        <v-btn color="primary" dark class="mb-2" v-on="on">Nuevo</v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                        <span class="headline">{{ formTitle }}</span>
                        </v-card-title>
            
                        <v-card-text>
                            <v-container grid-list-md>
                                <v-layout wrap>
                                    <v-flex xs12 sm12 md12>
                                        <v-text-field v-model="nombre" label="Nombre"></v-text-field>
                                    </v-flex>                                    
                                    <v-flex xs12 sm12 md12>
                                        <v-text-field v-model="descripcion" label="Descripción"></v-text-field>
                                    </v-flex>                                    
                                </v-layout>
                            </v-container>
                        </v-card-text>
        
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="blue darken-1" flat @click="close">Cancelar</v-btn>
                            <v-btn color="blue darken-1" flat @click="guardar">Guardar</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>

            </v-toolbar>

            <v-data-table
                :headers="headers"
                :items="tipos_de_lavados"
                :search="search"
                class="elevation-1"
            >
                <template v-slot:items="props">
                    <td>{{ props.item.nombre }}</td>
                    <td>{{ props.item.descripcion }}</td>                            
                    <td>
                        <v-icon small class="mr-2" @click="editItem(props.item)"> edit </v-icon>
                        <v-icon small class="mr-2" @click="deleteItem(props.item)"> delete </v-icon>                    
                    </td>
                </template>
                <template v-slot:no-data>
                    <v-btn color="primary" @click="listar()">Resetear</v-btn>
                </template>
            </v-data-table>
        </v-flex>
    </v-layout>
</template>

<script>
    import axios from "axios";
    export default {
        data(){
            return{
                dialog: false,
                search:'',
                tipos_de_lavados:[],
                dialogDelete:false,
                headers: [        
                    { text: 'Nombre', value: 'nombre', sortable:true },
                    { text: 'Descripcion', value: 'descripcion', sortable:true },
                    { text: 'Actions', value: 'action', sortable:false },   
                ],                
                editedIndex: -1,
                _id:'',
                nombre:'',
                descripcion:''
            }
        },
        computed: {
            formTitle () {
                return this.editedIndex === -1 ? 'Nuevo registro' : 'Editar registro'
            }
        },
        watch: {
            dialog (val) {
                val || this.close()
            }
        },
        created () {
            this.listar();
        },
        methods: {
            listar(){
                let me = this;/* Refiere a toda esta clase */
                axios.get('tipos/tipos_lavados/')
                .then(
                function (response){
                    console.log(response)
                    me.tipos_de_lavados = response.data;
                })
                .catch(function (error){
                    console.log('Errores ')
                    console.log(error);
                })
            },
            limpiar(){
                this.nombre='';
                this.descripcion='';
            },
            guardar(){
                let me = this;
                if(this.editedIndex > -1){
                    //Editar registro
                }else{
                    //Guardar registro
                    axios.post('tipos/tipos_lavados/',{'nombre':this.nombre, 'descripcion':this.descripcion})
                    .then(function (response){
                        me.limpiar();
                        me.close();
                        me.listar();

                    })
                    .catch(function(error){
                        console.log(error)
                    });
                }
            },
            editItem (item) {
                this.editedIndex = this.desserts.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },

            deleteItem (item) {
                const index = this.desserts.indexOf(item)
                confirm('Are you sure you want to delete this item?') && this.desserts.splice(index, 1)
            },

            close () {
                this.dialog = false
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                }, 300)
            },            
        }
    }
</script>
