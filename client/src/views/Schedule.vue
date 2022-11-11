<template>
    <div class="container min-h-screen mx-auto pb-8 px-4 space-y-4">
        <div class="space-y-4">
            <div class="flex justify-between">
                <div class="flex space-x-2">
                    <div>
                        <label for="instructors" class="block mb-2 text-xs xl:text-sm font-medium text-gray-900 dark:text-gray-400">Sort by...</label>
                        <select v-model="sortBy" id="instructors" class="border text-xs xl:text-sm rounded-lg 0 block xl:px-5 xl:py-2.5 px-3 py-1.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500 w-max">
                            <option>
                                Instructors
                            </option>
                            <option>
                                Rooms
                            </option>
                        </select>
                    </div>
                    <div v-if="sortBy == 'Instructors'">
                        <label for="instructors" class="block mb-2 text-xs xl:text-sm font-medium text-gray-900 dark:text-gray-400">Select an instructor</label>
                        <select v-model="selectedInstructor" id="instructors" class="border text-xs xl:text-sm rounded-lg 0 block xl:px-5 xl:py-2.5 px-3 py-1.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500 w-max">
                            <option v-for="i, index in instructors" :key="index">
                                {{i}}
                            </option>
                        </select>
                    </div>
                    <div v-if="sortBy == 'Rooms'">
                        <label for="rooms" class="block mb-2 text-xs xl:text-sm font-medium text-gray-900 dark:text-gray-400">Select a room</label>
                        <select v-model="selectedRoom" id="rooms" class="border text-xs xl:text-sm rounded-lg 0 block xl:px-5 xl:py-2.5 px-3 py-1.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500 w-max">
                            <option v-for="r, index in rooms" :key="index">
                                {{r}}
                            </option>
                        </select>
                    </div>
                </div>
                <button @click="invokeSolver" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-xs xl:text-sm xl:px-5 xl:py-2.5 px-3 py-1.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800 w-max self-end">
                    Invoke Solver
                </button>
            </div>
            <ScheduleWeek v-if="sortBy == 'Instructors'" :modules="classesPerInstructor"></ScheduleWeek>
            <ScheduleWeek v-if="sortBy == 'Rooms'" :modules="classesPerRoom"></ScheduleWeek>
        </div>
        <div>
            <LoadingModal v-model="showModal" :click-to-close="false">
                <template v-slot:title>Solver is working</template>
            </LoadingModal>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import _, {keys} from 'underscore'


import ScheduleWeek from '../components/ScheduleWeek.vue'
import LoadingModal from '../components/LoadingModal.vue'


export default {
    name: 'Schedule',
    data() {
        return {
            schedule: [],
            classesPerInstructor: [],
            classesPerRoom: [],
            instructors: [],
            rooms: [],
            modules: [],
            selectedInstructor: 'Gideon Koekok',
            selectedRoom: 'B.001',
            sortBy: 'Instructors',
            colors: [
                'bg-blue-400',
                'bg-red-400',
                'bg-green-400',
                'bg-yellow-400',
                'bg-indigo-400',
                'bg-pink-400',
                'bg-cyan-400',
                'bg-rose-400',
                'bg-fuchsia-400',
            ],
            showModal: false
        }
    },
    components: {
        ScheduleWeek, LoadingModal
    },
    async created() {
        await this.getSchedule()
    },
    mounted() {

    },
    watch: {
        selectedInstructor(newVal, oldVal) {
            this.sortByInstructor(newVal)
        },
        selectedRoom(newVal, oldVal) {
            this.sortByRoom(newVal)
        }
    },
    methods: {
        async getSchedule() {
            const path = 'http://localhost:5000/schedule';
            const res = await axios.get(path).then((res) => {
                    this.schedule = res.data.schedule
                    this.fillInstructors()
                    this.fillRooms()
                    this.sortByInstructor(this.selectedInstructor)
                    this.sortByRoom(this.selectedRoom)
                })
                .catch((error) => {
                    console.error(error);
                });

        },
        async invokeSolver() {
            this.showModal = true
            const path = 'http://localhost:5000/invoke';
            const res = await axios.get(path)
            await this.getSchedule()
            this.showModal = false
        },
        fillInstructors() {
            let data = this.schedule
            this.instructors = _.keys(_.countBy(data, function(data) { return data.instructor_name; }))
        },
        fillRooms() {
            let data = this.schedule
            this.rooms = _.keys(_.countBy(data, function(data) { return data.room_name; }))
            // console.log(this.rooms)
            this.rooms.sort()
        },
        sortByInstructor(name) {
            this.classesPerInstructor = this.schedule.filter((c) => {
                return (c.instructor_name == name)
            }).map(c => ({...c}))

            this.classesPerInstructor.forEach((c) => {
                return c.end_time = this.addEndTime(c.start_time, c.duration)
            })

            this.classesPerInstructor.forEach((c) => {
                return c.start_time = this.convertStartTime(c.start_time)
            })

            this.addColors(this.classesPerInstructor)

            this.classesPerInstructor.sort(function (a,b) {
                return a.start_time - b.start_time
            })
        },

        sortByRoom(room) {
            this.classesPerRoom = this.schedule.filter((c) => {
                return (c.room_name == room)
            }).map(c => ({...c}))

            this.classesPerRoom.forEach((c) => {
                return c.end_time = this.addEndTime(c.start_time, c.duration)
            })

            this.classesPerRoom.forEach((c) => {
                return c.start_time = this.convertStartTime(c.start_time)
            })

            this.addColors(this.classesPerRoom)

            this.classesPerRoom.sort(function (a,b) {
                return a.start_time - b.start_time
            })
        },
        convertStartTime(startTime) {
            let fraction = 8*60+startTime
            return fraction
        },
        addEndTime(startTime, duration) {
            let fraction = 8*60+startTime+duration
            return fraction
        },

        addColors(arr) {
            arr.sort(function(a,b){
                return a.course_title < b.course_title ? -1 : a.course_title > b.course_title ? 1 : 0;
            })

            let currCourse = arr[0].course_title 
            let j = 0
            for (let i = 0; i < arr.length; i++) {
                if (arr[i].course_title == currCourse) {
                    arr[i].color = this.colors[j]
                }
                else {
                    j+=1
                    arr[i].color = this.colors[j]
                    currCourse = arr[i].course_title
                }
            }
        },
    }
}
</script>