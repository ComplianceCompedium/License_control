from db_config import username, password, database, hostname
import psycopg2


def connect():
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    return  myConnection

