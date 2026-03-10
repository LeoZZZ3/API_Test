import mysql.connector

class ORM:
    def __init__(self, host, user, password, database):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    def select_all(self, table):
        db = self._get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {table}")
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result

    def insert(self, table, data):
        db = self._get_connection()
        cursor = db.cursor()
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, list(data.values()))
        db.commit()
        inserted_id = cursor.lastrowid
        cursor.close()
        db.close()
        return inserted_id

    def update(self, table, data, id_value, id_column="id"):
        db = self._get_connection()
        cursor = db.cursor()
        set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE {id_column} = %s"
        params = list(data.values()) + [id_value]
        cursor.execute(sql, params)
        db.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        db.close()
        return rows_affected

    def delete(self, table, id_value, id_column="id"):
        db = self._get_connection()
        cursor = db.cursor()
        sql = f"DELETE FROM {table} WHERE {id_column} = %s"
        cursor.execute(sql, (id_value,))
        db.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        db.close()
        return rows_affected