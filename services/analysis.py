# from typing import Dict, Any
#
# import pandas as pd
# from sqlalchemy.orm import Session
# from fastapi import HTTPException
#
# from entities import models
#
#
# class SportsClubAnalytics:
#     def __init__(self, db: Session):
#         self.db = db
#         self.events_df = self._get_events_df()
#         self.users_df = self._get_users_df()
#
#     def _get_events_df(self) -> pd.DataFrame:
#         try:
#             events_query = self.db.query(models.Event).all()
#             if not events_query:
#                 return pd.DataFrame(columns=['id', 'name', 'date', 'location'])
#             return pd.DataFrame([{
#                 'id': event.id,
#                 'name': event.name,
#                 'date': event.date,
#                 'location': event.location,
#             } for event in events_query])
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Error getting events data: {str(e)}")
#
#     def _get_users_df(self) -> pd.DataFrame:
#         try:
#             users_query = self.db.query(models.User).all()
#             if not users_query:
#                 return pd.DataFrame(columns=['id', 'name', 'age', 'role'])
#             return pd.DataFrame([{
#                 'id': user.id,
#                 'name': user.name,
#                 'age': user.age,
#                 'role': user.role,
#             } for user in users_query])
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Error getting users data: {str(e)}")
#
#
#
#     def get_ordinal_analysis(self) -> Dict[str, Any]:
#         try:
#             if self.users_df.empty:
#                 return {
#                     'age_group_distribution': {},
#                 }
#
#             # Binning ages into groups for ordinal analysis
#             age_bins = [0, 18, 30, 40, 50, 60, 100]
#             age_labels = ['<18', '18-30', '30-40', '40-50', '50-60', '60+']
#             self.users_df['age_group'] = pd.cut(self.users_df['age'], bins=age_bins, labels=age_labels)
#
#             age_dist = self.users_df['age_group'].value_counts().to_dict()
#
#             return {
#                 'age_group_distribution': age_dist,
#             }
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Error analyzing ordinal data: {str(e)}")
#
#
#     def get_complex_analysis(self) -> Dict[str, Any]:
#         try:
#             if self.events_df.empty or self.users_df.empty:
#                 return {
#                     'user_event_participation': {},
#                 }
#
#             # Example: How many users attend each event
#             event_participation = self.events_df.merge(self.users_df, left_on='id', right_on='event_id')
#             participation_count = event_participation.groupby('event_id')['user_id'].count().to_dict()
#
#             return {
#                 'user_event_participation': participation_count,
#             }
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Error in complex analysis: {str(e)}")
#
#
#
