<template>
    <nav class=" border-gray-200 px-4 sm:px-4 py-2.5 bg-gray-900">
        <div class="container flex flex-col justify-center py-2 items-center mx-auto space-y-4">
            <router-link to="/" class="flex items-center">
                <font-awesome-icon icon="fa-regular fa-calendar-days" class="text-white mr-2 h-6"/>
                <span class="self-center text-2xl lg:text-4xl font-semibold whitespace-nowrap text-white">Timetabler</span>
            </router-link>

            <div class="text-xl text-white font-medium space-x-8">
                <router-link to="/">
                    Availabilities
                </router-link>
    
                <router-link to="/schedule">
                    Schedule
                </router-link>

                <router-link to="/insert">
                    Insert Data
                </router-link>
            </div>

        </div>
    </nav>
</template>

<script>
export default {
    name: 'Navbar',
    data() {
        return {

        }
    }
}
</script>