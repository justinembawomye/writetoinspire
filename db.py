import psycopg2
from pprint import pprint

class MyDatabase:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(dbname='flaskblog', host='localhost', user='postgres', password='1234', port='5432')
            self.connection.autocommit=True
            self.cursor = self.connection.cursor()

        except:
            pprint('Failed to connect to the database')
    def create_table(self):
        create_table_command = "CREATE TABLE users(id serial PRIMARY_KEY, username VARCHAR(50) NOT NULL, email VARCHAR(100) NOT NULL, password VARCHAR(50) NOT NULL)"
        self.cursor.execute(create_table_command)


if __name__=='__main__':
    database_connection = MyDatabase()
    database_connection.create_table()

