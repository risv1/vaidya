<script setup>

const tabs = [
    { id: 'crops', name: 'Crop Analysis' },
    { id: 'energy', name: 'Energy Usage' },
    { id: 'health', name: 'Air Quality' }
]

const currentTab = ref('crops')
const isDropdownOpen = ref(false)
const isNotifsOpen = ref(false)

const userNavigation = [
    { name: 'Your Profile', icon: "mdi:user" },
    { name: 'Settings', icon: "mi:settings" },
    { name: 'Sign out', icon: "material-symbols:logout" }
]

const notifications = ref([
    {
        id: 1,
        title: 'New Analytics Report',
        description: 'Monthly analysis is ready for review',
        time: '1h ago'
    },
    {
        id: 2,
        title: 'System Update',
        description: 'New features available',
        time: '3h ago'
    }
])
</script>

<template>
    <main
        class="relative min-h-screen bg-gradient-to-br dark:from-gray-900 from-gray-200 dark:via-gray-950 via-gray-100 dark:to-black to-white">
        <div
            class="absolute inset-0 bg-[url('/grid.svg')] bg-center [mask-image:linear-gradient(180deg,white,rgba(255,255,255,0))] opacity-20">
        </div>
        <div class="absolute inset-0 overflow-hidden">
            <div class="absolute -inset-[10px] opacity-50">
                <div
                    class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-gradient-to-r from-sky-500/30 to-blue-500/30 rounded-full blur-3xl">
                </div>
                <div
                    class="absolute top-1/2 left-1/3 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-gradient-to-r from-purple-500/20 to-violet-500/20 rounded-full blur-3xl">
                </div>
            </div>
        </div>
        <header class="relative z-20">
            <nav class="border-b border-white/10 backdrop-blur-xl">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex justify-between items-center h-16">
                        <div class="flex items-center">
                            <h1 class="text-xl font-bold text-white">Dashboard</h1>
                        </div>
                        <div class="flex items-center space-x-4">
                            <div class="relative">
                                <button @click="isNotifsOpen = !isNotifsOpen"
                                    class="p-2 text-gray-400 hover:text-white rounded-lg hover:bg-white/10">
                                    <Icon name="mdi:bell" class="h-5 w-5" />
                                </button>
                                <div v-if="isNotifsOpen"
                                    class="absolute right-10 mt-2 w-80 rounded-lg bg-white/10 backdrop-blur-xl shadow-lg focus:outline-none z-30">
                                    <div class="p-4">
                                        <h3 class="text-sm font-medium text-white mb-3">Notifications</h3>
                                        <div class="space-y-3">
                                            <div v-for="notification in notifications" :key="notification.id"
                                                class="flex p-3 rounded-lg hover:bg-white/10">
                                                <div class="flex-1 min-w-0">
                                                    <p class="text-sm font-medium text-white">
                                                        {{ notification.title }}
                                                    </p>
                                                    <p class="text-sm text-gray-400">
                                                        {{ notification.description }}
                                                    </p>
                                                    <p class="text-xs text-gray-500">{{ notification.time }}</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="relative ml-3">
                                <button @click="isDropdownOpen = !isDropdownOpen"
                                    class="flex items-center space-x-2 p-2 text-gray-400 hover:text-white rounded-lg hover:bg-white/10">
                                    <span class="h-8 w-8 rounded-full bg-gradient-to-r from-sky-500 to-blue-600"></span>
                                    <Icon name="mdi:chevron-down" class="h-4 w-4" />
                                </button>

                                <div v-if="isDropdownOpen"
                                    class="absolute right-0 mt-2 w-48 rounded-lg bg-white/10 backdrop-blur-xl shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                                    <div class="py-1">
                                        <a v-for="item in userNavigation" :key="item.name" href="#"
                                            class="flex items-center px-4 py-2 text-sm text-gray-300 hover:bg-white/10">
                                            <Icon :name="item.icon" class="h-4 w-4 mr-2" />
                                            {{ item.name }}
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </nav>
        </header>
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8">
            <div class="flex justify-center mb-8">
                <div class="inline-flex p-1 bg-white/10 backdrop-blur-xl rounded-xl">
                    <button v-for="tab in tabs" :key="tab.id" @click="currentTab = tab.id" :class="[
                        'px-6 py-2.5 rounded-lg text-sm font-medium transition-all duration-300',
                        currentTab === tab.id
                            ? 'bg-gradient-to-r from-sky-500 to-blue-600 text-white shadow-lg shadow-sky-500/25'
                            : 'text-gray-400 hover:text-white'
                    ]">
                        {{ tab.name }}
                    </button>
                </div>
            </div>
            <DashCrops v-if="currentTab === 'crops'" />
            <DashEnergy v-else-if="currentTab === 'energy'" />
            <DashAirQ v-else-if="currentTab === 'health'" />
        </div>
    </main>
</template>