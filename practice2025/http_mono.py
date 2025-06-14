import requests

def get_exchange_rate(currency_code_from: int, currency_code_to: int):
    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)

    if response.status_code != 200:
        print("Не вдалося отримати дані від Monobank")
        return None

    rates = response.json()
    
    for rate in rates:
        
        if rate["currencyCodeA"] == currency_code_from and rate["currencyCodeB"] == currency_code_to:
            buy = rate.get("rateBuy")
            sell = rate.get("rateSell")
            return buy, sell
    
    print("Курс для заданої пари не знайдено")
    return None


currency_from = 840  
currency_to = 980   
result = get_exchange_rate(currency_from, currency_to)

if result:
    buy, sell = result
git --version
    print(f"Курс {currency_from} -> {currency_to}: Покупка = {buy}, Продаж = {sell}")
