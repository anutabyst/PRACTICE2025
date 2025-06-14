from fastapi import FastAPI, Header, HTTPException, Query
import requests

app = FastAPI()

API_KEY = "my-secret-key"

def verify_api_key(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

@app.get("/holidays")
def get_holidays(
    country: str = Query("US", min_length=2, max_length=2),
    count: int = Query(5, ge=1, le=20),
    api_key: str = Header(None, alias="api-key")
):
    verify_api_key(api_key)

    # Приклад API для свят — Nager.Date (без ключа, для демо)
    url = f"https://date.nager.at/api/v3/NextPublicHolidays/{country.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch holidays"}

    holidays = response.json()

    # Відбираємо лише перші count свят
    nearest_holidays = holidays[:count]

    # Форматуємо відповідь
    result = []
    for holiday in nearest_holidays:
        result.append({
            "date": holiday["date"],
            "localName": holiday["localName"],
            "name": holiday["name"],
            "countryCode": holiday["countryCode"]
        })

    return {"holidays": result}
