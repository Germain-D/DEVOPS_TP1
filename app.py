from flask import request, jsonify, Flask
import os, requests
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/', methods=['GET'])
def home():
    uri = f"https://api.openweathermap.org/data/2.5/weather?lat={app.config['LAT']}&lon={app.config['LONG']}&appid={app.config['APIKEY']}&units=m"
    res = requests.get(uri)
    if res.status_code == 200:

        data = res.json()
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        city = data['name']
        daylight = sunset-sunrise
        meteo = data['weather'][0]['main']
        descri = data['weather'][0]['description']
        temp = data['main']['temp']
        feels = data['main']['feels_like']
        wind = data['wind']['speed']
        country = data['sys']['country']

        html = """
            <h1>API TP DEVOPS - Germain Deffontaines </h1>
            <p><b> Latitude </b> : """+ str(latitude) +""" °</p>
            <p><b> Longitude </b> : """+ str(longitude) +""" °</p>
            <p><b> Pays </b> : """+ str(country) +"""</p>
            <p><b> Ville </b> : """+ str(city) +"""</p>
            <p><b> Température </b> :"""+ str(temp) +""" °C</p>
            <p><b> Température ressentie </b> : """+ str(feels) +""" °C</p>
            <p><b> Temps </b> : """+ str(meteo) +"""</p>
            <p><b> Description du temps </b> : """+ str(descri) +"""</p>
            <p><b> Force du vent </b> : """+ str(wind) +"""</p>
            <p><b> Heure du lever du soleil </b> : """+ str(sunrise) +"""</p>
            <p><b> Heure du coucher du soleil </b> : """+ str(sunset) +"""</p>
            <p><b> Durée de soleil </b> : """+ str(daylight) +"""</p>"""
            
    return html




if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=8081)
    # host='0.0.0.0' -> accept connection from every host (to connect through a Docker virtual network)

    
