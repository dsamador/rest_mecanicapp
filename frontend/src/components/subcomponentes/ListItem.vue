<template>    
    <v-list-tile>        
        <v-list-tile-action>
            <v-icon>{{materialIcon}}</v-icon>
        </v-list-tile-action>
        
        <v-list-tile-content>
            <v-list-tile-title>
                {{texto}}                
            </v-list-tile-title>
        </v-list-tile-content>    
    </v-list-tile>    
</template>

<script>
export default {
    name:"list-item",
    props:['texto','materialIcon', 'hacia']    
}
</script>

<style>

</style>