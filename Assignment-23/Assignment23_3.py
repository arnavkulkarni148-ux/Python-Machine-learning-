import multiprocessing
import os

def CountEven(no):
    count = 0
    for i in range(1,no+1):
        if i % 2 == 0:
            count = count + 1

    print(f"Process Id is:{os.getpid()}")
    print(f"Input number is:{no}")
    print(f"Count of Even numbers:{count}\n")

    return count

def main():
    Data = [1000000,2000000,3000000,4000000]

    with multiprocessing.Pool() as pool:
        result = pool.map(CountEven,Data)
    
    print("Result is:",result)

if __name__ == "__main__":
    main()