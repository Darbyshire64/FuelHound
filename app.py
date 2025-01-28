from flask import Flask, render_template, request, session, redirect, url_for
import requests  # For fetching external data
import getdata # For fetching external data
import json 

#Updated:
# Index.html
#

app = Flask(__name__)
app.secret_key = 'TeeheheNotGivingUThis'  # Ensure this is a secure, random key for session encryption



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
        for fuel_type in ['E10', 'E5', 'B7']:
            if fuel_type in station['prices']:
                local_prices[fuel_type].append(station['prices'][fuel_type] / 100)

    for station in processed_data.get('stations', []):
        for fuel_type in ['E10', 'E5', 'B7']:
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
#1

@app.route("/", methods=["GET", "POST"])
def home():
    # Always clear session data on GET request (i.e., on refresh)
    session.clear()  # Clears all session data
    
    # Check if the form is being submitted
    if request.method == "POST":
        postcode = request.form.get("postcode")
        agree = request.form.get("agree")  # Check if user agreed to terms
        if not agree:
            return render_template("index.html", error="You must agree to the Privacy Policy and Terms of Service.")
        
        prices = get_cheapest_fuel(postcode)
        
        # Store the postcode and prices in the session for the user
        session['postcode'] = postcode
        session['prices'] = prices
        
        return render_template("index.html", postcode=postcode, prices=prices)
    return render_template("index.html")


@app.route('/api/v1/fueldata/postcode/<string:postcode>', methods=['GET','POST'])
def FuelApi(postcode):
    if request.method == "POST":
        dataOut = get_cheapest_fuel(postcode)
        return dataOut


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms-of-service.html')

if __name__ == "__main__":
    app.run(debug=True)
