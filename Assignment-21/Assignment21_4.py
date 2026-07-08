
import threading

def SumNumber(Lst):
    sum = 0
    for i in Lst:
        sum = sum + i
    print("Sum of elements:",sum)

def ProductNumber(Lst):
    product = 1
    for i in Lst:
        product = product * i
    print("Product of elements:",product)


def main():
    no = int(input("Enter how many numbers do you want in the list: "))
    num=[]
    for i in range(no):
        value = int(input())
        num.append(value)

    thread1 = threading.Thread(target=SumNumber,args=(num,))
    thread2 = threading.Thread(target=ProductNumber,args=(num,))

    thread1.start()
    thread2.start()

    thread1.join()

    thread2.join()


if __name__ == "__main__":
    main()