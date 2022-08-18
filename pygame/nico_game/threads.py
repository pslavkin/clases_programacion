import threading
import time

n1=0
n2=0

def f1():
    global n1
    while True:
        n1=n1+1
        print("f1: ",n1)
        time.sleep(0.1)

def f2():
    global n2
    while True:
        n2=n2+1
        print("f2: ",n2)
        time.sleep(1.8)


if __name__ == "__main__":

    taskF1 = threading.Thread(target=f1)
    taskF1.start()

    taskF2 = threading.Thread(target=f2)
    taskF2.start()
