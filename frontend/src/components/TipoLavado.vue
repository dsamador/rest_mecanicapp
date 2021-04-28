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
                        <v-btn color="primary" dark class="mb-2" v-on="on">Nuevo registro</v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                            <span class="headline">{{ formTitle }}</span>
                        </v-card-title>
            
                        <v-card-text>
                            <v-container grid-list-md>
                                <v-layout wrap>
                                    <v-flex xs12 sm12 md12>
                                        <v-text-field v-model="nombre" label="Nombre *"></v-text-field>
                                    </v-flex>                                    
                                    <v-flex xs12 sm12 md12>
                                        <v-text-field v-model="descripcion" label="Descripción"></v-text-field>
                                    </v-flex>                                    
                                    <v-flex xs12 sm12 md12 v-show="valida">
                                        <div class="red--text" v-for="v in validaMensaje" :key="v" v-text="v"></div>
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
                
                
                <!-- Modal para eliminar -->
                <v-dialog v-model="adModal" max-width="500">
                    <v-card>                                                                            
                        <v-card-title class="headline">Eliminar registro</v-card-title>
                        <v-card-text>¿Estás seguro/a de eliminar el registro "<span class="light-blue lighten-3 dark--text"> {{adNombre}}</span>"?</v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="green" @click="close2()">
                                Cancelar
                            </v-btn>
                            <v-btn color="orange" @click="deleteItem()">
                                Aceptar
                            </v-btn>
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
                        <v-icon small class="mr-2" @click="modalDelete(props.item)"> delete </v-icon>                         
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
                id:'',
                nombre:'',
                descripcion:'',
                valida:0,
                validaMensaje:[],
                adModal: false,
                adAccion:0,
                adNombre:'',
                adId:''
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
                this.valida = 0;
                this.validaMensaje = [];
                this.editedIndex = -1;
            },
            validar(){
                this.valida = 0;
                this.validaMensaje = [];
                if(this.nombre.length<1 || this.nombre.length>254){
                    this.validaMensaje.push('El nombre del tipo de lavado debe tener entre 1-254 caracteres');
                }
                if(this.descripcion.length>254){
                    this.validaMensaje.push('La descripcion del tipo de lavado debe tener entre 1-254 caracteres');
                }
                if(this.validaMensaje.length){
                    this.valida = 1;
                }
                return this.valida;
            },
            guardar(){
                let me = this;
                if(this.validar()){
                    return;
                }
                if(this.editedIndex > -1){
                    //Editar registro
                    axios.put(`tipos/tipos_lavados/${this.id}/`, {'id':this.id, 'nombre':this.nombre, 'descripcion':this.descripcion})
                    .then(function(){
                        me.limpiar();
                        me.close();
                        me.listar();
                    })
                    .catch(function(error){
                        console.log(error)
                    });
                }else{
                    //Guardar registro
                    axios.post('tipos/tipos_lavados/', {'nombre':this.nombre, 'descripcion':this.descripcion})
                    .then(function (response){
                        me.limpiar();
                        me.close();
                        me.listar();/* Es necesario aquí poner el método listar */

                    })
                    .catch(function(error){
                        console.log(error)
                    });
                }
            },
            editItem (item) {
                this.id = item.id;
                this.nombre = item.nombre;
                this.descripcion = item.descripcion;
                this.dialog = true;
                this.editedIndex = 1;
            },
            modalDelete(item){                
                this.adModal = true;                                           
                this.adNombre = item.nombre;
                this.adId = item.id;
            },
            deleteItem () {   
                let me = this;               
                axios.delete(`tipos/tipos_lavados/${this.adId}/`)
                .then(function(){                                        
                    me.adModal = false;
                    me.listar();
                })
                .catch(function(error){
                    console.log(error)
                });                
            },
            close () {
                this.dialog = false
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                }, 300)
            }, 
            close2 () {
                this.adModal = false;
            }
        }
    }
</script>
