<template>
        <table class="text-white rounded-xl w-full border-separate border-spacing-2 border border-slate-500">
            <thead class="mx-auto text-4xl">
                <tr>
                    <th>
                        Time
                    </th>
                    <th colspan="8" class="w-full">
                        Class
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr :id="i + 'row' + this.day" v-for="i, index in 48" :key="index" class="text-sm font-bold ">
                    <td class="border-b text-center">
                        {{convertTime(i-1)}}
                    </td>
                </tr>
            </tbody>
        </table>
</template>

<script>
import OverviewModule from './OverviewModule.vue'


export default {
    name: 'OverviewDay',
    data() {
        return {

        }
    },
    props: {
        modules: Array,
        day: String
    },
    components: {
        OverviewModule
    },
    created() {

    },
    mounted() {
        this.placeModules()
    },
    methods: {
        convertTime(time) {
            let fraction = (8*60+time*15)
            return this.time_convert(fraction)
        },
        time_convert(num) { 
            let hours = Math.floor(num / 60);  
            let minutes = num % 60;
            return `${hours}:${minutes == 0 ? '00' : minutes}`;         
        },
        start(slot) {
            return `row-start-${slot} row-end-${slot+7} row-span-7`
        },
        placeModules() {
            let colors = [
                'bg-blue-300',
                'bg-green-300',
                'bg-indigo-300',
                'bg-red-300',
                'bg-pink-300',
                'bg-teal-300',
                'bg-gray-300',
                'bg-amber-300',
                'bg-pink-300'
            ]
            this.modules.forEach((m) => {
                let row = document.getElementById(String(m.start_time_id) + 'row' +this.day)
                let subject = m.course_title.substring(0,3)
                let div = document.createElement("td")
                let p = document.createElement("p")
                let text = `${m.course_title} \n ${m.instructor_name} \n ${m.course_type} \n ${m.room_name} \n ${this.convertTime(m.start_time_id-1)} - ${this.convertTime(m.end_time_id)}`
                p.innerText = text
                if(m.course_type != 'P') {
                    div.rowSpan = "7"
                    if(subject == 'PHY') {
                        div.classList.add(colors[0])
                    }
                    else if(subject == 'BIO') {
                        div.classList.add(colors[1])
                    }
                    else if(subject == 'INT') {
                        div.classList.add(colors[2])
                    }
                    else if(subject == 'MAT') {
                        div.classList.add(colors[3])
                    }
                    else if(subject == 'NEU') {
                        div.classList.add(colors[4])
                    }
                    else if(subject == 'CHE') {
                        div.classList.add(colors[5])
                    }
                    else if(subject == 'HUM') {
                        div.classList.add(colors[7])
                    }
                    else if(subject == 'SCI') {
                        div.classList.add(colors[8])
                    }
                    
                }
                else {
                    div.rowSpan = "28"
                    div.classList.add(colors[6])
                }
                p.classList.add('text-gray-700')
                p.classList.add('font-bold')
                p.classList.add('text-center')
                p.classList.add('max-w-[100px]')
                p.classList.add('mx-auto')
                div.classList.add('rounded')
                div.classList.add('mx-auto')
                div.appendChild(p)
                row.appendChild(div)
            })
        }
    }
}
</script>