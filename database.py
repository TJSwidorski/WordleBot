import sqlite3
import json

class WordleDatabase:
    @staticmethod
    def create_lists_table(connection):
        """
        Create the lists table in the database.

        :param connection: SQLite database connection
        """
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lists (
                id INTEGER PRIMARY KEY,
                list_name TEXT,
                list_data TEXT
            )
        """)
        connection.commit()

    @staticmethod
    def create_dicts_table(connection):
        """
        Create the dictionaries table in the database.

        :param connection: SQLite database connection
        """
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dictionaries (
                id INTEGER PRIMARY KEY,
                dict_name TEXT,
                dict_data TEXT
            )
        """)
        connection.commit()

    @staticmethod
    def insert_list(connection, list_name, list_data):
        """
        Insert a list into the database.

        :param connection: SQLite database connection
        :param list_name: Name of the list
        :param list_data: List data
        """
        serialized_data = json.dumps(list_data)  # Serialize the list to JSON string
        cursor = connection.cursor()
        cursor.execute("INSERT INTO lists (list_name, list_data) VALUES (?, ?)", (list_name, serialized_data))
        connection.commit()

    @staticmethod
    def insert_dict(connection, dict_name, dict_data):
        """
        Insert a dictionary into the database.

        :param connection: SQLite database connection
        :param dict_name: Name of the dictionary
        :param dict_data: Dictionary data
        """
        serialized_data = json.dumps(dict_data)  # Serialize the dictionary to JSON string
        cursor = connection.cursor()
        cursor.execute("INSERT INTO dictionaries (dict_name, dict_data) VALUES (?, ?)", (dict_name, serialized_data))
        connection.commit()
  
    @staticmethod
    def retrieve_list(connection, list_name):
        """
        Retrieve a specific list from the database.

        :param connection: SQLite database connection
        :param list_name: Name of the list
        :return: List data
        """
        cursor = connection.cursor()
        cursor.execute("SELECT list_data FROM lists WHERE list_name = ?", (list_name,))
        serialized_data = cursor.fetchone()[0]
        if serialized_data:
            return json.loads(serialized_data)  # Deserialize JSON string back to a list
        else:
            return None

    @staticmethod
    def retrieve_dict(connection, dict_name):
        """
        Retrieve a specific dictionary from the database.

        :param connection: SQLite database connection
        :param dict_name: Name of the dictionary
        :return: Tuple (id, dict_name, dict_data)
        """
        cursor = connection.cursor()
        cursor.execute("SELECT dict_data FROM dictionaries WHERE dict_name = ?", (dict_name,))
        serialized_data = cursor.fetchone()[0]
        if serialized_data:
            return json.loads(serialized_data)  # Deserialize JSON string back to a dictionary
        else:
            return None