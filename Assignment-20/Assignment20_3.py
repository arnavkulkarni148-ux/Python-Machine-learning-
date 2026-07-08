# Dsiplay Eventhread and OddThread 

import threading

def EvenLst(lst1):
    sum = 0
    EvenNumbers = []
    for i in lst1:
        if i % 2 == 0:
            EvenNumbers.append(i)
            sum = sum + i
    print("Even Numbers:",EvenNumbers)
    print("Sum =",sum)

def OddLst(lst2):
    sum = 0
    OddNumbers = []
    for i in lst2:
        if i % 2 != 0:
            OddNumbers.append(i)
            sum = sum + i
    print("Odd Numbers:",OddNumbers)
    print("Sum =",sum)

def main():
    no = int(input("Enter how many numbers do you want in the list: "))
    num=[]
    print("Enter a numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)

    EvenList = threading.Thread(target=EvenLst,args=(num,))
    OddList = threading.Thread(target=OddLst,args=(num,))

    EvenList.start()
    OddList.start()

    # EvenList.join()
    # OddList.join()
    

if __name__ == "__main__":
    main()