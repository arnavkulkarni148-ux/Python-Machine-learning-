from functools import reduce

def ChkPrime(No):
        if No < 2:
            return False
        if No == 2:
            return True
        for i in range(2,No):
            if No % i == 0:
                 return False
        return True

def main():
    no = int(input("Enter a how many number do you want i the list: "))
    num=[]
    # num1 = [2,70,11,10,17,23,31,77]

    print("Enter a numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)
    
    Filter_Data = list(filter(ChkPrime,num))
    print("The list after filtering data is: ")
    print(Filter_Data)

    MData = lambda No1 : No1 * 2
    Map_Data = list(map(MData,Filter_Data))
    print("The list after maping is: ")
    print(Map_Data)
    
    RData = lambda No1,No2 : No1 if No1 > No2 else No2
    Reduce_Data = reduce(RData,Map_Data)
    print("The list after reducing the data is:")
    print(Reduce_Data)

if __name__ == "__main__":
    main()
