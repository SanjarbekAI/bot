import psycopg2 as db


class Database:
    @staticmethod
    def connect(query, query_type, fetchall=False, fetchone=False, fetchmany=False):
        database = db.connect(
            database='n41',
            password='sanjarbek2002',
            user='postgres',
            host='localhost'
        )
        cursor = database.cursor()
        cursor.execute(query=query)

        query_types = ['insert', 'update', 'delete', 'create']
        if query_type in query_types:
            database.commit()
            return "Done"
        else:
            if fetchall:
                return cursor.fetchall()
            elif fetchone:
                return cursor.fetchone()
            elif fetchmany:
                return cursor.fetchmany()
            return cursor.fetchall()
            
            