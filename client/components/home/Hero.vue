<template>
    <div class="relative h-screen flex items-center justify-center overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br dark:from-gray-900 from-gray-200 dark:via-gray-950 via-gray-100  dark:to-black to-white"></div>
        <div class="absolute inset-0 bg-[url('/grid.svg')] bg-center [mask-image:linear-gradient(180deg,white,rgba(255,255,255,0))] opacity-20"></div>
        
        <div class="absolute inset-0 overflow-hidden">
            <div class="absolute -inset-[10px] opacity-50">
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-gradient-to-r from-sky-500/30 to-blue-500/30 rounded-full blur-3xl"></div>
                <div class="absolute top-1/2 left-1/3 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-gradient-to-r from-purple-500/20 to-violet-500/20 rounded-full blur-3xl"></div>
            </div>
        </div>
        
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 py-10">
            <div class="text-center">
                <h1 class="text-3xl md:text-7xl font-bold bg-gradient-to-r from-sky-400 via-blue-500 to-blue-600 bg-clip-text text-transparent mb-10 py-5">
                    Vaidya: Weather-Powered Intelligence
                </h1>
                <p class="text-xl md:text-2xl text-gray-400 max-w-3xl mx-auto mb-12 leading-relaxed">
                    Transform weather data into actionable insights for agriculture, energy, and health.
                </p>
                <div class="flex justify-center space-x-6">
                    <NuxtLink to="/dash" class="hover:cursor-pointer px-8 py-4 bg-gradient-to-r from-sky-500 to-blue-600 text-white rounded-xl shadow-lg shadow-sky-500/25 hover:shadow-sky-500/40 hover:scale-105 transition-all duration-300">
                        Get Started
                    </NuxtLink>
                    <button class="px-8 py-4 dark:bg-white/5 bg-neutral-800 backdrop-blur-xl border border-white/10 text-white rounded-xl shadow-lg dark:hover:bg-white/10 hover:bg-neutral-600 hover:scale-105 transition-all duration-300">
                        Learn More
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>