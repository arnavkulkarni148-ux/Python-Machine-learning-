from multiprocessing import Pool

def Prime_check(No):
    if No <= 1:
        return False
    if No == 2:
        return True
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

def Prime_count(No):
    count = 0

    for i in range(1,No+1):
        if Prime_check(i):
            count = count + 1
    return count

def main():
    
    numbers = [10000,20000,30000,40000]

    with Pool() as pool:
        result = pool.map(Prime_count,numbers)

    print(f"The Prime Number between {numbers} is :")
    print(result)

if __name__ == "__main__":
    main()
