from typing import List

from fastapi import HTTPException, Depends, APIRouter
from sqlmodel import Session

from core.database import get_db
from entities.models import Event, User, EventParticipants;
from entities.schemas import UserCreate, EventCreate, EventRead, UserRead

router = APIRouter(tags=["Users"], prefix="/users"  )


# Create User Endpoint
@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, hashed_password=user.password, is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Get All Users Endpoint
@router.get("/users", response_model=List[UserRead])
def get_all_users_from_the_database(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# Read User Endpoint
@router.get("/users/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Create Event Endpoint
@router.post("/events/", response_model=EventRead)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(name=event.name, description=event.description, date=event.date,
                     max_participants=event.max_participants)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


# Read Event Endpoint
@router.get("/events/{event_id}", response_model=EventRead)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


# Add User to Event (Linking)
@router.post("/events/{event_id}/add_user/{user_id}")
def add_user_to_event(event_id: int, user_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_event is None or db_user is None:
        raise HTTPException(status_code=404, detail="Event or User not found")

    # Link User to Event via EventParticipants
    db_participant = EventParticipants(user_id=user_id, event_id=event_id)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)

    return {"message": "User added to event successfully"}


# Get Users for Event
@router.get("/events/{event_id}/participants", response_model=List[UserRead])
def get_event_participants(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    participants = db.query(User).join(EventParticipants).filter(EventParticipants.event_id == event_id).all()
    return participants
