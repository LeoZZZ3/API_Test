import mysql.connector

class ORM:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    def select_all(self, table):
        db = self._get_connection()
        # On utilise dictionary=True pour que fetchall() retourne des listes de dictionnaires
        # ex: [{"id": 1, "nom": "Léo"}, ...] au lieu de [(1, "Léo"), ...]
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
        cursor.close()
        db.close()

    def update(self, table, data, condition_id):
        db = self._get_connection()
        cursor = db.cursor()
        set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE id = %s"
        params = list(data.values()) + [condition_id]
        cursor.execute(sql, params)
        db.commit()
        cursor.close()
        db.close()

    def delete(self, table, condition_id):
        db = self._get_connection()
        cursor = db.cursor()
        sql = f"DELETE FROM {table} WHERE id = %s"
        cursor.execute(sql, (condition_id,))
        db.commit()
        cursor.close()
        db.close()