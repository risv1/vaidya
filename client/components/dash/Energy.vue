<script setup lang="ts">
import { fetchPowerData } from '~/utils/power';

const { coords } = useLocation()

onMounted(() => {
  fetchPowerData(coords);
});
</script>

<template>
  <div class="p-6">
    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-white"></div>
    </div>

    <div v-else-if="error" class="flex justify-center items-center h-64">
      <div class="text-red-500 text-center p-4 bg-white/5 rounded-xl">
        {{ error }}
      </div>
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
        <h3 class="text-xl font-semibold text-white mb-4">Solar Generation</h3>
        <div class="space-y-4">
          <div class="p-4 bg-white/5 rounded-lg">
            <div class="flex justify-between items-center mb-2">
              <span class="text-gray-400">Current Output</span>
              <span class="text-2xl font-bold text-yellow-500">{{ solarData.currentOutput }} kW</span>
            </div>
            <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
              <div class="h-full w-3/4 bg-gradient-to-r from-yellow-500 to-orange-500"></div>
            </div>
          </div>
          <div class="grid grid-cols-3 gap-4 text-center">
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Daily</p>
              <p class="text-white font-bold">{{ solarData.daily }} kWh</p>
            </div>
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Weekly</p>
              <p class="text-white font-bold">{{ solarData.weekly }} kWh</p>
            </div>
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Monthly</p>
              <p class="text-white font-bold">{{ solarData.monthly }} kWh</p>
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
              <span class="text-2xl font-bold text-blue-500">{{ windData.currentOutput }} kW</span>
            </div>
            <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
              <div class="h-full w-1/2 bg-gradient-to-r from-blue-500 to-sky-500"></div>
            </div>
          </div>
          <div class="grid grid-cols-3 gap-4 text-center">
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Daily</p>
              <p class="text-white font-bold">{{ windData.daily }} kWh</p>
            </div>
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Weekly</p>
              <p class="text-white font-bold">{{ windData.weekly }} kWh</p>
            </div>
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Monthly</p>
              <p class="text-white font-bold">{{ windData.monthly }} kWh</p>
            </div>
          </div>
        </div>
      </div>
      <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl relative">
        <div class="absolute top-2 right-2 bg-blue-500 text-xs text-white px-2 py-1 rounded">
          Future Feature
        </div>
        <h3 class="text-xl font-semibold text-white mb-4">Battery Storage</h3>
        <div class="space-y-4">
          <div class="p-4 bg-white/5 rounded-lg">
            <div class="flex justify-between items-center mb-2">
              <span class="text-gray-400">Charge Level</span>
              <span class="text-2xl font-bold text-green-500">{{ batteryData.chargeLevel }}%</span>
            </div>
            <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
              <div 
                class="h-full bg-gradient-to-r from-green-500 to-emerald-500"
                :style="{ width: `${batteryData.chargeLevel}%` }"
              ></div>
            </div>
          </div>
          <div class="grid grid-cols-3 gap-4 text-center">
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Capacity</p>
              <p class="text-white font-bold">{{ batteryData.capacity }} kWh</p>
            </div>
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Input</p>
              <p class="text-green-500 font-bold">+{{ batteryData.input }} kW</p>
            </div>
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Output</p>
              <p class="text-red-500 font-bold">-{{ batteryData.output }} kW</p>
            </div>
          </div>
        </div>
      </div>
      <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl relative">
        <div class="absolute top-2 right-2 bg-blue-500 text-xs text-white px-2 py-1 rounded">
          Future Feature
        </div>
        <h3 class="text-xl font-semibold text-white mb-4">Grid Consumption</h3>
        <div class="space-y-4">
          <div class="p-4 bg-white/5 rounded-lg">
            <div class="flex justify-between items-center mb-2">
              <span class="text-gray-400">Current Usage</span>
              <span class="text-2xl font-bold text-purple-500">{{ gridData.currentUsage }} kW</span>
            </div>
            <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
              <div class="h-full w-1/4 bg-gradient-to-r from-purple-500 to-pink-500"></div>
            </div>
          </div>
          <div class="grid grid-cols-3 gap-4 text-center">
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Daily</p>
              <p class="text-white font-bold">{{ gridData.daily }} kWh</p>
            </div>
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Weekly</p>
              <p class="text-white font-bold">{{ gridData.weekly }} kWh</p>
            </div>
            <div class="p-3 bg-white/5 rounded-lg">
              <p class="text-gray-400 text-sm">Monthly</p>
              <p class="text-white font-bold">{{ gridData.monthly }} kWh</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>