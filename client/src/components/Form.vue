<template>    
    <form class="border-2 p-4 rounded-xl border-gray-500 mx-auto max-w-full" @submit.prevent="handleSubmit">
        <h2 class="text-xl font-bold text-white mb-8 text-center select-none">How many courses do you teach?</h2>
        <div class="mb-6">
            <label for="number" class="block mb-2 text-sm font-medium  text-gray-300">Number of courses</label>
            <input v-model="number" type="number" min="1" id="number" class=" border  text-sm rounded-lg  block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500 outline-none appearance-none" placeholder="1" required="true">
        </div>
        <div v-if="number !== 0">
            <div v-for="n in number" :key="n" class="mb-6">
                <label :for="`subject${n}`" class="block mb-2 text-sm font-medium  text-gray-300">Course {{n}}</label>
                <input v-model="subjects[n-1]" type="text" :id="`subject${n}`" class=" border  text-sm rounded-lg  block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500" placeholder="PHY2006" required="true">
            </div>
        </div>
        <!-- <div class="mb-6">
            <label for="lastname" class="block mb-2 text-sm font-medium  text-gray-300">Last Name</label>
            <input v-model="lastName" type="text" id="lastname" class=" border  text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500" placeholder="Doe" required="true">
        </div>
        <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium text-gray-300">Your email</label>
            <input v-model="email" type="email" id="email" class=" border text-sm rounded-lg  block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500" placeholder="john@doe.com" required="true">
        </div> -->
        <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Continue</button>
    </form>
</template>

<script>
export default {
    name: 'Form',
    data() {
        return {
            // firstName: '',
            // lastName: '',
            // email: ''
            number: 0,
            subjects: [],
        }
    },
    methods: {
        handleSubmit() {
            // let teacher = {
            //     firstName: this.firstName,
            //     lastName: this.lastName,
            //     email: this.email
            // }
            this.$emit('continue', this.subjects)
        }
    }
}
</script>