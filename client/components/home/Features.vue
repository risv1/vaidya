<script setup lang="ts">
const features = [
    {
        title: "Energy Generation",
        description: "Predict renewable energy output based on weather patterns",
        icon: 'emojione-monotone:battery',
        gradient: "from-emerald-500 to-green-600",
        bgClass: "bg-emerald-50 dark:bg-emerald-900/20"
    },
    {
        title: "Crop Yield Forecasts",
        description: "Optimize farming with precise yield predictions",
        icon: 'mdi:leaf',
        gradient: "from-green-500 to-emerald-600",
        bgClass: "bg-green-50 dark:bg-green-900/20"
    },
    {
        title: "Planting Calendar",
        description: "Find the perfect timing for your crops",
        icon: 'emojione-monotone:sun',
        gradient: "from-yellow-500 to-orange-600",
        bgClass: "bg-yellow-50 dark:bg-yellow-900/20"
    },
    {
        title: "Pest & Disease Alerts",
        description: "Stay ahead of potential threats to your crops",
        icon: 'solar:bug-bold',
        gradient: "from-red-500 to-rose-600",
        bgClass: "bg-red-50 dark:bg-red-900/20"
    },
    {
        title: "Air Quality Impact",
        description: "Monitor health risks from air quality changes",
        icon: 'mdi:lungs',
        gradient: "from-blue-500 to-indigo-600",
        bgClass: "bg-blue-50 dark:bg-blue-900/20"
    },
    {
        title: "Weather Analytics",
        description: "Detailed weather analysis and predictions",
        icon: 'material-symbols-light:wind-power-outline',
        gradient: "from-purple-500 to-violet-600",
        bgClass: "bg-purple-50 dark:bg-purple-900/20"
    }
]
</script>

<template>
    <div id="features" class="min-h-screen py-32 relative">
        <div class="absolute inset-0 bg-gradient-to-b dark:from-gray-950 from-gray-200 dark:via-gray-900 via-gray-100 dark:to-gray-950 to-white"></div>
        <div class="absolute inset-0 overflow-hidden">
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1000px] h-[1000px] bg-gradient-to-r from-sky-500/10 to-blue-500/10 rounded-full blur-3xl"></div>
        </div>
        
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-20">
                <h2 class="text-4xl font-bold bg-gradient-to-r from-sky-400 to-blue-600 bg-clip-text text-transparent mb-6">
                    Our Features
                </h2>
                <p class="text-gray-400 max-w-2xl mx-auto text-lg">
                    Comprehensive weather analysis tools designed for modern agriculture and energy sectors
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div v-for="(feature, index) in features" :key="index"
                    class="group relative rounded-2xl overflow-hidden transition-all duration-500 hover:scale-105">
                    <div class="absolute inset-0 bg-gradient-to-br from-gray-900 to-gray-950"></div>
                    <div :class="[feature.bgClass, 'absolute inset-0']"></div>
                    <div class="relative p-8 backdrop-blur-xl bg-white/5 dark:bg-gray-900/50 h-full border border-white/10 dark:border-gray-800/50 rounded-2xl">
                        <div :class="['bg-gradient-to-r', feature.gradient, 'inline-flex p-3.5 rounded-xl text-white mb-6 shadow-lg group-hover:scale-110 group-hover:rotate-3 transition-all duration-300']">
                            <Icon :name="feature.icon" class="w-6 h-6" />
                        </div>
                        <h3 class="text-xl font-semibold dark:text-white text-gray-800 mb-4">
                            {{ feature.title }}
                        </h3>
                        <p class="dark:text-gray-400 text-gray-600">
                            {{ feature.description }}
                        </p>
                        <div class="absolute bottom-8 right-8 opacity-0 group-hover:opacity-100 transition-all duration-500 transform group-hover:translate-x-0 translate-x-4">
                            <div :class="['bg-gradient-to-r', feature.gradient, 'rounded-full p-2.5 text-white shadow-lg']">
                                <Icon name="material-symbols:chevron-right" class="w-4 h-4" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>