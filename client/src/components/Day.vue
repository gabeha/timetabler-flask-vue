<template>
    <div>
        <div class="flex items-center justify-center space-x-3 border max-w-fit mx-auto px-2 py-1 rounded mb-4">
            <span :id="`entireDay${this.name}`" class="flex items-center" @click="checkEntireDay(this.name)">
                <font-awesome-icon icon="fa-solid fa-check" class="border-2 rounded p-0.5 hover:cursor-pointer hover:scale-110" :id="`icon${this.name}`"/>
            </span>
            <span class="text-xl select-none">
                Mark entire day
            </span>             
        </div>

        <div v-for="(timeslot, index) in timeslots" :key="index" class="flex text-white justify-center 2xl:justify-start items-center space-x-4 mb-2">
            <div v-if="index % 4 == 0" class="flex flex-col justify-between items-center">
                <span class="font-semibold text-lg select-none">
                    {{hours[index/4]}}h:
                </span>
                <span :id="`checkbox${this.name + index}`" @click="checkEntireHour(hours[index/4], index)">
                    <font-awesome-icon icon="fa-solid fa-check" class="border-2 rounded p-0.5 hover:cursor-pointer hover:scale-110" :id="`icon${this.name + index}`"/>
                </span>
            </div>
            <div v-if="index % 4 == 0">
                <div class="space-x-2 flex">
                    <p :id="this.name + index" @click="handleClick(hours[index/4], index)" class="max-w-max bg-gray-500 px-4 py-2 rounded-md cursor-pointer select-none hover:scale-110 transition-all">
                        <!-- 0-15 -->
                        {{min(timeslots[index])}}
                    </p>
                    <p :id="this.name + (index+1)" @click="handleClick(hours[index/4], index+1)" class="max-w-max bg-gray-500 px-4 py-2 rounded-md cursor-pointer select-none hover:scale-110 transition-all">
                        <!-- 15-30 -->
                        {{min(timeslots[index+1])}}
                    </p>
                    <p :id="this.name + (index+2)" @click="handleClick(hours[index/4], index+2)" class=" max-w-max bg-gray-500 px-4 py-2 rounded-md cursor-pointer select-none hover:scale-110 transition-all">
                        <!-- 30-45 -->
                        {{min(timeslots[index+2])}}
                    </p>
                    <p :id="this.name + (index+3)" @click="handleClick(hours[index/4], index+3)" class="max-w-max bg-gray-500 px-4 py-2 rounded-md cursor-pointer select-none hover:scale-110 transition-all">
                        <!-- 45-60 -->
                        {{min(timeslots[index+3])}}
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Day',
    data() {
        return {
            timeslots: Array.from(Array(48).keys()),
            hours: Array.from({length: 12}, (_, i) => i + 8)
        }
    },
    props: {
        name: String,
    },
    emits: ['slot-select', 'slot-neutral', 'slot-delete'],
    mounted() {
        // console.log(this.name)
    },
    methods: {
        min(index) {
            if(index % 4 == 0) {
                return 15
            }
            else if (index % 4 == 1) {
                return 30
            }
            else if (index % 4 == 2) {
                return 45
            }
            else if (index % 4 == 3) {
                return 60
            }
        },
        handleClick(hour, index) {

            if(document.getElementById(this.name + index).classList.contains('bg-green-500')) {
                let slot = {
                    hour: hour,
                    min: this.min(this.timeslots[index])
                }
                document.getElementById(this.name + index).classList.remove('bg-green-500');
                document.getElementById(this.name + index).classList.add('bg-red-500');
                this.$emit('slot-delete', {data:slot, message:'delete'})
            }
            else if (document.getElementById(this.name + index).classList.contains('bg-red-500')) {
                let slot = {
                    hour: hour,
                    min: this.min(this.timeslots[index])
                }
                document.getElementById(this.name + index).classList.remove('bg-red-500');
                this.$emit('slot-neutral', {data:slot, message:'neutral'})
            }
            else {
                let slot = {
                    hour: hour,
                    min: this.min(this.timeslots[index])
                }
                document.getElementById(this.name + index).classList.add('bg-green-500');
                this.$emit('slot-select', {data:slot, message:'select'})
            }
        },
        checkEntireHour(hour, index) {
            if(document.getElementById('icon' + this.name + index).classList.contains('border-green-500')) {
                document.getElementById('icon' + this.name + index).classList.remove('border-green-500');
                document.getElementById('icon' + this.name + index).classList.remove('text-green-500');
                document.getElementById('icon' + this.name + index).classList.add('border-red-500');
                document.getElementById('icon' + this.name + index).classList.add('text-red-500');
            }
            else if (document.getElementById('icon' + this.name + index).classList.contains('border-red-500')) {
                document.getElementById('icon' + this.name + index).classList.remove('border-red-500');
                document.getElementById('icon' + this.name + index).classList.remove('text-red-500');
            }
            else {
                document.getElementById('icon' + this.name + index).classList.add('border-green-500');
                document.getElementById('icon' + this.name + index).classList.add('text-green-500');
            }
            for (let i = 0; i < 4; i++) {
                let idx = index + i;
                if(document.getElementById(this.name + idx).classList.contains('bg-green-500')) {
                    let slot = {
                        hour: hour,
                        min: this.min(this.timeslots[idx])
                    }
                    document.getElementById(this.name + idx).classList.remove('bg-green-500');
                    document.getElementById(this.name + idx).classList.add('bg-red-500');
                    this.$emit('slot-delete', {data:slot, message:'delete'})
                }
                else if (document.getElementById(this.name + idx).classList.contains('bg-red-500')) {
                    let slot = {
                        hour: hour,
                        min: this.min(this.timeslots[idx])
                    }
                    document.getElementById(this.name + idx).classList.remove('bg-red-500');
                    this.$emit('slot-neutral', {data:slot, message:'neutral'})
                }
                else {
                    let slot = {
                        hour: hour,
                        min: this.min(this.timeslots[idx])
                    }
                    document.getElementById(this.name + idx).classList.add('bg-green-500');
                    this.$emit('slot-select', {data:slot, message:'select'})
                }
            }
        },
        checkEntireDay(day) {
            if(document.getElementById('icon' + this.name).classList.contains('border-green-500')) {
                document.getElementById('icon' + this.name).classList.remove('border-green-500');
                document.getElementById('icon' + this.name).classList.remove('text-green-500');
                document.getElementById('icon' + this.name).classList.add('border-red-500');
                document.getElementById('icon' + this.name).classList.add('text-red-500');
                this.handleDay('delete')
            }
            else if (document.getElementById('icon' + this.name).classList.contains('border-red-500')) {
                document.getElementById('icon' + this.name).classList.remove('border-red-500');
                document.getElementById('icon' + this.name).classList.remove('text-red-500');
                this.handleDay('neutral')
            }
            else {
                document.getElementById('icon' + this.name).classList.add('border-green-500');
                document.getElementById('icon' + this.name).classList.add('text-green-500');
                this.handleDay('select')
            }
            

            // for (let i = 0; i < 48; i++) {
            //     let idx = i;
            //     let hour = this.hours[Math.floor(idx/4)]
            //     // console.log(hour)
            //     if(idx%4 == 0) {
            //         // console.log(idx/4)
            //         this.colorTickMarks(idx)
            //     }
            //     if(document.getElementById(this.name + idx).classList.contains('bg-green-500')) {
            //         let slot = {
            //             hour: hour,
            //             min: this.min(this.timeslots[idx])
            //         }
            //         document.getElementById(this.name + idx).classList.remove('bg-green-500');
            //         document.getElementById(this.name + idx).classList.add('bg-red-500');
            //         this.$emit('slot-delete', {data:slot, message:'delete'})
            //     }
            //     else if (document.getElementById(this.name + idx).classList.contains('bg-red-500')) {
            //         let slot = {
            //             hour: hour,
            //             min: this.min(this.timeslots[idx])
            //         }
            //         document.getElementById(this.name + idx).classList.remove('bg-red-500');
            //         this.$emit('slot-neutral', {data:slot, message:'neutral'})
            //     }
            //     else {
            //         let slot = {
            //             hour: hour,
            //             min: this.min(this.timeslots[idx])
            //         }
            //         document.getElementById(this.name + idx).classList.add('bg-green-500');
            //         this.$emit('slot-select', {data:slot, message:'select'})
            //     }
            // }
        },
        colorTickMarks(idx, action) {
            // console.log(idx)
            if(action == 'delete') {
                document.getElementById('icon' + this.name + idx).classList.remove('border-green-500');
                document.getElementById('icon' + this.name + idx).classList.remove('text-green-500');
                document.getElementById('icon' + this.name + idx).classList.add('border-red-500');
                document.getElementById('icon' + this.name + idx).classList.add('text-red-500');
                
            }
            else if (action == 'neutral') {
                document.getElementById('icon' + this.name + idx).classList.remove('border-red-500');
                document.getElementById('icon' + this.name + idx).classList.remove('text-red-500');
                
            }
            else if (action == 'select'){
                document.getElementById('icon' + this.name + idx).classList.remove('border-red-500');
                document.getElementById('icon' + this.name + idx).classList.remove('text-red-500');
                document.getElementById('icon' + this.name + idx).classList.add('border-green-500');
                document.getElementById('icon' + this.name + idx).classList.add('text-green-500');
                
            }
        },
        handleDay(action) {
            for (let i = 0; i < 48; i++) {
                let idx = i;
                let hour = this.hours[Math.floor(idx/4)]
                // console.log(hour)
                if(idx%4 == 0) {
                    this.colorTickMarks(idx, action)
                }
                
                if(action == 'delete') {
                    let slot = {
                        hour: hour,
                        min: this.min(this.timeslots[idx])
                    }
                    document.getElementById(this.name + idx).classList.remove('bg-green-500');
                    document.getElementById(this.name + idx).classList.add('bg-red-500');
                    this.$emit('slot-delete', {data:slot, message:'delete'})
                }
                else if (action == 'neutral') {
                    let slot = {
                        hour: hour,
                        min: this.min(this.timeslots[idx])
                    }
                    document.getElementById(this.name + idx).classList.remove('bg-red-500');
                    document.getElementById(this.name + idx).classList.remove('bg-green-500');
                    this.$emit('slot-neutral', {data:slot, message:'neutral'})
                }
                else if (action == 'select') {
                    let slot = {
                        hour: hour,
                        min: this.min(this.timeslots[idx])
                    }
                    document.getElementById(this.name + idx).classList.remove('bg-red-500');
                    document.getElementById(this.name + idx).classList.add('bg-green-500');
                    this.$emit('slot-select', {data:slot, message:'select'})
                }
            }
        }
    }
}
</script>