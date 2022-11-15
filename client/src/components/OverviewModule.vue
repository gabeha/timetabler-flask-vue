<template>

    <div class="p-2 rounded-lg bg-gray-500 shadow-xl hover:bg-opacity-80 hover:bg-gray-600">
        <div class="flex justify-between">
            <h5 class="mb-2 text-lg font-extrabold tracking-tight leading-none px-2 py-1 rounded-md text-gray-800" :class="modules.color">{{modules.course_title}}</h5>
            <h5 class="mb-2 text-base font-semibold tracking-tight leading-none text-white ">{{spellOutType(modules.course_type)}}</h5>
        </div>
        <div class="overflow-x-auto sm:rounded-lg">
            <table class="w-full text-xs text-left text-gray-500">
                <tbody>
                    <tr class="border-b bg-gray-900 border-gray-700">
                        <th scope="row" class="py-2 pl-2 font-medium whitespace-nowrap text-white">
                            Room
                        </th>
                        <td class="py-2">
                            <span class="text-xs font-medium ml-2 px-2.5 py-0.5 rounded bg-blue-200 text-blue-800">{{modules.room_name}}</span>
                        </td>
                    </tr>
                    <tr class="border-b bg-gray-800 border-gray-700">
                        <th scope="row" class="py-2 pl-2 font-medium  whitespace-nowrap text-white">
                            Instructor
                        </th>
                        <td class="py-2">
                            <span class=" text-xs font-semibold ml-2 px-2.5 py-0.5 rounded bg-purple-200 text-purple-900">{{modules.instructor_name}}</span>
                        </td>
                    </tr>
                    <tr class=" border-b bg-gray-900 border-gray-700">
                        <th scope="row" class="py-2 pl-2 font-medium whitespace-nowrap text-white">
                            Time
                        </th>
                        <td class="py-2">
                            <span class=" text-xs font-semibold ml-2 px-2.5 py-0.5 rounded bg-green-200 text-green-900">
                            <!-- {{time_convert(modules.start_time)}} - {{time_convert(modules.end_time)}} -->
                            {{modules.start_time}} - {{modules.end_time}}
                        </span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

    </div>

</template>

<script>
export default {
    name: 'OverviewModule',
    data() {
        return {

        }
    },
    props: {
        modules: null
    },
    methods: {
        spellOutType(type) {
            if(type == 'L') {
                return 'Lecture'
            }
            else if(type == 'T') {
                return 'Tutorial'
            }
            else if(type == 'P') {
                return 'Practical'
            }
        },
        time_convert(num) { 
            let hours = Math.floor(num / 60);  
            let minutes = num % 60;
            return `${hours}:${minutes == 0 ? '00' : minutes}`;         
        }
    }
}
</script>