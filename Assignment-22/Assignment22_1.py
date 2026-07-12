from multiprocessing import Pool 

def Sum_Square(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i*i)
    return sum

def main():
    Numbers = [1000000,20000000,30000000,4000000]

    with Pool() as pool:
        results = pool.map(Sum_Square,Numbers)
    print(results)

if __name__ == "__main__":
    main()