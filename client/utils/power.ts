type MyLocation = {
    lat: number;
    lon: number;
}

export const solarData = ref({
    currentOutput: 0,
    daily: 0,
    weekly: 0,
    monthly: 0
});

export const windData = ref({
    currentOutput: 0,
    daily: 0,
    weekly: 0,
    monthly: 0
});

export const batteryData = ref({
    chargeLevel: 85,
    capacity: 13.5,
    input: 2.4,
    output: 1.2
});

export const gridData = ref({
    currentUsage: 1.6,
    daily: 12,
    weekly: 84,
    monthly: 360
});

export const loading = ref(true);
export const error = ref<string | null>(null);

export const fetchPowerData = async (coords: Ref<MyLocation>) => {
    try {
        loading.value = true;
        error.value = null;

        const response = await fetch('http://localhost:8000/power', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                lat: coords.value.lat,
                lon: coords.value.lon
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data?.solar?.predicted_power_kw) {
            const predictedSolarPower = data.solar.predicted_power_kw;
            solarData.value = {
                currentOutput: parseFloat((predictedSolarPower / 1000).toFixed(1)),
                daily: Math.round(predictedSolarPower * 24 / 1000),
                weekly: Math.round(predictedSolarPower * 24 * 7 / 1000),
                monthly: Math.round(predictedSolarPower * 24 * 30 / 1000)
            };
        }

        if (data?.wind?.predicted_power) {
            const predictedWindPower = data.wind.predicted_power;
            windData.value = {
                currentOutput: predictedWindPower.toFixed(1),
                daily: Math.round(predictedWindPower * 24),
                weekly: Math.round(predictedWindPower * 24 * 7),
                monthly: Math.round(predictedWindPower * 24 * 30)
            };
        }

    } catch (err) {
        error.value = 'Failed to fetch power data. Please try again later.';
        console.error('Error fetching power data:', err);
    } finally {
        loading.value = false;
    }
};
