import requests
import json 
import time

# Get data from the API's

class HeartBeat:
    def InternetCheck():
        google_response = requests.get("https://google.com")
        if google_response.status_code == 200:
            return True
        else:
            return False
        microsoft_response = requests.get("https://microsoft.com")
        if microsoft_response.status_code == 200:
            return True
        else:
            return False
        apple_response = requests.get("https://apple.com")
        if apple_response.status_code == 200:
            return True
        else:
            return False
        amazon_response = requests.get("https://amazon.com")
        if amazon_response.status_code == 200:
            return True
        else:
            return False
        facebook_response = requests.get("https://facebook.com")
        if facebook_response.status_code == 200:
            return True
        else:
            return False
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
    def RonTec():
        url = "https://www.rontec-servicestations.co.uk/fuel-prices/data/fuel_prices_data.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def SGN():
        url = "https://www.sgnretail.uk/files/data/SGN_daily_fuel_prices.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
    def Tesco():
        url = "https://www.tesco.com/fuel_prices/fuel_prices_data.json"
        #Spoof The API into thinking the codes a browser"
        headers = {Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return None
