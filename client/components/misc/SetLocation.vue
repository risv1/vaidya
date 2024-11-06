<script setup lang="ts">
const { coords } = useLocation();
const isOpen = ref(false);
const toggleOpen = () => isOpen.value = !isOpen.value;
defineProps<{
    submitHandler: (lat: number, lon: number) => void
}>()
</script>

<template>
    <div class="relative w-fit h-fit group">
        <button 
            @click="toggleOpen" 
            class="w-12 h-12 bg-neutral-950 rounded-full flex justify-center items-center border border-neutral-800 shadow-lg transform transition-all duration-300 hover:scale-110 hover:border-blue-500 hover:shadow-blue-500/20 hover:shadow-xl"
        >
            <Icon 
                name="mdi:location" 
                class="w-6 h-6 text-blue-400 group-hover:text-blue-500 transition-colors duration-300" 
            />
        </button>
    </div>

    <Transition
        enter-active-class="transition duration-300 ease-out"
        enter-from-class="transform scale-95 opacity-0"
        enter-to-class="transform scale-100 opacity-100"
        leave-active-class="transition duration-200 ease-in"
        leave-from-class="transform scale-100 opacity-100"
        leave-to-class="transform scale-95 opacity-0"
    >
        <div 
            v-if="isOpen" 
            @click="toggleOpen" 
            class="w-screen h-screen fixed top-0 left-0 bg-black/60 backdrop-blur-sm flex justify-center items-center z-50"
        >
            <form 
                @click="(event)=>event.stopPropagation()" 
                class="w-full max-w-md mx-4 bg-neutral-950 border border-neutral-800 rounded-lg shadow-2xl shadow-blue-500/10 transform transition-all duration-300 hover:shadow-blue-500/20"
            >
                <div class="p-6 space-y-4">
                    <h2 class="text-xl font-semibold text-white mb-6">Set Location</h2>
                    
                    <div class="space-y-4">
                        <div class="relative">
                            <input 
                                v-model="coords.lat" 
                                type="text"
                                class="w-full h-12 px-4 bg-neutral-900 border border-neutral-800 rounded-lg text-white placeholder-neutral-500 transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500"
                                placeholder="Latitude" 
                            />
                        </div>
                        
                        <div class="relative">
                            <input 
                                v-model="coords.lon" 
                                type="text"
                                class="w-full h-12 px-4 bg-neutral-900 border border-neutral-800 rounded-lg text-white placeholder-neutral-500 transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500"
                                placeholder="Longitude" 
                            />
                        </div>
                    </div>

                    <button 
                        @click="(e) => {
                            e.preventDefault()
                            submitHandler(coords.lat, coords.lon)
                            isOpen = !isOpen
                        }" 
                        class="w-full h-12 mt-6 bg-blue-500 text-white font-medium rounded-lg transform transition-all duration-300 hover:bg-blue-600 hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-blue-500/50 active:scale-[0.98]"
                    >
                        Set Location
                    </button>
                </div>
            </form>
        </div>
    </Transition>
</template>