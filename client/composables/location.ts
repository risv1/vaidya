type Location = { lat: number; lon: number }

export default function useLocation() {
    const { coords, error } = useGeolocation()

    const location = useState<Location | null>('location', () => {
        if (!error.value) {
            return {
                lat: coords.value?.latitude || 0,
                lon: coords.value?.longitude || 0,
            }
        } else {
            return null
        }
    })

    return { location }
}