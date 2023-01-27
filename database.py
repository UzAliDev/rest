import sqlite3

class Database:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table_users(self):
        return self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            username VARCHAR(255),
            first_name VARCHAR(255),
            data VARCHAR(255),
            PRIMARY KEY (id)
            );
        """)

    def add(self, user_id):
        with self.conn:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,))
            return bool(len(result.fetchall()))

    def add_id(self, user_id):
        with self.conn:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id, ))

    def add_id_user(self, user_id, username):
        with self.conn:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `username`) VALUES (?, ?)", (user_id, username, ))

    def add_id_user_name(self, user_id, username, first_name):
        with self.conn:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `username`, `first_name`) VALUES (?, ?, ?)", (user_id, username, first_name, ))

    def add_id_user_name_data(self, user_id, username, first_name, data):
        with self.conn:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `username`, `first_name`, `data`)" "VALUES (?, ?, ?, ?)", (user_id, username, first_name, data, ))
     
    def add_id_user_data(self, user_id, username, data):
        with self.conn:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `username`, `data`) VALUES (?, ?, ?)", (user_id, username, data))

    def delete(self, user_id, username, first_name, data):
        with self.conn:
            return self.cursor.execute("DELETE FROM `users` WHERE `user_id` = ? and `username` = ? and `first_name` = ? and `data` = ?", (user_id, username, first_name, data))

    def count(self):
        res = self.cursor.execute("SELECT COUNT (*) FROM users")
        return res.fetchone()[0]
