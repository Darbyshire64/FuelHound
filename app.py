from flask import Flask, render_template, request, session, jsonify
import datahandaling 
import getdata
import json
import os

# Run Self Tests To ensure the Code can Opperate
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
        ("Tesco", getdata.GetData.Tesco),
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


#Define and Run Flask App
app = Flask(__name__)
app.secret_key = 'TeeheheNotGivingUThis'

# Apps Main Function
@app.route("/", methods=["GET", "POST"])
def home():

    # Check if the form is being submitted
    if request.method == "POST":
        postcode = request.form.get("postcode")
        agree = request.form.get("agree")  # Check if user agreed to terms
        if not agree:
            return render_template("index.html", error="You must agree to the Privacy Policy and Terms of Service.")
        
        #Call Cheapest Fuel
        prices = datahandaling.get_cheapest_fuel(postcode)
        
        # Store the postcode and prices in the session for the user
        session['postcode'] = postcode
        session['prices'] = prices
        
        return render_template("index.html", postcode=postcode, prices=prices)
    return render_template("index.html")


# -- API --
#Returns the Cheapest Fuel Prices
@app.route('/api/cheapest/postcode/<postcode>', methods=['GET'])
def cheapest_fuel(postcode):
    price = get_cheapest_fuel(postcode)
    return jsonify(price)
#Returns All Local Fuel Prices
@app.route('/api/cheapestlocal/postcode/<postcode>', methods=['GET'])
def cheapest_local(postcode):
    price = cheapest_local_fuel(postcode)
    return jsonify(price)
# Returns All Fuel Prices
@app.route('/api/alldata', methods=['GET'])
def all_fuel_stations():
    price = get_all_fuel_stations()
    return jsonify(price)

# -- Web Handeling---
@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')
@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms-of-service.html')
@app.route('/api/docs')
def api():
    return render_template('api.html')
@app.route('/api/docs/samplejson')
def samplejson():
    return render_template('sampleresponse.json')

# Deploy App 
if __name__ == "__main__":
    debug_mode = False
    app.run(debug=debug_mode, port=44751)
