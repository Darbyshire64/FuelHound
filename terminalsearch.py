import getdata
import json
import requests
# Welcome User
print("Welcome To Fuel Price Directory")

print("Initialising And Testing Integrity")
# Initialize an array to store matching stations
matching_stations = []
successping = 0
totalping = 0
match = 0


try:
    GetDATAReturn = getdata.HeartBeat.HeartBeat()
    print(GetDATAReturn)
except:
    print("Error: GetDataModule Not Found")
    exit()


try:
    requests.head("http://www.google.com/", timeout=30)
    print('The internet connection is Stable')
except requests.ConnectionError:
    print("The internet connection is down")


# Gather Search Data
postal = input("Enter The First Section of Your Postal Code: ")

#Validate Data
if len(postal) > 4:
    print("Invalid Postal Code")
    exit()
try:
    postal = str(postal)
except:
    print("Invalid Postal Code")
    exit()


print("Searching For Stations Near You")
# Sainsbury's
Sbdata = getdata.GetData.Sainsburys()
if Sbdata is not None:
    # Parse the data
    sbdataprocessing = json.loads(Sbdata)

    # Iterate through the data and match the postal code
    for site in sbdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1
            

    print("Sainsburys: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

    

SHLdata = getdata.GetData.Shell()
if SHLdata is not None:
    # Parse the data
    SHLdataprocessing = json.loads(SHLdata)

    # Find DataTime

    # Iterate through the data and match the postal code
    for site in SHLdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1

    print("Shell: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1


AGdata = getdata.GetData.AppleGreen()
if AGdata is not None:
    # Parse the data
    AGdataprocessing = json.loads(AGdata)

    # Iterate through the data and match the postal code
    for site in AGdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1

    print("AppleGreen: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

Adata = getdata.GetData.Ascona()
if Adata is not None:
    # Parse the data
    Adataprocessing = json.loads(Adata)


    # Iterate through the data and match the postal code
    for site in Adataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1

    print("Ascona: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

ASdata = getdata.GetData.Asda()
if ASdata is not None:
    # Parse the data
    ASdataprocessing = json.loads(ASdata)

    # Find DataTime

    # Iterate through the data and match the postal code
    for site in ASdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1

    print("Asda: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1


Bdata = getdata.GetData.BP()
if Bdata is not None:
    # Parse the data
    Bdataprocessing = json.loads(Bdata)


    # Iterate through the data and match the postal code
    for site in Bdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1

    print("Bp: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1


ETdata = getdata.GetData.ET()
if ETdata is not None:
    # Parse the data
    ETdataprocessing = json.loads(ETdata)

    # Iterate through the data and match the postal code
    for site in ETdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1
    print("Esso Tesco: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

Jetdata = getdata.GetData.Jet()
if Jetdata is not None:
    # Parse the data
    Jetdataprocessing = json.loads(Jetdata)

    # Iterate through the data and match the postal code
    for site in Jetdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1

    print("Jet: Complete")
Karendata = getdata.GetData.Karen()
if Karendata is not None:

    # Parse the data
    Karendataprocessing = json.loads(Karendata)

    # Iterate through the data and match the postal code
    for site in Karendataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1
    totalping = totalping + 1
    successping = successping + 1
    print("Karen Retail: Complete")
else:
    totalping = totalping + 1

    
Morrisondata = getdata.GetData.Morisons()
if Morrisondata is not None:
    # Parse the data
    Morrisondataprocessing = json.loads(Morrisondata)

    # Iterate through the data and match the postal code
    for site in Morrisondataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1
    print("Morrison Search: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

Motodata = getdata.GetData.Moto()
if Motodata is not None:
    # Parse the data
    Motodataprocessing = json.loads(Motodata)

    # Iterate through the data and match the postal code
    for site in Motodataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1
    print("Moto Search: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

motordata = getdata.GetData.Motor()
if motordata is not None:
    # Parse the data
    motordataprocessing = json.loads(motordata)

    # Iterate through the data and match the postal code
    for site in motordataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1
    print("Motor Search: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

rontecdata = getdata.GetData.RonTec()
if rontecdata is not None:
    # Parse the data
    rontecdataprocessing = json.loads(rontecdata)

    # Iterate through the data and match the postal code
    for site in rontecdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1
    print("Rontec: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

sgndata = getdata.GetData.SGN()
if sgndata is not None:
    # Parse the data
    sgndataprocessing = json.loads(sgndata)

    # Iterate through the data and match the postal code
    for site in sgndataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            match = match + 1
    print("SGN: Complete")
    totalping = totalping + 1
    successping = successping + 1
else:
    totalping = totalping + 1

print("Search Complete")
print(f"Total Companys: {totalping}")
print(f"Successful Requests: {successping}")
print(f"Matching Stations Found: {match}")


# Find the cheapest station for each fuel type
cheapest_stations = {'E10': None, 'E5': None, 'B7': None}
cheapest_prices = {'E10': float('inf'), 'E5': float('inf'), 'B7': float('inf')}

for station in matching_stations:
    for fuel_type in ['E10', 'E5', 'B7']:
        if fuel_type in station['prices'] and station['prices'][fuel_type] < cheapest_prices[fuel_type]:
            cheapest_prices[fuel_type] = station['prices'][fuel_type]
            cheapest_stations[fuel_type] = station

# Calculate the average price for each fuel type locally and nationally
local_prices = {'E10': [], 'E5': [], 'B7': []}
national_prices = {'E10': [], 'E5': [], 'B7': []}

# Collect local prices
for station in matching_stations:
    for fuel_type in ['E10', 'E5', 'B7']:
        if fuel_type in station['prices']:
            local_prices[fuel_type].append(station['prices'][fuel_type])

# Collect national prices
for station in sbdataprocessing['stations']:
    for fuel_type in ['E10', 'E5', 'B7']:
        if fuel_type in station['prices']:
            national_prices[fuel_type].append(station['prices'][fuel_type])

# Calculate averages
local_avg_prices = {fuel_type: (sum(p for p in prices if p is not None) / len([p for p in prices if p is not None])) if prices else None for fuel_type, prices in local_prices.items()}
national_avg_prices = {fuel_type: (sum(p for p in prices if p is not None) / len([p for p in prices if p is not None])) if prices else None for fuel_type, prices in national_prices.items()}


# Print the cheapest stations in a pretty manner along with average prices and comparison
print("\nCheapest Stations and Average Prices:")
for fuel_type, station in cheapest_stations.items():
    if station:
        if fuel_type == 'E10':
            dfuel_type = 'Unleaded Petrol (E10)'
        elif fuel_type == 'E5':
            dfuel_type = 'Petrol (E5)'
        elif fuel_type == 'B7':
            dfuel_type = 'Diesel (B7)'
        print(f"{dfuel_type}:")
        print(f"  Brand: {station['brand']}")
        print(f"  Address: {station['address']}")
        print(f"  Postcode: {station['postcode']}")
        print(f"  Price: {station['prices'][fuel_type]}")
        
        # Generate Google Maps link
        latitude = station['location']['latitude']
        longitude = station['location']['longitude']
        google_maps_link = f"https://www.google.com/maps/dir/?api=1&destination={latitude},{longitude}"
        print(f"  Google Maps Link: {google_maps_link}")
        
        # Print average prices and comparison with the cheapest station
        cheapest_price = station['prices'][fuel_type]
        national_avg = national_avg_prices[fuel_type]
        diff_percentage = ((cheapest_price - national_avg) / national_avg) * 100
        cheaper_or_more_expensive = "cheaper" if diff_percentage < 0 else "more expensive"
        print(f"  National Average: {national_avg:.2f}")
        print(f"  The cheapest station price is {abs(diff_percentage):.2f}% {cheaper_or_more_expensive} than the national average.")
    else:
        print(f"{fuel_type}: No stations found")