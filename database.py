import sqlite3
from datetime import datetime

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('todolistDB.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS list (
                id INTEGER PRIMARY KEY,
                todo TEXT,
                time TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS datelist (
                date TEXT
            )
        ''')
        self.conn.commit()

    def checkDate(self):
        todaysdate = datetime.now().date()
        date = self.cursor.execute('SELECT date FROM datelist').fetchone()
        if date is None:
            self.cursor.execute('INSERT INTO datelist VALUES (?)',(str(todaysdate),))
        else:
            fetcheddateobject = datetime.strptime(date[0],'%Y-%m-%d').date()
            if todaysdate != fetcheddateobject:
                self.cursor.execute('DELETE FROM list')
                self.cursor.execute('DELETE FROM datelist')
                self.cursor.execute('INSERT INTO datelist VALUES (?)',(str(todaysdate),))
        self.conn.commit()

    def fetchAll(self):
        data = self.cursor.execute('SELECT * FROM list')
        return data.fetchall()

    def insert(self, text):
        current_time = datetime.now().strftime('%I:%M:%S %p')
        self.cursor.execute('INSERT INTO list VALUES (NULL,?,?)', (text, current_time))
        self.conn.commit()

    def update(self, id, todo):
        self.cursor.execute('UPDATE list SET todo=? WHERE id=?', (todo, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('DELETE FROM list WHERE id=?', (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
