from database import Database
import multiprocessing
from datetime import datetime


def insert_data(query,query_type):
    print(Database.connect(query,query_type))
def select_data(query, query_type):
    print(Database.connect(query, query_type))
def process():
    query_1="INSERT INTO courses VALUES('Python',100)"
    query_2="INSERT INTO courses VALUES('English',20)"
    query_3= "INSERT INTO courses  VALUES('Java',90)"
    query_4= "INSERT INTO courses  VALUES('C++',50)"
    query_5= "INSERT INTO courses  VALUES('C#',39)"
    query_6="INSERT INTO courses  VALUES('Matematika',50)"
    query_7="INSERT INTO courses  VALUES('3ds max',28)"
    query_8="INSERT INTO courses  VALUES('Graphic desing',45)"
    query_type_1="insert"
    query_type_2="insert"
    query_type_3="insert"
    query_type_4="insert"
    query_type_5="insert"
    query_type_6="insert"
    query_type_7="insert"
    query_type_8="insert"
    process1=multiprocessing.Process(target=insert_data,args=[query_1,query_type_1])
    process2=multiprocessing.Process(target=insert_data,args=[query_2,query_type_2])
    process3=multiprocessing.Process(target=insert_data,args=[query_3,query_type_3])
    process4=multiprocessing.Process(target=insert_data,args=[query_4,query_type_4])
    process5=multiprocessing.Process(target=insert_data,args=[query_5,query_type_5])
    process6=multiprocessing.Process(target=insert_data,args=[query_6,query_type_6])
    process7=multiprocessing.Process(target=insert_data,args=[query_7,query_type_7])
    process8=multiprocessing.Process(target=insert_data,args=[query_8,query_type_8])
    #processing
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
#joining
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()
def process_select():
    query_1 = "SELECT * FROM courses WHERE name='Python'"
    query_2 = "SELECT * FROM courses WHERE name='English'"
    query_3 = "SELECT * FROM courses WHERE name='Java'"
    query_4 = "SELECT * FROM courses WHERE name='C++'"
    query_5 = "SELECT * FROM courses WHERE name='C#'"
    query_6 = "SELECT * FROM courses WHERE name='Matematika'"
    query_7 = "SELECT * FROM courses WHERE name='3ds max'"
    query_8 = "SELECT * FROM courses WHERE name='graphic desing'"
    query_type_1 = "select"
    query_type_2 = "select"
    query_type_3 = "select"
    query_type_4 = "select"
    query_type_5 = "select"
    query_type_6 = "select"
    query_type_7 = "select"
    query_type_8 = "select"
    process1 = multiprocessing.Process(target=select_data, args=[query_1, query_type_1])
    process2 = multiprocessing.Process(target=select_data, args=[query_2, query_type_2])
    process3 = multiprocessing.Process(target=select_data, args=[query_3, query_type_3])
    process4 = multiprocessing.Process(target=select_data, args=[query_4, query_type_4])
    process5 = multiprocessing.Process(target=select_data, args=[query_5, query_type_5])
    process6 = multiprocessing.Process(target=select_data, args=[query_6, query_type_6])
    process7 = multiprocessing.Process(target=select_data, args=[query_7, query_type_7])
    process8 = multiprocessing.Process(target=select_data, args=[query_8, query_type_8])
    # processing
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    # joining
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()

print("Main process continues execution.")

if __name__ == "__main__":
    print(datetime.now())
    process()
    process_select()
    print(datetime.now())

