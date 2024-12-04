import requests
import pandas as pd

# API URLs
USER_API = 'http://127.0.0.1:8000/users/{user_id}'
EVENT_API = 'http://127.0.0.1:8000/events/'

try:
    # Fetch user data
    user_response = requests.get(USER_API)
    user_response.raise_for_status()
    user_data = user_response.json()

    # Fetch all events
    event_response = requests.get(EVENT_API)
    event_response.raise_for_status()
    event_data = event_response.json()

    # Filter events belonging to the user
    user_events = [event for event in event_data if event['user_id'] == user_data['id']]

    # Combine user and events data
    mapped_data = {
        "user": user_data,
        "events": user_events
    }

    # Print as JSON
    print(mapped_data)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
