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

type MyLocation = {
    lat: number;
    lon: number;
}

export const cropRecommendations = ref<CropRecommendation[]>([]);
export const loading = ref(true);
export const error = ref<string | null>(null);

export const fetchCropData = async (coords: Ref<MyLocation>) => {
    loading.value = true;
    error.value = null;
    try {
        const response = await fetch('http://localhost:8000/crops_info', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                lat: coords.value.lat,
                lon: coords.value.lon
            })
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