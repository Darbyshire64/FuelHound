from flask import Flask, render_template, request, session, redirect, url_for
import requests  # For fetching external data

app = Flask(__name__)
app.secret_key = 'TeeheheNotGivingUThis'  # Ensure this is a secure, random key for session encryption

#2
# Function to fetch the cheapest fuel (using a dummy API for now)
def get_cheapest_fuel(postcode):
    # Use a real API or data source here. For now, we'll return hardcoded values.
    response = {
        'petrol': 1.25,
        'diesel': 1.30,
        'lpg': 0.99
    }
    return response

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

    # If the page is accessed with a GET request (i.e., on refresh), no prices or postcode should be shown
    return render_template("index.html", postcode=None, prices=None)

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms-of-service.html')

if __name__ == "__main__":
    app.run(debug=True)
