import requests
import json 
import time

# Get data from the API's


class GetData:
    def Sainsburys():
        url = "https://api.sainsburys.co.uk/v1/exports/latest/fuel_prices_data.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Shell():
        url = "https://www.shell.co.uk/fuel-prices-data.html"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def AppleGreen():
        url = "https://applegreenstores.com/fuel-prices/data.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Ascona():
        url = "https://fuelprices.asconagroup.co.uk/newfuel.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Asda():
        url = "https://storelocator.asda.com/fuel_prices_data.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def BP():
        url = "https://www.bp.com/en_gb/united-kingdom/home/fuelprices/fuel_prices_data.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def ET():
        url = "https://fuelprices.esso.co.uk/latestdata.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Jet():
        url = "https://jetlocal.co.uk/fuel_prices_data.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Karen():
        url = "https://api2.krlmedia.com/integration/live_price/krl"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Morisons():
        url = "https://www.morrisons.com/fuel-prices/fuel.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Moto():
        url = "https://moto-way.com/fuel-price/fuel_prices.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Motor():
        url = "https://fuel.motorfuelgroup.com/fuel_prices_data.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None