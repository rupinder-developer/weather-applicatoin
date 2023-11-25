from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your weatherapi.com API key
API_KEY = '402b853bd9704abcade34152232511'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    units = request.form['units']

    params = {
        'key': API_KEY,
        'q': city,
        'aqi': 'yes',  # Include air quality index
        'unit': units
    }

    response = requests.get(BASE_URL, params=params)
    weather_data = response.json()

    if 'error' in weather_data:
        return render_template('error.html', error_message=weather_data['error']['message'])
    
    temperature = weather_data['current']['temp_c'] if units == 'C' else weather_data['current']['temp_f']
    description = weather_data['current']['condition']['text']

    return render_template('weather.html', city=city, temperature=temperature, description=description, units=units)

if __name__ == '__main__':
    app.run(debug=True)
