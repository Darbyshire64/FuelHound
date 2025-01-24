import json
import getdata

def search_and_match_stations(postal, getdata):
    totalping = 0
    successping = 0
    match = 0

    # List of fuel providers and their methods
    fuel_providers = [
        ("Sainsbury's", getdata.GetData.Sainsburys),
        ("Shell", getdata.GetData.Shell),
        ("AppleGreen", getdata.GetData.AppleGreen),
        ("Ascona", getdata.GetData.Ascona),
        ("Asda", getdata.GetData.Asda),
        ("BP", getdata.GetData.BP),
        ("Esso Tesco", getdata.GetData.ET),
        ("Jet", getdata.GetData.Jet),
        ("Karen", getdata.GetData.Karen),
        ("Morrisons", getdata.GetData.Morisons),
        ("Moto", getdata.GetData.Moto),
        ("Motor", getdata.GetData.Motor),
        ("Rontec", getdata.GetData.RonTec),
        ("SGN", getdata.GetData.SGN),
    ]

    matching_stations = []

    for name, get_method in fuel_providers:
        data = get_method()
        totalping += 1
        if data is not None:
            processed_data = json.loads(data)
            for site in processed_data.get('stations', []):
                site_postal = site['postcode'].split(' ')[0]
                if site_postal == postal:
                    matching_stations.append(site)
                    match += 1
            successping += 1

    # Find the cheapest station for each fuel type
    cheapest_stations = {'E10': None, 'E5': None, 'B7': None}
    cheapest_prices = {'E10': float('inf'), 'E5': float('inf'), 'B7': float('inf')}

    for station in matching_stations:
        for fuel_type in ['E10', 'E5', 'B7']:
            if fuel_type in station['prices'] and station['prices'][fuel_type] < cheapest_prices[fuel_type]:
                cheapest_prices[fuel_type] = station['prices'][fuel_type]
                cheapest_stations[fuel_type] = station

    # Calculate average prices
    local_prices = {'E10': [], 'E5': [], 'B7': []}
    national_prices = {'E10': [], 'E5': [], 'B7': []}

    for station in matching_stations:
        for fuel_type in ['E10', 'E5', 'B7']:
            if fuel_type in station['prices']:
                local_prices[fuel_type].append(station['prices'][fuel_type])

    for station in processed_data.get('stations', []):
        for fuel_type in ['E10', 'E5', 'B7']:
            if fuel_type in station['prices']:
                national_prices[fuel_type].append(station['prices'][fuel_type])

    local_avg_prices = {fuel_type: (sum(prices) / len(prices)) if prices else None for fuel_type, prices in local_prices.items()}
    national_avg_prices = {fuel_type: (sum(prices) / len(prices)) if prices else None for fuel_type, prices in national_prices.items()}

    # Prepare the JSON response
    response = {
        "total_companies": totalping,
        "successful_requests": successping,
        "matching_stations_found": match,
        "cheapest_stations": {
            fuel_type: {
                "brand": station["brand"],
                "address": station["address"],
                "postcode": station["postcode"],
                "price": station["prices"][fuel_type],
                "google_maps_link": f"https://www.google.com/maps/dir/?api=1&destination={station['location']['latitude']},{station['location']['longitude']}",
            } if station else None
            for fuel_type, station in cheapest_stations.items()
        },
        "average_prices": {
            "local": local_avg_prices,
            "national": national_avg_prices,
        },
    }

    return json.dumps(response, indent=2)

# Example usage
postal_code = "RG14"  # Replace with the desired postal code
response = search_and_match_stations(postal_code, getdata)
print(response)
