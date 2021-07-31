import threading
import time

#starting time 
s_time = time.time()

def time_elapsed(): #helper function to evaluate time
  now = time.time()
  res = int(now - s_time) 
  return res

class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event() # The flag used to pause the thread
        self.__flag.set() # Set to True
        self.__running = threading.Event() # Used to stop the thread identification
        self.__running.set() # Set running to True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait() # return immediately when it is True, block until the internal flag is True when it is False
            print('Thread 1 is running at {}'.format(time_elapsed()))
            time.sleep(5)

    def pause(self):
        self.__flag.clear() # Set to False to block the thread

    def resume(self):
        self.__flag.set() # Set to True, let the thread stop blocking

    def stop(self):
        self.__flag.set() # Resume the thread from the suspended state, if it is already suspended
        self.__running.clear() # Set to False

class Job2(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job2, self).__init__(*args, **kwargs)
        self.__flag = threading.Event() # The flag used to pause the thread
        self.__flag.set() # Set to True
        self.__running = threading.Event() # Used to stop the thread identification
        self.__running.set() # Set running to True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait() # return immediately when it is True, block until the internal flag is True when it is False
            print('Thread 2 is running at {}'.format(time_elapsed()))
            time.sleep(5)

    def pause(self):
        self.__flag.clear() # Set to False to block the thread

    def resume(self):
        self.__flag.set() # Set to True, let the thread stop blocking

    def stop(self):
        self.__flag.set() # Resume the thread from the suspended state, if it is already suspended
        self.__running.clear() # Set to False

class Job3(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job3, self).__init__(*args, **kwargs)
        self.__flag = threading.Event() # The flag used to pause the thread
        self.__flag.set() # Set to True
        self.__running = threading.Event() # Used to stop the thread identification
        self.__running.set() # Set running to True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait() # return immediately when it is True, block until the internal flag is True when it is False 
            print('Thread 3 is running at {}'.format(time_elapsed()))
            time.sleep(5)


    def pause(self):
        self.__flag.clear() # Set to False to block the thread

    def resume(self):
        self.__flag.set() # Set to True, let the thread stop blocking

    def stop(self):
        self.__flag.set() # Resume the thread from the suspended state, if it is already suspended
        self.__running.clear() # Set to False

obj = Job()
obj2 = Job2()
obj3 = Job3()

obj.start()
obj3.start()
obj.join(timeout=20)
obj.pause()
print('Thread 1 will stop after 20s and Thread 2 will start')
obj2.start()
obj3.join(timeout=18)
obj3.stop()
print('Thread3 will stop and Thread 1 will start again')
obj.resume()
