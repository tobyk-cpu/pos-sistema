import sqlite3

class ConexionBD:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        
    def create_table(self, create_table_sql):
        try:
            self.cursor.execute(create_table_sql)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def execute_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def close_connection(self):
        self.connection.close()