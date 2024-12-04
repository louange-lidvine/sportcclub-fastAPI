# from core.database import SessionLocal  # Adjusted import
# from entities.models import User, Event, Facility, Booking  # Adjusted import
# from datetime import datetime, timedelta
# import random
# from hashlib import sha256
# from sqlalchemy.orm import Session
#
# # Sample data generators
# def generate_random_email(index):
#     return f"user{index}@sportsclub.com"
#
# def generate_random_password():
#     return sha256(f"password{random.randint(1000, 9999)}".encode()).hexdigest()
#
# def generate_random_event_type():
#     return random.choice(['Sports', 'Seminar', 'Concert', 'Workshop'])
#
# def generate_random_gender():
#     return random.choice(['Male', 'Female', 'Other'])
#
# def generate_random_event_date():
#     return datetime.now() + timedelta(days=random.randint(0, 30))
#
# # Create test data for Users, Events, Facilities, and Bookings
# def create_test_data():
#     db = SessionLocal()
#     try:
#         # Clean up any existing data
#         db.query(User).delete()
#         db.query(Event).delete()
#         db.query(Facility).delete()
#         db.query(Booking).delete()
#         db.commit()
#
#         # Generate sample Users
#         users = [
#             User(
#                 email=generate_random_email(i),
#                 hashed_password=generate_random_password(),
#                 is_active=random.choice([True, False]),
#                 gender=generate_random_gender()
#             ) for i in range(1, 21)
#         ]
#         db.add_all(users)
#         db.commit()
#
#         # Generate sample Events
#         events = [
#             Event(
#                 name=f"Event {i}",
#                 description=f"Description for event {i}",
#                 date=generate_random_event_date(),
#                 max_participants=random.randint(5, 100),
#                 event_type=generate_random_event_type()
#             ) for i in range(1, 6)
#         ]
#         db.add_all(events)
#         db.commit()
#
#         # Generate sample Facilities
#         facilities = [
#             Facility(
#                 name=f"Facility {i}",
#                 description=f"Description for facility {i}",
#                 capacity=random.randint(50, 200)
#             ) for i in range(1, 4)
#         ]
#         db.add_all(facilities)
#         db.commit()
#
#         # Generate sample Bookings
#         bookings = [
#             Booking(
#                 user_id=random.choice(users).id,
#                 facility_id=random.choice(facilities).id,
#                 start_time=datetime.now() + timedelta(days=random.randint(0, 30), hours=random.randint(1, 12)),
#                 end_time=datetime.now() + timedelta(days=random.randint(0, 30), hours=random.randint(2, 13))
#             ) for _ in range(1, 15)
#         ]
#         db.add_all(bookings)
#         db.commit()
#
#         # Assign participants to events
#         for event in events:
#             event.participants = random.sample(users, random.randint(1, event.max_participants))
#         db.commit()
#
#         print("Test data created successfully!")
#
#     except Exception as e:
#         print(f"Error creating test data: {e}")
#         db.rollback()
#     finally:
#         db.close()
#
# if __name__ == "__main__":
#     create_test_data()
