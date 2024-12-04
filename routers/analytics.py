# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from services import crud
# from entities import schemas, models
# from core import security as auth
# from core.database import get_db
# from typing import List
#
# from services.analysis import SportsClubAnalytics
#
# router = APIRouter()
# @router.get("/sports-club-analytics/")
# def get_sports_club_analytics(db: Session = Depends(get_db)):
#     analytics = SportsClubAnalytics(db)
#     return {
#         'basic_stats': analytics.get_basic_stats(),
#         'categorical_analysis': analytics.get_categorical_analysis(),
#         'ordinal_analysis': analytics.get_ordinal_analysis(),
#         'complex_analysis': analytics.get_complex_analysis(),
#     }