from flask import request
from ..conection_postgrestsql import connection

def get_taxi_from_db():
   """
      This function connects with the db to get the id and plate of all the taxis
      Args:
         limit: The limit of taxis for page, 10 by default
         page: The page to show, 1 by default
         crsr: keeps the value of the connection function so we
               can execute the methods to manipulate the db data
      Returns:
         A tuple with the requested taxis
   """
   limit = request.args.get("limit", default=10)
   page = request.args.get("page", default=1)
   crsr = connection().cursor()
   crsr.execute(f"SELECT * FROM taxis ORDER BY id ASC LIMIT {limit} OFFSET {page};")
   return crsr.fetchall()