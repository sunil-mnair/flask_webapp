from flask import Flask,request,render_template,jsonify
import requests,json

# Creating an Object of the Flask App
app = Flask(__name__)

# Define the API endpoint
url = 'https://eif.pythonanywhere.com/countries'

# Send a GET request to the API
response = requests.get(url)
countries_list = response.json()

with open("static/data/student.json") as f:
    student_list = json.load(f)



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

@app.route("/dictionary")
def dictionary():
    word = request.args.get("word")

    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

    response = requests.get(url)
    dictionary_list = response.json()

    return render_template("dictionary.html",dl = dictionary_list[0])

@app.route("/students")
def students():
    return jsonify(student_list)