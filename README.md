
# Devops TP1 Docker :

L'objectif de ce tp est de créer un wrapper qui va retourner la météo d'un lieucà partir de sa latitude et sa longitude. Pour cela nous allons utiliser l'API d'OpenWeather.
J'ai choisi d'utiliser Python3 pour le développement de ce TP car il s'agit du langage avec lequel j'ai le plus d'affinité.

Ensuite nous allons créer une image Docker qui va contenir notre wrapper puis la mettre à disposition sur Docker Hub afin de pouvoir l'utiliser par le biais de Docker Hub.


----

## Commandes :

Tout d'abord nous allons créer un environement de travail :
> pipenv shell

on défini la variable d'environnement pour la clé :
> export APIKEY=68e3a32a2b52669bdab1c00876332096

On test l'API depuis la console :
> curl "http://api.openweathermap.org/data/2.5/weather?q=brescia&appid=$APIKEY"
```shell
(Devops_TP1) germain@germain-KLVL-WXX9:~/Documents/Devops_TP1$ 

curl "http://api.openweathermap.org/data/2.5/weather?q=brescia&appid=$APIKEY"

{"coord":{"lon":10.3,"lat":45.6333},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":298.56,"feels_like":298.25,"temp_min":296.9,"temp_max":299.87,"pressure":1017,"humidity":42,"sea_level":1017,"grnd_level":902},"visibility":10000,"wind":{"speed":1.9,"deg":226,"gust":2.42},"clouds":{"all":94},"dt":1654353301,"sys":{"type":2,"id":197942,"country":"IT","sunrise":1654313504,"sunset":1654369366},"timezone":7200,"id":3181553,"name":"Provincia di Brescia","cod":200}
```

On créer fichier api.py : 
> touch api.py

Dans le code du fichier api.py on accède à l'api avec  ```python load_dotenv() ``` de la libraire dotenv, puis avec ```python os.environ['APIKEY'] ```. On récupère de la même manière les variavles LAT et LONG.

On construit la requête :
```python response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + LAT + "&lon=" + LONG + "&appid=" + APIKEY + "&units=metric") ```

Puis on récupère la réponse (statur et contenu): 
-  ```python response.status_code ```
- ```python response.json() ```


----

## Conteneurisation : 

app.run(host='0.0.0.0')  

File Dockerfile :

    FROM python:3.8-buster

    WORKDIR /devops_tp1

    COPY requirements.txt .

    RUN pip install -r requirements.txt

    COPY api.py .

    EXPOSE 5000

    CMD ["python", "api.py"]

on contruit l'image :

> docker build --tag api .

On run le conteneur :

> docker run -p 5000:5000 --env APIKEY=$APIKEY --rm api

> docker run --env LAT="5.902785" --env LONG="102.754175" --env APIKEY=240aa650f4db4e154a07d0459c30a347 --rm api


----
## Docker Hub :

Envoi de l'image sur DockerHub :

> docker images

> docker login --username=germaindftn

tag IMAGE ID de api : ```ed1cae9181ef```

> docker tag ed1cae9181ef germaindftn/devops_tp1

> docker images   

> docker push germaindftn/devops_tp1 

> docker run --env LAT="5.902785" --env LONG="102.754175" --env APIKEY=240aa650f4db4e154a07d0459c30a347 germaindftn/devops_tp1 

````shell
 (Devops_TP1) germain@germain-KLVL-WXX9:~/Documents/Devops_TP1$ 
 
 docker run --env LAT="5.902785" --env LONG="102.754175" --env APIKEY=240aa650f4db4e154a07d0459c30a347 germaindftn/devops_tp1
200
{'coord': {'lon': 102.7542, 'lat': 5.9028}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 27.57, 'feels_like': 29.75, 'temp_min': 27.57, 'temp_max': 27.57, 'pressure': 1010, 'humidity': 69, 'sea_level': 1010, 'grnd_level': 983}, 'visibility': 10000, 'wind': {'speed': 2.33, 'deg': 89, 'gust': 2.31}, 'clouds': {'all': 100}, 'dt': 1654352109, 'sys': {'country': 'MY', 'sunrise': 1654296841, 'sunset': 1654341646}, 'timezone': 28800, 'id': 1736405, 'name': 'Jertih', 'cod': 200}
````

----

Lien du repo GitHub : https://github.com/Germain-D/DEVOPS_TP1

Lien du repo DockerHub : https://hub.docker.com/r/germaindftn/devops_tp1

# TP2

Lien du repo DockerHub : https://hub.docker.com/r/germaindftn/devops-tp2

Comment j'ai fait :
