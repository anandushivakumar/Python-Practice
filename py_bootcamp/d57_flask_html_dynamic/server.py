from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess/<name>')
def guess(name):
    gender_api = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_api)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    age_api = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_api)
    age_data = age_response.json()
    age = age_data['age']

    return render_template('guess.html', name = name, age = age, gender = gender)

if __name__ == '__main__':
    app.run(debug=True)
