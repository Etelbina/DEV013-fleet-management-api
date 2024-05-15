from flask import request
from ..conection_postgrestsql import connection

def get_trajectories_from_db():
   """
      This function connects with the db to get all the trajectories of an specific taxi and date
      Args:
         limit: The limit of taxis for page, 10 by default
         page: The page to show, 1 by default
         taxi: The taxi, 6418 by default
         date: The date, 2008-02-02 by default
         crsr: keeps the value of the connection function so we
               can execute the methods to manipulate the db data
      Returns:
         A tuple with the requested trajectories
   """
   limit = request.args.get("limit", default=10)
   page = request.args.get("page", default=1)
   taxi = request.args.get("taxi_id", default=6418)
   date = request.args.get("date", default='2008-02-02')
   crsr = connection().cursor()
   crsr.execute(f"SELECT * FROM trajectories WHERE taxi_id={taxi} AND CAST(date AS DATE) = '{date}' ORDER BY taxi_id ASC LIMIT {limit} OFFSET {page};")
   return crsr.fetchall()

def get_latest_from_db():
   """
      This function connects with the db to get the latest trajectories of every taxi
      Args:
         limit: The limit of taxis for page, 10 by default
         page: The page to show, 1 by default
         crsr: keeps the value of the connection function so we
               can execute the methods to manipulate the db data
      Returns:
         A tuple with the requested trajectories
   """
   limit = request.args.get("limit", default=10)
   page = request.args.get("page", default=1)
   crsr = connection().cursor()
   crsr.execute(f"SELECT DISTINCT ON (taxi_id) * FROM taxis JOIN trajectories ON taxis.id = trajectories.taxi_id ORDER BY taxi_id ASC, date DESC LIMIT {limit} OFFSET {page};")
   return crsr.fetchall()

