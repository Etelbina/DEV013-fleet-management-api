import psycopg2
import os

def connection():
    """
    This function connects with the db using the environment variables keeping them safe
    Args:
        connection: Keeps the value of the connection in a variable
        host: The host service from vercel
        user: The user of the db
        password: The password for the user
        database: The db from vercel
        port: The defoult port of vercel
    Returns:
        The value of the connection variable value
    """
    connection = psycopg2.connect(
    host = os.getenv("POSTGRES_HOST"),
    user = os.getenv("POSTGRES_USER"),
    password = os.getenv("POSTGRES_PASSWORD"),
    database = os.getenv("POSTGRES_DATABASE"),
    port = 5432
    )
    return connection

def close_crsr():
    """
    This function closes the db connection
    Args:
        crsr: Keeps the value of the connection
        closed: Applyes the close method to the cursor
    Returns:
        The value of the cursor closed
    """
    crsr = connection().cursor()
    closed = crsr.close()
    return closed