import requests

city = input("enter city name=")

api_key = "b43c21f106819d54c6dc3133c1c3f0e0"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]
    wind = data["wind"]["speed"]


    print("\nWheather Report")
    print("City:", city)
    print("Temperature:", temperature, "°c")
    print("Humidity:", humidity,"%")
    print("Condition:", condition)
    print("Wind:", wind,"m/s")
else:
    print("city not found!")