# Display the EvenFactor and OddFactor using thread

import threading

def EvenFact(num):
    sum = 0
    # print("Even Factors:")
    for i in range(1,num):
        if num % i == 0:
            if i % 2 == 0:
                    sum = sum + i
                    print(i,end=" ")
    print("\nSum of Even number is:",sum)

def OddFact(num):
    sum = 0
    # print("Odd factors:")
    for i in range(1,num):
          if num % i == 0:
               if i % 2 != 0:
                    sum = sum + i
                    print(i,end=" ")
    print("\nSum of Odd number is:",sum)

def main():
    no = int(input("Enter a number: "))

    EvenFactor = threading.Thread(target=EvenFact,args=(no,))
    OddFactor = threading.Thread(target=OddFact,args=(no,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from Main..")

if __name__ == "__main__":
    main()