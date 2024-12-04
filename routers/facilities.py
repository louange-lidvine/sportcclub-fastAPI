# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from services import crud
# from entities import schemas, models
# from core import security as auth
# from core.database import get_db
# from typing import List
#
# router = APIRouter()
#
#
# @router.post("/facilities/", response_model=schemas.Facility)
# async def create_facility(
#         facility: schemas.FacilityCreate,
#         db: Session = Depends(get_db),
#         current_user: models.User = Depends(auth.get_current_user),
# ):
#     # Assuming the user creating a facility is the owner
#     return crud.create_facility(db=db, facility=facility, owner_id=current_user.id)
#
#
# @router.get("/facilities/", response_model=List[schemas.Facility])
# async def read_facilities(
#         skip: int = 0,
#         limit: int = 100,
#          db: Session = Depends(get_db)
#  ):
#    # Fetch list of facilities with pagination
#     facilities = crud.get_facilities(db, skip=skip, limit=limit)
#     return facilities;
#
#
#  @router.post("/facilities/{facility_id}/book", response_model=schemas.Booking)
# async def book_facility(
#          facility_id: int,
#         booking: schemas.BookingCreate,
#       db: Session = Depends(get_db),
#        current_user: models.User = Depends(auth.get_current_user)
#  ):
# # Check if the facility exists and then create a booking
# facility = db.query(models.Facility).filter(models.Facility.id == facility_id).first()
#    if not facility:
#         raise HTTPException(status_code=404, detail="Facility not found")
#     return crud.create_booking(db=db, booking=booking, user_id=current_user.id)
#
# #
# @router.put("/facilities/{facility_id}", response_model=schemas.Facility)
# async def update_facility(
#         facility_id: int,
#         facility_update: schemas.FacilityUpdate,
#         db: Session = Depends(get_db),
#         current_user: models.User = Depends(auth.get_current_user),
# ):
#     # Fetch the facility to update
#     db_facility = db.query(models.Facility).filter(models.Facility.id == facility_id).first()
#     if not db_facility:
#         raise HTTPException(status_code=404, detail="Facility not found")
#     # Check if the current user is the owner of the facility before allowing updates
#     if db_facility.owner_id != current_user.id:
#      raise HTTPException(status_code=403, detail="Not authorized to update this facility")
#
#     # Perform the update using the CRUD service
#     updated_facility = crud.update_facility(db=db, db_facility=db_facility, facility_update=facility_update)
#     return updated_facility
#
#
# @router.delete("/facilities/{facility_id}", response_model=dict)
# async def delete_facility(
#         facility_id: int,
#         db: Session = Depends(get_db),
#         current_user: models.User = Depends(auth.get_current_user),
# ):
#     # Fetch the facility to delete
#     db_facility = db.query(models.Facility).filter(models.Facility.id == facility_id).first()
#     if not db_facility:
#         raise HTTPException(status_code=404, detail="Facility not found")
#     # Ensure the current user is the owner of the facility
#     if db_facility.owner_id != current_user.id:
#         raise HTTPException(status_code=403, detail="Not authorized to delete this facility")
#
#     # Perform the delete operation
#     crud.delete_facility(db=db, facility_id=facility_id)
#     return {"message": f"Facility with ID {facility_id} successfully deleted"}
