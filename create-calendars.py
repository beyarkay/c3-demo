from datetime import datetime, timedelta
import yaml
import os


def main():
    # A list of events to create
    events = [
        {
            "title": "An example event title",
            "description": "This event was created by [c3](https://github.com/beyarkay/c3)",
            "start": datetime.now(),
            "end": datetime.now() + timedelta(hours=3),

        },
    ]
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
