import multiprocessing
import os

def SumOdd(no):
    total = 0
    for i in range(1,no+1):
        if i % 2 != 0:
            total = total + i
    
    print(f"Process ID : {os.getpid()}")
    print(f"Input Number : {no}")
    print(f"Sum of Even Numbers : {total}\n")

    return total


def main():
    Data = [1000000,2000000,3000000,4000000]

    with multiprocessing.Pool() as pool:
        result = pool.map(SumOdd,Data)
    
    print("Final Result:",result)

if __name__ == "__main__":
    main()
