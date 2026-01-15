import mysql.connector
from mysql.connector import Error
from config.db_config import DB_CONFIG

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "connection") or self.connection is None:
            try:
                self.connection = mysql.connector.connect(**DB_CONFIG)
                if self.connection.is_connected():
                    print(" Database Connected Successfully")
            except Error as e:
                print(f" Database Connection Failed: {e}")
                self.connection = None

    def get_connection(self):
        return self.connection