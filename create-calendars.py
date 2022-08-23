from datetime import datetime, timedelta
import yaml
import os


def main():
    # A list of events to create
    events = [
        {
            "summary": "An event with a start and finish",
            "description": "This event has a start and finish time.",
            "start": datetime.now(),
            "finsh": datetime.now() + timedelta(hours=3),
        },
    ]
    # Create a directory to contain our calendars
    os.makedirs("calendars", exist_ok=True)
    # Write the events list as yaml files into the calendars directory
    with open('calendars/simple-calendar.yaml', 'w') as file:
        yaml.dump(events, file)

if __name__ == "__main__":
    main()
