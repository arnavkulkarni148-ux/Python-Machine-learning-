import threading

counter = 0
counter_lock = threading.Lock()

def IncrementCounter(no_of_times):
    global counter
    for i in range(no_of_times):
        counter_lock.acquire()
        counter = counter + 1
        counter_lock.release()

def main():
   
    no = int(input("Enter how many times each thread should increment: "))

    t1 = threading.Thread(target=IncrementCounter, args=(no,))
    t2 = threading.Thread(target=IncrementCounter, args=(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExpected Value:", no * 2)
    print("Final Counter Value:", counter)

if __name__ == "__main__":
    main()