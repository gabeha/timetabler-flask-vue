<template>
    <div class="container min-h-screen mx-auto pb-8 px-4 space-y-4">
        <div>
            <label for="choose" class="block mb-2 text-xs xl:text-sm font-medium text-gray-900 dark:text-gray-400">Insert</label>
            <select v-model="insertSelect" id="choose" class="border text-xs xl:text-sm rounded-lg 0 block xl:px-5 xl:py-2.5 px-3 py-1.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500 w-max">
                <option>
                    Instructor
                </option>
                <option>
                    Room
                </option>
                <option>
                    Module
                </option>
            </select>
        </div>
        <div class="p-4 rounded-xl w-max mx-auto bg-gray-700">
            <form>
                <div class="mb-6">
                    <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Instructor name</label>
                    <input type="text" id="name" class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" placeholder="John Doe" required="true">
                </div>
                <div class="mb-6">
                    <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Your password</label>
                    <input type="password" id="password" class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" required="">
                </div>
                <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Insert</button>
            </form>
        </div>
    </div>
</template>

<script>

export default {
    name: 'InsertValues',
    data() {
        return {
            insertSelect: 'Instructor',
            selected: []
        }
    },
    components: {

    },
    async created() {

    },
    mounted() {

    },
    methods: {

    }
}
</script>