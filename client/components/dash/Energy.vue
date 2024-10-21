<template>
    <div class="p-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                <h3 class="text-xl font-semibold text-white mb-4">Solar Generation</h3>
                <div class="space-y-4">
                    <div class="p-4 bg-white/5 rounded-lg">
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-gray-400">Current Output</span>
                            <span class="text-2xl font-bold text-yellow-500">4.2 kW</span>
                        </div>
                        <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                            <div class="h-full w-3/4 bg-gradient-to-r from-yellow-500 to-orange-500"></div>
                        </div>
                    </div>
                    <div class="grid grid-cols-3 gap-4 text-center">
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Daily</p>
                            <p class="text-white font-bold">32 kWh</p>
                        </div>
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Weekly</p>
                            <p class="text-white font-bold">224 kWh</p>
                        </div>
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Monthly</p>
                            <p class="text-white font-bold">960 kWh</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                <h3 class="text-xl font-semibold text-white mb-4">Wind Generation</h3>
                <div class="space-y-4">
                    <div class="p-4 bg-white/5 rounded-lg">
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-gray-400">Current Output</span>
                            <span class="text-2xl font-bold text-blue-500">2.8 kW</span>
                        </div>
                        <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                            <div class="h-full w-1/2 bg-gradient-to-r from-blue-500 to-sky-500"></div>
                        </div>
                    </div>
                    <div class="grid grid-cols-3 gap-4 text-center">
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Daily</p>
                            <p class="text-white font-bold">24 kWh</p>
                        </div>
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Weekly</p>
                            <p class="text-white font-bold">168 kWh</p>
                        </div>
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Monthly</p>
                            <p class="text-white font-bold">720 kWh</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                <h3 class="text-xl font-semibold text-white mb-4">Battery Storage</h3>
                <div class="space-y-4">
                    <div class="p-4 bg-white/5 rounded-lg">
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-gray-400">Charge Level</span>
                            <span class="text-2xl font-bold text-green-500">85%</span>
                        </div>
                        <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                            <div class="h-full w-[85%] bg-gradient-to-r from-green-500 to-emerald-500"></div>
                        </div>
                    </div>
                    <div class="grid grid-cols-3 gap-4 text-center">
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Capacity</p>
                            <p class="text-white font-bold">13.5 kWh</p>
                        </div>
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Input</p>
                            <p class="text-green-500 font-bold">+2.4 kW</p>
                        </div>
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Output</p>
                            <p class="text-red-500 font-bold">-1.2 kW</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                <h3 class="text-xl font-semibold text-white mb-4">Grid Consumption</h3>
                <div class="space-y-4">
                    <div class="p-4 bg-white/5 rounded-lg">
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-gray-400">Current Usage</span>
                            <span class="text-2xl font-bold text-purple-500">1.6 kW</span>
                        </div>
                        <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                            <div class="h-full w-1/4 bg-gradient-to-r from-purple-500 to-pink-500"></div>
                        </div>
                    </div>
                    <div class="grid grid-cols-3 gap-4 text-center">
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Daily</p>
                            <p class="text-white font-bold">12 kWh</p>
                        </div>
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Weekly</p>
                            <p class="text-white font-bold">84 kWh</p>
                        </div>
                        <div class="p-3 bg-white/5 rounded-lg">
                            <p class="text-gray-400 text-sm">Monthly</p>
                            <p class="text-white font-bold">360 kWh</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>