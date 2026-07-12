import multiprocessing
import os

def FactNum(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    print(f"Process Id is:{os.getpid()}")
    print(f"Input number is:{no}")
    print(f"Factorial is:{fact}\n")

    return fact

def main():
    Data = [10,15,20,25]

    with multiprocessing.Pool() as pool:
        result = pool.map(FactNum,Data)
    
    
    print("Final Result:",result)

if __name__ == "__main__":
    main()