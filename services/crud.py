from sqlmodel import Session, select
from entities import schemas, models

# User Operations
def get_user(db: Session, user_id: int):
    statement = select(models.User).where(models.User.id == user_id)
    return db.exec(statement).first()

def get_user_by_email(db: Session, email: str):
    statement = select(models.User).where(models.User.email == email)
    return db.exec(statement).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, hashed_password=user.password)  # Adjust for hashed_password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: models.User, user_update: schemas.UserUpdate):
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()

# Event Operations
def get_event(db: Session, event_id: int):
    statement = select(models.Event).where(models.Event.id == event_id)
    return db.exec(statement).first()

def get_events(db: Session, skip: int = 0, limit: int = 100):
    statement = select(models.Event).offset(skip).limit(limit)
    return db.exec(statement).all()

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def update_event(db: Session, db_event: models.Event, event_update: schemas.EventUpdate):
    for key, value in event_update.dict(exclude_unset=True).items():
        setattr(db_event, key, value)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = get_event(db, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()

# Event Participants
def add_user_to_event(db: Session, user_id: int, event_id: int):
    # Check if the association already exists to avoid duplicates
    statement = (
        select(models.EventParticipants)
        .where(models.EventParticipants.user_id == user_id, models.EventParticipants.event_id == event_id)
    )
    existing_association = db.exec(statement).first()
    if existing_association:
        return existing_association

    association = models.EventParticipants(user_id=user_id, event_id=event_id)
    db.add(association)
    db.commit()
    db.refresh(association)
    return association

def remove_user_from_event(db: Session, user_id: int, event_id: int):
    statement = (
        select(models.EventParticipants)
        .where(models.EventParticipants.user_id == user_id, models.EventParticipants.event_id == event_id)
    )
    association = db.exec(statement).first()
    if association:
        db.delete(association)
        db.commit()

def get_users_in_event(db: Session, event_id: int):
    statement = (
        select(models.User)
        .join(models.EventParticipants, models.User.id == models.EventParticipants.user_id)
        .where(models.EventParticipants.event_id == event_id)
    )
    return db.exec(statement).all()

def get_events_for_user(db: Session, user_id: int):
    statement = (
        select(models.Event)
        .join(models.EventParticipants, models.Event.id == models.EventParticipants.event_id)
        .where(models.EventParticipants.user_id == user_id)
    )
    return db.exec(statement).all()
