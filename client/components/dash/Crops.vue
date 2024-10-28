<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';

type Disease = {
    name: string;
    description: string;
}

type Pest = {
    name: string;
    description: string;
}

type CropRecommendation = {
    crop: string;
    confidence: number;
    soil_requirements: {
        N: number;
        P: number;
        K: number;
        pH: number;
    };
    estimated_price: number;
    pests: Pest[];
    diseases: Disease[];
}

const cropRecommendations = ref<CropRecommendation[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

const lat = (12.9 + Math.random() * 0.1).toFixed(4);
const lon = (80.2 + Math.random() * 0.1).toFixed(4);

const fetchCropData = async () => {
    loading.value = true;
    error.value = null;
    try {
        const response = await fetch('http://localhost:8000/crops_info', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ lat, lon })
        });
        const data = await response.json();
        cropRecommendations.value = data.data;
    } catch (err) {
        error.value = 'Failed to fetch crop data. Please try again later.';
        console.error('Error fetching crop data:', err);
    } finally {
        loading.value = false;
    }
};

onMounted(() => {
    fetchCropData();
});

const getRisksForCrop = (crop: CropRecommendation) => {
    const risks = [];
    
    risks.push(...crop.pests.map(pest => ({
        name: pest.name,
        condition: pest.description,
        status: 'High Risk',
        icon: 'M12 3c2.755 0 5.455.232 8.083.678.533.09.917.556.917 1.096v1.044a2.25 2.25 0 01-.659 1.591l-5.432 5.432a2.25 2.25 0 00-.659 1.591v2.927a2.25 2.25 0 01-1.244 2.013L9.75 21v-6.568a2.25 2.25 0 00-.659-1.591L3.659 7.409A2.25 2.25 0 013 5.818V4.774c0-.54.384-1.006.917-1.096A48.32 48.32 0 0112 3z',
        iconBg: 'bg-red-500/10',
        iconColor: 'text-red-500',
        statusClass: 'bg-red-500/10 text-red-500'
    })));
    
    risks.push(...crop.diseases.map(disease => ({
        name: disease.name,
        condition: disease.description,
        status: 'Medium Risk',
        icon: 'M12 3c2.755 0 5.455.232 8.083.678.533.09.917.556.917 1.096v1.044a2.25 2.25 0 01-.659 1.591l-5.432 5.432a2.25 2.25 0 00-.659 1.591v2.927a2.25 2.25 0 01-1.244 2.013L9.75 21v-6.568a2.25 2.25 0 00-.659-1.591L3.659 7.409A2.25 2.25 0 013 5.818V4.774c0-.54.384-1.006.917-1.096A48.32 48.32 0 0112 3z',
        iconBg: 'bg-yellow-500/10',
        iconColor: 'text-yellow-500',
        statusClass: 'bg-yellow-500/10 text-yellow-500'
    })));
    
    return risks;
};
</script>

<template>
    <div v-if="loading" class="flex justify-center items-center min-h-screen">
        <div class="text-white">Loading crop data...</div>
    </div>
    
    <div v-else-if="error" class="flex justify-center items-center min-h-screen">
        <div class="text-red-500">{{ error }}</div>
    </div>
    
    <div v-else class="space-y-6 pb-5">
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
                        <p class="text-sm font-medium text-gray-400">Location</p>
                        <p class="text-2xl font-semibold text-white">{{ lat }}, {{ lon }}</p>
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
                        <p class="text-sm font-medium text-gray-400">Best Crop</p>
                        <p class="text-2xl font-semibold text-white">{{ cropRecommendations[0]?.crop }}</p>
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
                        <p class="text-sm font-medium text-gray-400">Best Price</p>
                        <p class="text-2xl font-semibold text-white">₹{{ cropRecommendations[0]?.estimated_price.toFixed(2) }}</p>
                    </div>
                </div>
            </div>
        </div>

        <div v-for="crop in cropRecommendations" :key="crop.crop" class="mb-8">
            <h2 class="text-xl font-bold text-white mb-4">{{ crop.crop }} ({{ crop.confidence.toFixed(2) }}% Confidence)</h2>
            <h3 class="text-lg font-medium text-white mb-4">
                Estimated Price: ₹{{ crop.estimated_price }}</h3>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="lg:col-span-1">
                    <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                        <h3 class="text-lg font-medium text-white mb-4">Soil Requirements</h3>
                        <div class="space-y-4">
                            <div class="grid grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm font-medium text-gray-400 mb-1">Nitrogen (N)</label>
                                    <div class="text-xl text-white font-semibold">
                                        {{ crop.soil_requirements.N }}
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-400 mb-1">Phosphorous (P)</label>
                                    <div class="text-xl text-white font-semibold">
                                        {{ crop.soil_requirements.P }}
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-400 mb-1">Potassium (K)</label>
                                    <div class="text-xl text-white font-semibold">
                                        {{ crop.soil_requirements.K }}
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-400 mb-1">pH Level</label>
                                    <div class="text-xl text-white font-semibold">
                                        {{ crop.soil_requirements.pH }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-2 space-y-6">
                    <div class="p-6 bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl">
                        <h3 class="text-lg font-medium text-white mb-4">Crop Risks</h3>
                        <div class="space-y-4">
                            <div v-for="(risk, index) in getRisksForCrop(crop)" :key="index"
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
    </div>
</template>