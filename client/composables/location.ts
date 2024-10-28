type Location = { lat: number; lon: number }

export function useLocation() {
    const { coords, locatedAt, error, resume, pause } = useGeolocation()

    if (error.value) {
        return { error }
    }

    const locationData =
    {
        coords: {
            accuracy: coords.value.accuracy,
            latitude: coords.value.latitude,
            longitude: coords.value.longitude,
            altitude: coords.value.altitude,
            altitudeAccuracy: coords.value.altitudeAccuracy,
            heading: coords.value.heading,
            speed: coords.value.speed,
        },
        locatedAt,
        error: error ? error.value : error,
    }

    return { locationData, resume, pause }


}