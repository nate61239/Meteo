import pymongo

client = pymongo.MongoClient("mongodb+srv://Meteorologist0:Meteo0@meteo0-gpxyt.gcp.mongodb.net/test?retryWrites=true&w=majority")
meteoDB = client.test

meteoDB = client["weather_data"]
meteoCollection = meteoDB["temperatureAndPrecip"]

newEntry = {"location":"Kasson",
            "date":"4/27/2020",
            "time":"20:00",
            "temperature":66,
            "precipitation":2,
            "wind": 8.1,
            "wind_dir": "W",
            "visibility" : 24.9}
x = meteoCollection.insert_one(newEntry)
print(x.inserted_ids);