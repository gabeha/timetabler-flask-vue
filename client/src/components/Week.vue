<template>
    <div class="grid grid-rows-5 grid-cols-1 2xl:grid-rows-1 2xl:grid-cols-5 gap-2">
        <div v-for="(day, index) in week" :key="index" class="bg-gray-700 p-2 rounded-xl w-full">
            <h2 class="text-3xl font-bold dark:text-white mb-8 text-center select-none">{{day}}</h2>
            <Day :name="day" @slot-select="(arg) => {handleSlot(arg, day)}" @slot-neutral="(arg) => {handleSlot(arg, day)}" @slot-delete="(arg) => {handleSlot(arg, day)}"></Day>
        </div>
    </div>
</template>

<script>
import Day from './Day.vue';
export default {
    name: "Week",
    data() {
        return {
            week: [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday'
            ]
        };
    },
    components: { Day },
    methods: {
        handleSlot(arg, day) {
            let daySlot = {
                hour: arg.data.hour,
                min: arg.data.min,
                day: day
            }
            this.$emit('day-slot', {data:daySlot, message:arg.message})
        }
    }
}
</script>