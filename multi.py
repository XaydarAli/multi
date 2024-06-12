import threading
import time
from datetime import datetime
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        print(f"Data read from {file_path}: {data}")

def main():
    file_path1 = 'file1.txt'
    file_path2 = 'file2.txt'
    file_path3 = 'file3.txt'
    file_path4 = 'file4.txt'
    file_path5 = 'file5.txt'
    file_path6 = 'file6.txt'
    file_path7 = 'file7.txt'
    file_path8 = 'file8.txt'

    # Create threads
    thread1 = threading.Thread(target=read_file, args=(file_path1,))
    thread2 = threading.Thread(target=read_file, args=(file_path2,))
    thread3 = threading.Thread(target=read_file, args=(file_path4,))
    thread4 = threading.Thread(target=read_file, args=(file_path4,))
    thread5 = threading.Thread(target=read_file, args=(file_path5,))
    thread6 = threading.Thread(target=read_file, args=(file_path6,))
    thread7 = threading.Thread(target=read_file, args=(file_path7,))
    thread8 = threading.Thread(target=read_file, args=(file_path8,))
    # Start threads
    thread1.start()
    time.sleep(2)
    thread2.start()
    time.sleep(6)
    thread3.start()
    time.sleep(4)
    thread4.start()
    time.sleep(10)
    thread5.start()
    time.sleep(3)
    thread6.start()
    time.sleep(5)
    thread7.start()
    time.sleep(7)
    thread8.start()
    time.sleep(8)

    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()

    print("Main thread continues execution.")

if __name__ == "__main__":
    main()