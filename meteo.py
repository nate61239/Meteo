import pymongo

client = pymongo.MongoClient("mongodb+srv://Meteorologist0:Meteo0@meteo0-gpxyt.gcp.mongodb.net/test?retryWrites=true&w=majority")
meteoDB = client.test

meteoDB = client["weather_data"]
meteoCollection = meteoDB["temperatureAndPrecip"]

newEntry = {"locationID":"1",
    "time":"2020-04-27T20:34Z",
    "temperature":[
        {"temp":62,"unit":"F"}
        ],
    "feels_like":[
        {"temp":62,"unit":"F"}
        ],
    "heat_index":[
        {"temp":60,"unit":"F"}
        ],
    "dew_point":[
        {"temp":41,"unit":"F"}
        ],
    "humidity":40,
    "precipitation":2,
    "barometer":1010,
    "wind":[
        {"spd":6.2, "unit":"mph", "dir":"West"}
        ],
    "uv_index":0,
    "visibility":[
        {"dist":24.9, "unit":"miles"}
        ]}
x = meteoCollection.insert_one(newEntry)
print(x);