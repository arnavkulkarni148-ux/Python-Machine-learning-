
import threading

def Forward_order(num):
    for i in range(1,num+1):
        print(i,end=" ")
    print()

def Reverse_order(num):
    for i in range(num,0,-1):
        print(i,end=" ")

def main():
    thread1 = threading.Thread(target=Forward_order,args=(50,))
    thread2 = threading.Thread(target=Reverse_order,args=(50,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()