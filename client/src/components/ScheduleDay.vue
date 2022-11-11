<template>
    <div class="h-full">
        <div v-if="modules.length == 0" class="flex flex-col justify-center items-center h-full">
            <h5 class="mb-2 text-lg font-semibold tracking-tight leading-none text-white ">Nothing here :)</h5>
        </div>
        <div v-for="m, index in modules" :key="index" class="mb-4">
            <ClassModule :classes="m"></ClassModule>
        </div>
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