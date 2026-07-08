# Creating two seprate thread to display even and odd number 

import threading

def EvenNumber(No):
    print("First 10 Even Numbers are:")
    for i in range(2,No+1,2):
        print(i,end=" ")
    print("\n")

def OddNumber(No):
    print("First 10 Odd Numbers are:")
    for i in range(1,No+1,2):
        print(i,end=" ")

def main():
    
    EvenThread = threading.Thread(target=EvenNumber,args=(20,))
    OddThread = threading.Thread(target=OddNumber,args=(20,))

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

if __name__ == "__main__":
    main()
