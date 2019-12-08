# from multiprocessing import Process, Lock

# mutex = Lock()

# def processData(data):
#     with mutex:
#         print('Do some stuff')

# if __name__ == '__main__':
#     while True:
#         p = Process(target = processData, args = (some_data,))
#         p.start()




# https://www.geeksforgeeks.org/mutex-lock-for-linux-thread-synchronization/


from threading import Thread, Lock

mutex = Lock()

def processData(data):
    mutex.acquire()
    try:
        print('Do some stuff')
    finally:
        mutex.release()

while True:
    t = Thread(target = processData, args = (some_data,))
    t.start()