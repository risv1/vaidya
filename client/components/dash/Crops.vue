<script setup lang="ts">
const newCrop = useState('newCrop', () => {
    return {
        type: 'wheat',
        npk: {
            n: 0,
            p: 0,
            k: 0
        }
    }
})

const addCrop = () => {
    console.log(newCrop)
}

const pestDiseaseRisks = ref([
    {
        name: 'Fungal Disease Risk',
        condition: 'High humidity forecast',
        status: 'High Risk',
        icon: 'M12 3c2.755 0 5.455.232 8.083.678.533.09.917.556.917 1.096v1.044a2.25 2.25 0 01-.659 1.591l-5.432 5.432a2.25 2.25 0 00-.659 1.591v2.927a2.25 2.25 0 01-1.244 2.013L9.75 21v-6.568a2.25 2.25 0 00-.659-1.591L3.659 7.409A2.25 2.25 0 013 5.818V4.774c0-.54.384-1.006.917-1.096A48.32 48.32 0 0112 3z',
        iconBg: 'bg-red-500/10',
        iconColor: 'text-red-500',
        statusClass: 'bg-red-500/10 text-red-500'
    },
    {
        name: 'Pest Infestation Risk',
        condition: 'High temperature forecast',
        status: 'Medium Risk',
        icon: 'M12 3c2.755 0 5.455.232 8.083.678.533.09.917.556.917 1.096v1.044a2.25 2.25 0 01-.659 1.591l-5.432 5.432a2.25 2.25 0 00-.659 1.591v2.927a2.25 2.25 0 01-1.244 2.013L9.75 21v-6.568a2.25 2.25 0 00-.659-1.591L3.659 7.409A2.25 2.25 0 013 5.818V4.774c0-.54.384-1.006.917-1.096A48.32 48.32 0 0112 3z',
        iconBg: 'bg-yellow-500/10',
        iconColor: 'text-yellow-500',
        statusClass: 'bg-yellow-500/10 text-yellow-500'
    }
])
</script>

<template>
    <div class="space-y-6 pb-5">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                <div class="flex items-center">
                    <div class="p-2 bg-emerald-500/10 rounded-lg">
                        <div class="w-8 h-8 text-emerald-500">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" />
                            </svg>
                        </div>
                    </div>
                    <div class="ml-4">
                        <p class="text-sm font-medium text-gray-400">Active Crops</p>
                        <p class="text-2xl font-semibold text-white">12</p>
                    </div>
                </div>
            </div>
            <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                <div class="flex items-center">
                    <div class="p-2 bg-blue-500/10 rounded-lg">
                        <div class="w-8 h-8 text-blue-500">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5" />
                            </svg>
                        </div>
                    </div>
                    <div class="ml-4">
                        <p class="text-sm font-medium text-gray-400">Expected Yield</p>
                        <p class="text-2xl font-semibold text-white">6.8 tons</p>
                    </div>
                </div>
            </div>
            <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                <div class="flex items-center">
                    <div class="p-2 bg-purple-500/10 rounded-lg">
                        <div class="w-8 h-8 text-purple-500">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M2.25 15a4.5 4.5 0 004.5 4.5H18a3.75 3.75 0 001.332-7.257 3 3 0 00-3.758-3.848 5.25 5.25 0 00-10.233 2.33A4.502 4.502 0 002.25 15z" />
                            </svg>
                        </div>
                    </div>
                    <div class="ml-4">
                        <p class="text-sm font-medium text-gray-400">Weather Risk</p>
                        <p class="text-2xl font-semibold text-white">Low</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div class="lg:col-span-1">
                <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                    <h3 class="text-lg font-medium text-white mb-4">Add New Crop</h3>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-400 mb-1">Crop Type</label>
                            <select v-model="newCrop.type"
                                class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-2 text-white">
                                <option value="wheat">Wheat</option>
                                <option value="rice">Rice</option>
                                <option value="corn">Corn</option>
                                <option value="soybeans">Soybeans</option>
                            </select>
                        </div>
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <label class="block text-sm font-medium text-gray-400 mb-1">N Value</label>
                                <input v-model="newCrop.npk.n" type="number"
                                    class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-2 text-white">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-400 mb-1">P Value</label>
                                <input v-model="newCrop.npk.p" type="number"
                                    class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-2 text-white">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-400 mb-1">K Value</label>
                                <input v-model="newCrop.npk.k" type="number"
                                    class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-2 text-white">
                            </div>
                        </div>
                        <button @click="addCrop"
                            class="w-full px-4 py-2 bg-gradient-to-r from-sky-500 to-blue-600 text-white rounded-lg shadow-lg shadow-sky-500/25 hover:shadow-sky-500/40 hover:scale-105 transition-all duration-300">
                            Add Crop
                        </button>
                    </div>
                </div>

                <div class="p-6 bg-white/5 mt-5 backdrop-blur-xl border border-white/10 rounded-xl">
                    <h3 class="text-lg font-medium text-white mb-4">7-Day Weather Forecast</h3>
                    <div class="grid grid-cols-7 gap-4">
                        <div v-for="i in 7" :key="i" class="text-center">
                            <p class="text-sm text-gray-400">{{ ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][i - 1]
                                }}</p>
                            <div class="my-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mx-auto text-yellow-500"
                                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z" />
                                </svg>
                            </div>
                            <p class="text-white font-medium">{{ 20 + Math.floor(Math.random() * 8) }}°C</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="lg:col-span-2 space-y-6">

                <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                    <h3 class="text-lg font-medium text-white mb-4">Crop Health Status</h3>
                    <div class="space-y-4">
                        <div class="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                            <span class="text-gray-400">Soil Moisture</span>
                            <div class="w-64 h-2 bg-white/10 rounded-full overflow-hidden">
                                <div class="h-full w-3/4 bg-gradient-to-r from-sky-500 to-blue-600"></div>
                            </div>
                            <span class="text-white">75%</span>
                        </div>
                        <div class="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                            <span class="text-gray-400">Nutrient Levels</span>
                            <div class="w-64 h-2 bg-white/10 rounded-full overflow-hidden">
                                <div class="h-full w-4/5 bg-gradient-to-r from-emerald-500 to-green-600"></div>
                            </div>
                            <span class="text-white">80%</span>
                        </div>
                        <div class="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                            <span class="text-gray-400">Growth Rate</span>
                            <div class="w-64 h-2 bg-white/10 rounded-full overflow-hidden">
                                <div class="h-full w-2/3 bg-gradient-to-r from-yellow-500 to-orange-600"></div>
                            </div>
                            <span class="text-white">66%</span>
                        </div>
                    </div>
                </div>

                <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                    <h3 class="text-lg font-medium text-white mb-4">Pest & Disease Risk Monitor</h3>
                    <div class="space-y-4">
                        <div v-for="(risk, index) in pestDiseaseRisks" :key="index"
                            class="flex items-center justify-between p-4 bg-white/5 rounded-lg">
                            <div class="flex items-center">
                                <div :class="`p-2 ${risk.iconBg} rounded-lg mr-3`">
                                    <div :class="`w-6 h-6 ${risk.iconColor}`">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                            stroke-width="1.5" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" :d="risk.icon" />
                                        </svg>
                                    </div>
                                </div>
                                <div>
                                    <h4 class="text-white font-medium">{{ risk.name }}</h4>
                                    <p class="text-sm text-gray-400">{{ risk.condition }}</p>
                                </div>
                            </div>
                            <div :class="`px-3 py-1 rounded-full text-sm font-medium ${risk.statusClass}`">
                                {{ risk.status }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>