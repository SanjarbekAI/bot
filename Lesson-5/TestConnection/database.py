import psycopg2 as db


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database='test41',
            password='sanjarbek2002',
            user='postgres',
            host='localhost'
        )
        cursor = database.cursor()
        cursor.execute(query)

        data = ['insert', 'update', 'delete', 'create']
        if query_type in data:
            database.commit()
            return "Done"
        else:
            return cursor.fetchall()



