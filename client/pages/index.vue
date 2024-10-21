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
    <main class="bg-white dark:bg-gray-900 transition-colors duration-300">
        <div class="bg-gray-50 dark:bg-gray-950 transition-colors duration-300">
            <HomeNav />
            <HomeHero />
            <HomeFeatures :features="features" />
            <HomeFooter />
        </div>
    </main>
</template>
