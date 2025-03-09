from flask import Flask, render_template, request, session, jsonify
import datahandaling 
import getdata
import json
import os




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
    price = datahandaling.get_cheapest_fuel(postcode)
    return jsonify(price)
#Returns All Local Fuel Prices
@app.route('/api/cheapestlocal/postcode/<postcode>', methods=['GET'])
def cheapest_local(postcode):
    price = datahandaling.cheapest_local_fuel(postcode)
    return jsonify(price)
# Returns All Fuel Prices
@app.route('/api/alldata', methods=['GET'])
def all_fuel_stations():
    price = datahandaling.get_all_fuel_stations()
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

# --Hanndel Feed back
feedback = 0
@app.route("/api/feedback", methods=["POST"])
def submit_feedback(message):
    if not message:
        return jsonify({"status": "error", "message": "Message cannot be empty"}), 400
    
    feedback_data = {
        "message": message
    }
    

    feedback = feedback+1
    if not os.path.exists("feedback{feedback}.json"):
        with open("feedback{feedback}.json", "w") as file:
            json.dump([], file, indent=4)
    
    with open("feedback{feedback}.json", "r+") as file:
        data = json.load(file)
        data.append(feedback_data)
        file.seek(0)
        json.dump(data, file, indent=4)
    
    return jsonify({"status": "success", "message": "Feedback submitted successfully"})

# Deploy App 
if __name__ == "__main__":
    debug_mode = False
    app.run(debug=debug_mode, port=44751)
