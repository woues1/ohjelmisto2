import json
import requests


api_key = "b61266f84792f67987bae5d321c61917"
limit = 5
c = "metric"
municipality = input("Anna paikkakunta")
res1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={municipality}&limit={limit}&appid={api_key}").json()
lat = res1[0]["lat"]
lon = res1[0]["lon"]
res2 = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={c}&appid={api_key}").json()

print(json.dumps(res2, indent=2))

