from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import List, Optional

# User Schemas
class UserBase(SQLModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserUpdate(SQLModel):
    email: Optional[str] = None
    is_active: Optional[bool] = None

# Event Schemas
class EventBase(SQLModel):
    name: str
    description: Optional[str] = None
    date: datetime
    max_participants: int

class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: int
    participants: List[UserRead] = []

    class Config:
        orm_mode = True

class EventUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    max_participants: Optional[int] = None

# Facility Schemas
# class FacilityBase(SQLModel):
#     name: str
#     description: Optional[str] = None
#     capacity: int
#
# class FacilityCreate(FacilityBase):
#     pass
#
# class FacilityRead(FacilityBase):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# class FacilityUpdate(SQLModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     capacity: Optional[int] = None
#
# # Booking Schemas
# class BookingBase(SQLModel):
#     start_time: datetime
#     end_time: datetime
#
# class BookingCreate(BookingBase):
#     facility_id: int
#
# class BookingRead(BookingBase):
#     id: int
#     user_id: int
#     facility_id: int
#
#     class Config:
#         orm_mode = True
#
# # Token Schemas
# class Token(SQLModel):
#     access_token: str
#     token_type: str
#
# class TokenData(SQLModel):
#     email: Optional[str] = None
