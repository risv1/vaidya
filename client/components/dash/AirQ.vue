<template>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
            <h3 class="text-xl font-semibold text-white mb-4">Air Quality Index</h3>
            <div class="space-y-4">
                <div class="flex items-center justify-between p-4 bg-white/5 rounded-lg">
                    <div>
                        <p class="text-gray-400">Current AQI</p>
                        <p class="text-3xl font-bold text-green-500">65</p>
                    </div>
                    <div class="text-right">
                        <p class="text-white font-medium">Moderate</p>
                        <p class="text-gray-400 text-sm">Updated 5 min ago</p>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="p-3 bg-white/5 rounded-lg">
                        <p class="text-gray-400 text-sm">PM2.5</p>
                        <p class="text-white font-bold">18 µg/m³</p>
                    </div>
                    <div class="p-3 bg-white/5 rounded-lg">
                        <p class="text-gray-400 text-sm">PM10</p>
                        <p class="text-white font-bold">35 µg/m³</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
            <h3 class="text-xl font-semibold text-white mb-4">Health Advisory</h3>
            <div class="space-y-4">
                <div class="p-4 bg-white/5 rounded-lg">
                    <h4 class="text-lg text-white mb-2">Current Conditions</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li class="flex items-center">
                            <span class="w-2 h-2 bg-yellow-500 rounded-full mr-2"></span>
                            Moderate pollen levels - possible allergy triggers
                        </li>
                        <li class="flex items-center">
                            <span class="w-2 h-2 bg-green-500 rounded-full mr-2"></span>
                            Good conditions for outdoor activities
                        </li>
                    </ul>
                </div>
                <div class="p-4 bg-white/5 rounded-lg">
                    <h4 class="text-lg text-white mb-2">Recommendations</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li class="flex items-center">
                            <span class="w-2 h-2 bg-blue-500 rounded-full mr-2"></span>
                            Keep windows closed during peak pollen hours
                        </li>
                        <li class="flex items-center">
                            <span class="w-2 h-2 bg-blue-500 rounded-full mr-2"></span>
                            Best time for outdoor exercise: Early morning
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
            <h3 class="text-xl font-semibold text-white mb-4">UV Index & Weather</h3>
            <div class="space-y-4">
                <div class="flex items-center justify-between p-4 bg-white/5 rounded-lg">
                    <div>
                        <p class="text-gray-400">UV Index</p>
                        <p class="text-3xl font-bold text-orange-500">8</p>
                    </div>
                    <div class="text-right">
                        <p class="text-white font-medium">Very High</p>
                        <p class="text-gray-400 text-sm">Peak at 1 PM</p>
                    </div>
                </div>
                <div class="grid grid-cols-3 gap-4">
                    <div class="p-3 bg-white/5 rounded-lg">
                        <p class="text-gray-400 text-sm">Temperature</p>
                        <p class="text-white font-bold">28°C</p>
                    </div>
                    <div class="p-3 bg-white/5 rounded-lg">
                        <p class="text-gray-400 text-sm">Humidity</p>
                        <p class="text-white font-bold">65%</p>
                    </div>
                    <div class="p-3 bg-white/5 rounded-lg">
                        <p class="text-gray-400 text-sm">Wind</p>
                        <p class="text-white font-bold">12 km/h</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
            <h3 class="text-xl font-semibold text-white mb-4">Indoor Environment</h3>
            <div class="space-y-4">
                <div class="grid grid-cols-2 gap-4">
                    <div class="p-4 bg-white/5 rounded-lg">
                        <p class="text-gray-400">CO2 Levels</p>
                        <div class="flex items-end justify-between">
                            <p class="text-2xl font-bold text-white">450</p>
                            <p class="text-gray-400 text-sm">ppm</p>
                        </div>
                    </div>
                    <div class="p-4 bg-white/5 rounded-lg">
                        <p class="text-gray-400">VOC Levels</p>
                        <div class="flex items-end justify-between">
                            <p class="text-2xl font-bold text-green-500">Low</p>
                            <p class="text-gray-400 text-sm">125 ppb</p>
                        </div>
                    </div>
                </div>
                <div class="p-4 bg-white/5 rounded-lg">
                    <h4 class="text-lg text-white mb-2">Comfort Index</h4>
                    <div class="flex items-center justify-between">
                        <div class="space-y-1">
                            <p class="text-gray-400 text-sm">Temperature</p>
                            <div class="w-32 h-2 bg-white/10 rounded-full overflow-hidden">
                                <div class="h-full w-3/4 bg-green-500"></div>
                            </div>
                        </div>
                        <div class="space-y-1">
                            <p class="text-gray-400 text-sm">Humidity</p>
                            <div class="w-32 h-2 bg-white/10 rounded-full overflow-hidden">
                                <div class="h-full w-1/2 bg-green-500"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>