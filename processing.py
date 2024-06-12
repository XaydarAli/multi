import multiprocessing
from datetime import datetime
import time
def write_to_file(file_path, data):
    time.sleep(3)
    with open(file_path, 'r+') as file:
        file.write(data)
        print(f"Data written to {file_path}\n")

def main():
    file_path1 = 'data1.txt'
    file_path2 = 'data2.txt'
    data1 = 'Hello from Process 1!'
    data2 = 'Greetings from Process 2!'

    # Create processes
    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2, data2))

    # Start processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())