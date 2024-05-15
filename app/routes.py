from flask import Flask, jsonify
from .models.taxis import get_taxi_from_db
from .models.trajectories import get_trajectories_from_db, get_latest_from_db
from .utils import taxis_serializer, trajectories_serializer, latest_serializer
from .conection_postgrestsql import close_crsr

app = Flask(__name__)

@app.route("/")
def home_page():
   """
   A simple function to test the home page
   """
   return "Home"

@app.route("/taxis", methods=["GET"])
def get_taxis():
   """
   This function creates the route for the trajectories views,
   gets the data from the db, 
   executes the function to close the connection
   and returns the array of taxis
   Args:
      tuples_trajectories: Executes the function to get the data from the db
   Returns:
      The taxis tuple transformed to a Json format
   """
   tuples_taxis = get_taxi_from_db()
   close_crsr()
   return jsonify(taxis_serializer(tuples_taxis))

# ToDo qué hace @app.route
@app.route("/trajectories", methods=["GET"])
def get_trajectories():
   """
   This function creates the route for the trajectories views,
   gets the data from the db, 
   executes the function to close the connection
   and returns the array of trajectories
   Args:
      tuples_trajectories: Executes the function to get the data from the db
   Returns:
      The trajectories tuple transformed to a Json format
   """
   tuples_trajectories = get_trajectories_from_db()
   close_crsr()
   return jsonify(trajectories_serializer(tuples_trajectories))

@app.route("/trajectories/latest", methods=["GET"])
def get_latest_trajectory():
   """
   This function creates the route for the last trajectories views
   gets the data from the db, 
   executes the function to close the connection
   and returns the array of the latest trajectories
   Args:
      tuple_latest: Executes the function to get the data from the db
   Returns:
      The latest trajectories tuple transformed to a Json format
   """
   tuple_latest = get_latest_from_db()
   close_crsr()
   return jsonify(latest_serializer(tuple_latest))

if __name__ == "__main__":
    app.run(debug=True)