import requests

API_KEY = "Your_API_Key"
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

def get_supported_currencies():
    try:
        response = requests.get(f"{API_URL}/latest/USD")
        data = response.json()
        if data.get("result") == "success":
            return list(data["conversion_rates"].keys())
        else:
            print("Error:", data.get("error-type"))
            return []
    except Exception as e:
        print("Error fetching currencies:", e)
        return []

def get_conversion_rate(base, target):
    try:
        url = f"{API_URL}/latest/{base}"
        print("Fetching:", url)
        response = requests.get(url)
        data = response.json()
        if data.get("result") == "success":
            return data["conversion_rates"].get(target)
        else:
            print("Error:", data.get("error-type"))
            return None
    except Exception as e:
        print("Error fetching conversion rate:", e)
        return None
