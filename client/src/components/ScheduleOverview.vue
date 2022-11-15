<template>
    <div class="grid grid-rows-5 grid-cols-1 gap-2">
        <div v-for="(day, index) in week" :key="index" class="p-2 rounded-xl w-full mx-auto bg-gray-700 flex flex-col items-center">
            <h2 class="text-3xl font-bold text-white mb-8 text-center select-none">{{day}}</h2>
            <OverviewDay :modules="filterDays(modules, day)" :day="day" class="w-full"></OverviewDay>
        </div>
    </div>
</template>

<script>
import OverviewDay from './OverviewDay.vue'


export default {
    name: 'ScheduleOverview',
    data() {
        return {
            week: [
                'Mon',
                'Tue',
                'Wed',
                'Thu',
                'Fri'
            ],
        }
    },
    components: {
        OverviewDay
    },
    props: {
        modules: Array
    },
    created() {

    },
    mounted() {
        
    },
    methods: {
        filterDays(arr, day) {
            arr = arr.filter((m) => {
                return m.day_name == day
            })
            return arr
        }
    }
}
</script>