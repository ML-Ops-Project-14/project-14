import csv
import requests
import time

URL = "https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&current_weather=true" 

with open("dataset.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["temperature", "wind_speed"])

    count = 0

    try:
        while count < 60:
            data = requests.get(URL).json()["current_weather"]
            temp = data["temperature"]
            wind = data["windspeed"]

            writer.writerow([temp, wind])
            count += 1

            print(f"Temp={temp:.2f}°C | Wind={wind:.1f} km/h")
            time.sleep(2)

    except KeyboardInterrupt:
        pass
