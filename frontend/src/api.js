const base = "https://localhost:8000";

export async function handleRes(res) {
    if(!res.ok){
        const text = await res.text().catch(()=>null);
        throw new Error(text || `HTTP ${res.status}`);
    }

    return res.json()
}