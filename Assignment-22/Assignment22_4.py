from multiprocessing import Pool
import time

def MultipleFive(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i**5)
    return sum

def main():
    numbers = [10000000,2000000,3000000,4000000]

    start_time = time.perf_counter()

    with Pool() as pool:
        result = pool.map(MultipleFive,numbers)

    end_time = time.perf_counter()
    print(result)
    print(f"Time requried is:{end_time - start_time}")



if __name__ == "__main__":
    main()