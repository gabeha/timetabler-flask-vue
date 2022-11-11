<template>
    <div v-for="m, index in modules" :key="index" class="mb-4">
        <ClassModule :classes="m"></ClassModule>
    </div>
</template>

<script>
import ClassModule from './ClassModule.vue'

export default {
    name: 'ScheduleDay',
    data() {
        return {

        }
    },
    props: {
        modules: Array
    },
    components: {
        ClassModule
    },
    mounted() {

    },
    methods: {

    }
}
</script>