
import threading

def Maximum(lst):
    Max_number = max(lst)
    print("Maximum number:",Max_number)

def Minimum(lst):
    Min_number = min(lst)
    print("Minimum Number:",Min_number)

def main():
    no = int(input("Enter how many numbers do you want un the list: "))
    num=[]

    for i in range(no):
        value = int(input())
        num.append(value)
    
    thread1 = threading.Thread(target=Maximum,args=(num,))
    thread2 = threading.Thread(target=Minimum,args=(num,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    


if __name__ == "__main__":
    main()