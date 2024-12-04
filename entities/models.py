from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional
from datetime import datetime

# Association Table
class EventParticipants(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    event_id: int = Field(foreign_key="event.id", primary_key=True)

# User Model
class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)

    events: List["Event"] = Relationship(back_populates="participants", link_model=EventParticipants)
    # bookings: List["Booking"] = Relationship(back_populates="user")

# Event Model
class Event(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    date: datetime
    max_participants: int

    participants: List[User] = Relationship(back_populates="events", link_model=EventParticipants)
#
# # Facility Model
# class Facility(SQLModel, table=True):
#     id: int = Field(primary_key=True, index=True)
#     name: str = Field(index=True)
#     description: Optional[str] = None
#     capacity: int
#
#     bookings: List["Booking"] = Relationship(back_populates="facility")
#
# # Booking Model
# class Booking(SQLModel, table=True):
#     id: int = Field(primary_key=True, index=True)
#     user_id: int = Field(foreign_key="user.id")
#     facility_id: int = Field(foreign_key="facilities.id")
#     start_time: datetime
#     end_time: datetime
#
#     user: "User" = Relationship(back_populates="bookings")
#     facility: "Facility" = Relationship(back_populates="bookings")
