import getdata
import json

def extract_outward_code(postcode):
    """
    Extracts the outward code (first segment) from a full postcode.

    Args:
        postcode (str): The full UK postcode, e.g., 'RG14 5PA'.

    Returns:
        str: The outward code, e.g., 'RG14', or None if the input is invalid.
    """
    if not postcode:
        return None

    # Split by space and return the first segment
    parts = postcode.strip().upper().split(" ")
    return parts[0] if parts else None

def get_cheapest_fuel(postcode):
    totalping = 0
    successping = 0
    match = 0
    postcode = extract_outward_code(postcode)
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
                if site_postal == postcode:
                    matching_stations.append(site)
                    match += 1
            successping += 1

    # Find the cheapest station for each fuel type
    cheapest_stations = {'E10': None, 'E5': None, 'B7': None}
    cheapest_prices = {'E10': float('inf'), 'E5': float('inf'), 'B7': float('inf')}

    for station in matching_stations:
        for fuel_type in ['E10', 'E5', 'B7']:
            if fuel_type in station['prices']:
                # Convert prices from pennies to pounds
                price_in_pounds = station['prices'][fuel_type] / 100
                if price_in_pounds < cheapest_prices[fuel_type]:
                    cheapest_prices[fuel_type] = price_in_pounds
                    cheapest_stations[fuel_type] = station

    # Calculate average prices
    local_prices = {'E10': [], 'E5': [], 'B7': []}
    national_prices = {'E10': [], 'E5': [], 'B7': []}

    for station in matching_stations:
        for fuel_type in ['E10', 'E5', 'B7', 'SDV']:
            if fuel_type in station['prices']:
                local_prices[fuel_type].append(station['prices'][fuel_type] / 100)

    for station in processed_data.get('stations', []):
        for fuel_type in ['E10', 'E5', 'B7', 'SDV']:
            if fuel_type in station['prices']:
                national_prices[fuel_type].append(station['prices'][fuel_type] / 100)

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
                "price": cheapest_prices[fuel_type],  # Price already in pounds
                "google_maps_link": f"https://www.google.com/maps/dir/?api=1&destination={station['location']['latitude']},{station['location']['longitude']}",
            } if station else None
            for fuel_type, station in cheapest_stations.items()
        },
        "average_prices": {
            "local": local_avg_prices,
            "national": national_avg_prices,
        },
    }
    return response

def cheapest_local_fuel(postcode):
    totalping = 0
    successping = 0
    match = 0
    postcode = extract_outward_code(postcode)
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
                if site_postal == postcode:
                    matching_stations.append(site)
                    match += 1
            successping += 1

     # Find the cheapest station for each fuel type
    cheapest_prices = {'E10': float('inf'), 'E5': float('inf'), 'B7': float('inf'), 'SDV': float('inf')}

    for station in matching_stations:
        for fuel_type in ['E10', 'E5', 'B7', 'SDV']:
            if fuel_type in station['prices']:
                # Convert prices from pennies to pounds
                price_in_pounds = station['prices'][fuel_type] / 100
                if price_in_pounds < cheapest_prices[fuel_type]:
                    cheapest_prices[fuel_type] = price_in_pounds

     # Prepare the JSON response
    response = {
        "total_companies": totalping,
        "successful_requests": successping,
        "matching_stations_found": match,
        "stations": [
            {
                "brand": station["brand"],
                "address": station["address"],
                "postcode": station["postcode"],
                "prices": {
                    fuel_type: {
                        "price": station["prices"][fuel_type] / 100,  # Price in pounds
                        "cheapest": (station["prices"][fuel_type] / 100 == cheapest_prices[fuel_type])
                    }
                    for fuel_type in station["prices"]
                },
                "google_maps_link": f"https://www.google.com/maps/dir/?api=1&destination={station['location']['latitude']},{station['location']['longitude']}",
            }
            for station in matching_stations
        ],
    }
    return response

def get_all_fuel_stations():
    totalping = 0
    successping = 0

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

    all_stations = []

    for name, get_method in fuel_providers:
        data = get_method()
        totalping += 1
        if data is not None:
            processed_data = json.loads(data)
            for site in processed_data.get('stations', []):
                all_stations.append(site)
            successping += 1

     # Prepare the JSON response
    response = {
        "total_companies": totalping,
        "successful_requests": successping,
        "all_stations": all_stations,
    }
    return response