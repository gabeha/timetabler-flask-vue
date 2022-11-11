<template>
    <div class="container flex flex-col w-full justify-start items-start min-h-screen mx-auto pb-8 px-4 space-y-4">
        <section class="bg-gray-900 w-full">
            <div class="grid max-w-screen-xl px-4 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
                <div class="mr-auto place-self-center lg:col-span-7">
                    <h1 class="max-w-2xl mb-4 text-3xl font-extrabold tracking-tight leading-none md:text-4xl xl:text-5xl text-white">A teacher's availability survey at the Maastricht Science Programme</h1>
                    <p class="max-w-2xl mb-6 font-light  lg:mb-8 md:text-lg lg:text-xl text-gray-400">Please enter your weekly availability here such that I can work with relevant data for my Bachelor thesis.</p>
                    <a v-if="!showCalendar" href="#form" class="inline-flex items-center justify-center px-5 py-3 mr-3 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-900">
                        Get started
                        <svg class="w-5 h-5 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    </a>
                    <a href="mailto:g.hauss@student.maastrichtuniversity.nl" class="inline-flex items-center justify-center px-5 py-3 text-base font-medium text-center border  rounded-lg  focus:ring-4 text-white border-gray-700 hover:bg-gray-700 focus:ring-gray-800">
                        Contact me
                    </a> 
                </div>
                <div class="lg:mt-0 lg:col-span-5 lg:flex">
                    <img src="../assets/plan.png"  class="w-1/2 lg:w-full mx-auto" alt="logo">
                </div>                
            </div>
        </section>
        <Form v-if="!showCalendar" id="form" @continue="handleEmitTeacher"></Form>
        <div>
            <Modal v-model="showModal" @confirm="confirm" @cancel="cancel">
            <template v-slot:title>Hello, there!</template>
            </Modal>
        </div>
        <Transition name="slide-fade">
            <div v-if="showCalendar" class="font-medium text-white space-y-4 flex flex-col mx-auto w-full">
                <div class="text-lg flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 justify-between items-center">
                    <div class="self-start">
                        Your Courses:
                        <br>
                        <span v-for="s in subjects" :key="s" class="mr-4">
                            {{s}}
                        </span>
                    </div>
                    <div class="flex flex-col space-y-4 justify-center items-center">
                        <button @click="showModal = true" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm max-w-fit sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Show instructions </button>
                        <div class="space-x-4">
                            <span class="bg-gray-500 px-4 py-2 rounded-md cursor-pointer select-none">neutral</span>
                            <span class="bg-green-500 px-4 py-2 rounded-md cursor-pointer select-none">preferred</span>
                            <span class="bg-red-500 px-4 py-2 rounded-md cursor-pointer select-none">unavailable</span>
                        </div>
                    </div>
                </div>
                <Week @day-slot="handleSelection" v-if="showCalendar"></Week>
                <button @click="handleSubmission" type="button" class="flex justify-center items-center self-end text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
                    Submit Choice
                    <svg v-if="loading" class="h-2" width="60" height="30" viewBox="0 0 50 30" xmlns="http://www.w3.org/2000/svg" fill="#fff">
                        <circle cx="15" cy="15" r="15">
                            <animate attributeName="r" from="15" to="15"
                                    begin="0s" dur="0.8s"
                                    values="15;9;15" calcMode="linear"
                                    repeatCount="indefinite" />
                            <animate attributeName="fill-opacity" from="1" to="1"
                                    begin="0s" dur="0.8s"
                                    values="1;.5;1" calcMode="linear"
                                    repeatCount="indefinite" />
                        </circle>
                        <circle cx="60" cy="15" r="9" fill-opacity="0.3">
                            <animate attributeName="r" from="9" to="9"
                                    begin="0s" dur="0.8s"
                                    values="9;15;9" calcMode="linear"
                                    repeatCount="indefinite" />
                            <animate attributeName="fill-opacity" from="0.5" to="0.5"
                                    begin="0s" dur="0.8s"
                                    values=".5;1;.5" calcMode="linear"
                                    repeatCount="indefinite" />
                        </circle>
                        <circle cx="105" cy="15" r="15">
                            <animate attributeName="r" from="15" to="15"
                                    begin="0s" dur="0.8s"
                                    values="15;9;15" calcMode="linear"
                                    repeatCount="indefinite" />
                            <animate attributeName="fill-opacity" from="1" to="1"
                                    begin="0s" dur="0.8s"
                                    values="1;.5;1" calcMode="linear"
                                    repeatCount="indefinite" />
                        </circle>
                    </svg>
                </button>
            </div>
        </Transition>
    </div>
</template>

<script>

import {supabase} from '../supabase'

import Day from '../components/Day.vue';
import Week from '../components/Week.vue';
import Form from '../components/Form.vue';
import Modal from '../components/Modal.vue'

export default {
    name: "Index",
    components: { Day, Week, Form, Modal },
    data() {
        return {
            showCalendar: false,
            showModal: false,
            subjects: [],
            availabilityPreference: [],
            availabilityNeutral: [],
            availabilityUnavailable: [],
            loading: false
        }
    },
    mounted() {
        // this.handleSubmission()
    },
    methods: {
        confirm() {
        // some code...
        this.show = false
        },
        cancel(close) {
        // some code...
        close()
        },
        handleEmitTeacher(subjects) {
            this.subjects = subjects
            this.showCalendar = true
            this.showModal = true
            window.scrollTo(0, document.body.scrollHeight);
        },
        handleSelection(daySlot) {
            if(daySlot.message == 'select') {
                this.availabilityUnavailable = this.availabilityUnavailable.filter(function(el) {
                    return !(el.hour == daySlot.data.hour && el.min == daySlot.data.min && el.day == daySlot.data.day);
                })
                this.availabilityNeutral = this.availabilityNeutral.filter(function(el) {
                    return !(el.hour == daySlot.data.hour && el.min == daySlot.data.min && el.day == daySlot.data.day);
                })
                this.availabilityPreference.push(daySlot.data)
                // console.log('Slot marked as available!')
            }
            else if(daySlot.message == 'delete') {
                this.availabilityPreference = this.availabilityPreference.filter(function(el) {
                    return !(el.hour == daySlot.data.hour && el.min == daySlot.data.min && el.day == daySlot.data.day);
                })
                this.availabilityNeutral = this.availabilityNeutral.filter(function(el) {
                    return !(el.hour == daySlot.data.hour && el.min == daySlot.data.min && el.day == daySlot.data.day);
                })
                this.availabilityUnavailable.push(daySlot.data)
                // console.log('Slot marked as unavailable!')
            }
            else if(daySlot.message == 'neutral') {
                this.availabilityUnavailable = this.availabilityUnavailable.filter(function(el) {
                    return !(el.hour == daySlot.data.hour && el.min == daySlot.data.min && el.day == daySlot.data.day);
                })
                this.availabilityPreference = this.availabilityPreference.filter(function(el) {
                    return !(el.hour == daySlot.data.hour && el.min == daySlot.data.min && el.day == daySlot.data.day);
                })
                this.availabilityNeutral.push(daySlot.data)
                // console.log('Slot marked as neutral!')
            }
        },
        async handleSubmission() {
            this.loading = true
            const { data, error } = await supabase
                .from('availability')
                .select()

            let id = 0 
            let id_changed = false
            data.forEach(d => {
                for(let i = 0; i < d.courses.length; i++) {
                    for(let j = 0; j < this.subjects.length; j++) {
                        if(d.courses[i] == this.subjects[j]) {
                            id = d.id
                            id_changed = true
                        }
                    }
                }

            })

            if(id_changed) {
                const { data, error } = await supabase
                    .from('availability')
                    .update({ 
                        neutral: this.availabilityNeutral,
                        preference: this.availabilityPreference,
                        unavailable: this.availabilityUnavailable
                    })
                    .match({ id: id })
                this.loading = false
                alert('Your availabilities have been updated, thank you!')
                location.reload()
            }
            else {
                const { data, error } = await supabase
                    .from('availability')
                    .insert([
                        {
                            courses: this.subjects,
                            neutral: this.availabilityNeutral,
                            preference: this.availabilityPreference,
                            unavailable: this.availabilityUnavailable
                        }
                    ])
                    this.loading = false
                    alert('Your availabilities have been recorded, thank you!')
                    location.reload()
            }

        }
    }
}
</script>

<style scoped>
/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}

</style>