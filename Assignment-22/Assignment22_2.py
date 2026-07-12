from multiprocessing import Pool
import os

def Fact_number(No):

    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    print(f"Process Id is:{os.getpid()}")
    return fact

def main():
    numbers = [10,15,20,25]

    with Pool() as pool:
        result = pool.map(Fact_number,numbers)
    print(result)

if __name__ == "__main__":
    main()