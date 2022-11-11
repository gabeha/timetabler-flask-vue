<template>

    <div class="p-6 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hover:bg-opacity-80 dark:border-gray-700 dark:hover:bg-opacity-80" :class="classes.color">
        <div class="flex justify-between">
            <h5 class="mb-2 text-2xl font-extrabold tracking-tight leading-none text-gray-900 dark:text-white">{{classes.course_title}}</h5>
            <h5 class="mb-2 text-lg font-bold tracking-tight leading-none text-gray-900 dark:text-white">{{spellOutType(classes.course_type)}}</h5>
        </div>
        <div class="overflow-x-auto relative shadow-md sm:rounded-lg">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <tbody>
                    <tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                        <th scope="row" class="py-4 pl-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Room
                        </th>
                        <td class="py-4">
                            <span class="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800">{{classes.room_name}}</span>
                        </td>
                    </tr>
                    <tr class="bg-gray-50 border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" class="py-4 pl-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Instructor
                        </th>
                        <td class="py-4">
                            <span class="bg-purple-100 text-purple-800 text-sm font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-purple-200 dark:text-purple-900">{{classes.instructor_name}}</span>
                        </td>
                    </tr>
                    <tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                        <th scope="row" class="py-4 pl-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Time
                        </th>
                        <td class="py-4">
                            <span class="bg-green-100 text-green-800 text-sm font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-green-200 dark:text-green-900">
                            {{time_convert(classes.start_time)}} - {{time_convert(classes.end_time)}}
                            <!-- {{classes.start_time}} - {{classes.end_time}} -->
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
    name: 'ClassModule',
    data() {
        return {

        }
    },
    props: {
        classes: {
            type: Object,
            default: null
        }
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