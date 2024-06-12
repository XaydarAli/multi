import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()
class Database:
    @staticmethod
    def connect(query:str,query_type:str):
        db=psql.connect(
            database=os.getenv('db_name'),
            user=os.getenv('db_user'),
            host=os.getenv('db_host'),
            password=os.getenv('db_password'),
            port=os.getenv('db_port')

        )
        cursor=db.cursor()
        data=["insert","delete","update","alter"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "inserted data"

        else:
            return cursor.fetchall()

