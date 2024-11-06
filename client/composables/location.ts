type MyLocation = {
    lat: number;
    lon: number;
}

export function useLocation() {
    const coords = useState<MyLocation>('location', ()=>{ 
        return {
            lat: 12.8230,
            lon: 80.0444,
        }
     });

     return {
            coords
     }
}