type MyLocation = {
    lat: number;
    lon: number;
}

export const aqi = ref<number | null>(null);

export const fetchAirQuality = async (coords: Ref<MyLocation>) => {
    try {
        const response = await fetch('http://localhost:8000/air_quality', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                lat: coords.value.lat,
                lon: coords.value.lon,
            }),
        });

        if (!response.ok) {
            throw new Error('Failed to fetch air quality data');
        }

        const data = await response.json();
        aqi.value = data.aqi;

        loading.value = false;
    } catch (err) {
        console.error(err);
        error.value = err as string;
    }
}
