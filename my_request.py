import pandas as pd
import requests

try:
    # Fetch users data
    users_api = requests.get('http://127.0.0.1:8000/users/users')
    users_api.raise_for_status()
    users_api_data = users_api.json()

    # Fetch events data
    events_api = requests.get('http://127.0.0.1:8000/events/events')
    events_api.raise_for_status()
    events_api_data = events_api.json()

    # Create DataFrames
    users_df = pd.DataFrame(users_api_data if isinstance(users_api_data, list) else users_api_data.get('users', []))
    events_df = pd.DataFrame(events_api_data if isinstance(events_api_data, list) else events_api_data.get('events', []))

    # Flatten the participants field in events_df
    event_participants = []
    for event in events_api_data:
        event_id = event['id']  # Get the event ID
        for participant in event.get('participants', []):  # Loop through the participants
            user_id = participant.get('id')  # Extract user ID from the participant
            if user_id:  # Ensure user_id is valid (not None)
                event_participants.append({'event_id': event_id, 'user_id': user_id})

    # Create Participants DataFrame
    participants_df = pd.DataFrame(event_participants)
    print("Participants DataFrame:\n", participants_df)

    # Check if the Participants DataFrame is empty
    if participants_df.empty:
        raise ValueError("Participants DataFrame is empty. Check the 'participants' field in the events API response.")

    # Perform Joins
    # Inner Join
    inner_join_df = pd.merge(participants_df, users_df, left_on='user_id', right_on='id', how='inner')
    inner_join_df = pd.merge(inner_join_df, events_df, left_on='event_id', right_on='id', how='inner', suffixes=('_user', '_event'))
    print("\nInner Join Result:\n", inner_join_df)

    # Left Join
    left_join_df = pd.merge(participants_df, users_df, left_on='user_id', right_on='id', how='left')
    left_join_df = pd.merge(left_join_df, events_df, left_on='event_id', right_on='id', how='left', suffixes=('_user', '_event'))
    print("\nLeft Join Result:\n", left_join_df)

    # Right Join
    right_join_df = pd.merge(participants_df, users_df, left_on='user_id', right_on='id', how='right')
    right_join_df = pd.merge(right_join_df, events_df, left_on='event_id', right_on='id', how='right', suffixes=('_user', '_event'))
    print("\nRight Join Result:\n", right_join_df)

    inner_join_df['email_lenghth']=inner_join_df['email'].apply(lambda x: len(x))
    print(inner_join_df['email_lenghth'])

    # 2. Determine active status
    inner_join_df['is_active'] = inner_join_df['event_id'].apply(lambda x: 1 if pd.notnull(x) else 0)

    # Print the final DataFrame
    print(inner_join_df[['email', 'event_id', 'is_active']])  # Show specific columns
    print(inner_join_df.head())

    # 3. Handle missing values using ffill and bfill
    inner_join_df.ffill(inplace=True)
    inner_join_df.bfill(inplace=True)

    # Print the final DataFrame
    print(  inner_join_df.head())




except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
    print("Ensure the API server is running and accessible.")

except ValueError as val_err:
    print(f"ValueError: {val_err}")

except KeyError as key_err:
    print(f"KeyError: {key_err}")

except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
