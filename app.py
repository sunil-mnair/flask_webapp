from flask import Flask,request,render_template
import requests

# Creating an Object of the Flask App
app = Flask(__name__)

# Define the API endpoint
url = 'https://eif.pythonanywhere.com/countries'

# Send a GET request to the API
response = requests.get(url)
countries_list = response.json()

@app.route("/")
def index():
    name = "Sunil Nair"
    return render_template("index.html",getname = name)

@app.route("/about")
def about():
    return "About The Website"

@app.route("/countries")
def countries():
    country = request.args.get("country")

    for c in countries_list:
        if c["name"] == country:
            return render_template("countries.html",c = c)
