<template>
    <div class="grid grid-rows-5 grid-cols-1 2xl:grid-rows-1 2xl:grid-cols-5 gap-2">
        <div v-for="(day, index) in week" :key="index" class="p-2 rounded-xl w-full bg-gray-700">
            <h2 class="text-3xl font-bold dark:text-white mb-8 text-center select-none">{{day}}</h2>
            <ScheduleDay :modules="filterDays(modules, day)"></ScheduleDay>
        </div>
    </div>
</template>

<script>
import ScheduleDay from './ScheduleDay.vue';
export default {
    name: "ScheduleWeek",
    data() {
        return {
            week: [
                'Mon',
                'Tue',
                'Wed',
                'Thu',
                'Fri'
            ],
        };
    },
    components: { ScheduleDay },
    props: {
        modules: Array
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