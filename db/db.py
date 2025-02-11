import psycopg2


def connect():
    return psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="postgres", port=5432)
 