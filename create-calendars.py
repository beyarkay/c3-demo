from datetime import datetime, timedelta
import yaml
import os
import requests
from bs4 import BeautifulSoup

def main():
    # A static list of events to create
    events = [
        {
            "title": "An example event title",
            "description": "This event was created by [c3](https://github.com/beyarkay/c3)",
            "start": datetime.now(),
            "end": datetime.now() + timedelta(hours=3),
        },
    ]
    
    # Also collect weather data from a website, scrape it with BeautifulSoup,
    # and add that data as a calendar event
    weather_url = "https://www.timeanddate.com/weather/south-africa/stellenbosch"
    res = requests.get(weather_url)
    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')
        selector = '.table > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)'
        txt = soup.select_one(selector)
        print(txt)
        events.append({
            "title": f"{txt.text} in Stellenbosch",
            "description": f"Data from {weather_url}\nThis event was created by [c3](https://github.com/beyarkay/c3)",
            "start": str(datetime.now())[:10],
            "end": str(datetime.now())[:10],
        })

    # Create a directory to contain our calendars
    print("Creating directory `calendars/`")
    os.makedirs("calendars", exist_ok=True)

    # Write the events list as yaml files into the calendars directory
    print(f"Writing events to `calendars/simple-calendar.yaml`:\n{events}")
    with open('calendars/simple-calendar.yaml', 'w') as file:
        yaml.dump({"events": events}, file)

    print(f"Python script finished")

if __name__ == "__main__":
    main()
