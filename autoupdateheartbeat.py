import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(subject, body, to_email):
    from_email = "lawri@hackclub.app"
    from_password = ""  # Use app-specific password if needed (e.g., for Gmail)

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))


    if isinstance(to_emails, list):
        to_emails = ", ".join(to_emails)
    message["To"] = to_emails

    # Connect to SMTP server 
    try:
        with smtplib.SMTP("hackclub.app", 587) as server:
            server.starttls()  # Secure connection
            server.login(from_email, from_password)
            text = message.as_string()
            server.sendmail(from_email, to_emails.split(", "), text)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to make GET request and report status
def check_url_status(url, to_email):
    try:
        # Send GET request to the URL
        response = requests.get(url)

        # Check response status code
        if response.status_code == 200:
            subject = f"URL Status for {url}"
            body = f"The URL {url} is up and returned status code 200."
        else:
            subject = f"URL Status for {url}"
            body = f"The URL {url} returned an error with status code {response.status_code}."

    except requests.exceptions.RequestException as e:
        subject = f"URL Status for {url}"
        body = f"Failed to reach {url}. Error: {e}"

    # Send email with the status
    send_email(subject, body, to_email)

# Set your URL to check and the recipient email address
url_to_check = "https://lawri.hackclub.app"
recipient_email = ["darbyshire.lawri@gmail.com", "lawri@lawridarbyshire.co.uk", "lawri@lawridarbyshire.co.uk"]

# Call the function
check_url_status(url_to_check, recipient_email)
