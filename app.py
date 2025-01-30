from flask import Flask, render_template, request, session, jsonify
import getdata 
import json 
import os

#Updated With New announcment Data

# Run Self Tests
print("Checking Dependecies")
if getdata:
    print("Getdata module is installed")
else:
    print("Getdata module are not installed")
    exit("Please install the Getdata module")

if json:
    print("Json module is installed")
else:
    print("Json module are not installed")
    exit("Please install the Json module")

if Flask:
    print("Flask module is installed")
else:
    print("Flask module are not installed")
    exit("Please install the Flask module")
if render_template:
    print("Render_template module is installed")
else:
    print("Render_template module are not installed")
    exit("Please install the Render_template module")
if jsonify:
    print("Jsonify module is installed")
else:
    print("Jsonify modules are not installed")
    exit("Please install the Jsonify module")
print("All Dependecies are installed")
print("Running Internet Acccess Test")

internet = getdata.HeartBeat.InternetCheck()
if internet == True:
    print("Internet Access Test Passed")
else:
    print("Internet Access Test Failed")
    print("Please check your internet connection")
    exit("No internet connection")
print("Running API Test")
try:
    postcode = 'RG14'
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
        try:
            data = get_method()
        except:
            error = Exception
        if data is not None:
            print(name, "API Test Passed")
        else:
            print(name, "API Test Failed")
            print(error)
except:
    print("API Test Failed")
    print("Contuining with limited functionality/No functionality")
    print("Bugs may occur")
    print("SOFTWARE IS UNSTABLE DO NOT USE")

app = Flask(__name__)
app.secret_key = 'TeeheheNotGivingUThis'



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


#Api
@app.route('/api/cheapest/postcode/<postcode>', methods=['GET'])
def cheapest_fuel(postcode):
    price = get_cheapest_fuel(postcode)
    return jsonify(price)


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')
@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms-of-service.html')
@app.route('/api/doc')
def api():
    return render_template('api.html')
@app.route('/api/samplejson')
def samplejson():
    return render_template('sampleresponse.json')

if __name__ == "__main__":
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode, port=44751)
