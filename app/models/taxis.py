from flask import request
from ..conection_postgrestsql import connection

def get_taxi_from_db():
   limit = request.args.get("limit", default=10)
   page = request.args.get("page", default=1)
   crsr = connection().cursor()
   crsr.execute(f"SELECT * FROM taxis ORDER BY id ASC LIMIT {limit} OFFSET {page};")
   return crsr.fetchall()