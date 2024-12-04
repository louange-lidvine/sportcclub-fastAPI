from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from core.database import get_db
from entities import schemas, models
from services import crud

router = APIRouter()

# Create Event
@router.post("/events/", response_model=schemas.EventRead)
async def create_event(
    event: schemas.EventCreate,
    db: Session = Depends(get_db),
):
    return crud.create_event(db=db, event=event)

# Get All Events
@router.get("/events/", response_model=List[schemas.EventRead])
async def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_events(db, skip=skip, limit=limit)

# Update Event
@router.put("/events/{event_id}/", response_model=schemas.EventRead)
async def update_event(
    event_id: int,
    event_update: schemas.EventUpdate,
    db: Session = Depends(get_db),
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return crud.update_event(db=db, db_event=event, event_update=event_update)

# Delete Event
@router.delete("/events/{event_id}/")
async def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    crud.delete_event(db=db, event_id=event_id)
    return {"message": "Event deleted successfully"}

# Add User to Event
@router.post("/events/{event_id}/add_user/{user_id}")
async def add_user_to_event(
    event_id: int,
    user_id: int,
    db: Session = Depends(get_db),
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.add_user_to_event(db=db, event_id=event_id, user_id=user_id)

# Get Event Participants
@router.get("/events/{event_id}/participants/", response_model=List[schemas.UserRead])
async def get_event_participants(
    event_id: int,
    db: Session = Depends(get_db),
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return crud.get_event_participants(db=db, event_id=event_id)

# Get Events for a User
@router.get("/users/{user_id}/events/", response_model=List[schemas.EventRead])
async def get_user_events(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.get_user_events(db=db, user_id=user_id)
