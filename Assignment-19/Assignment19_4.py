
from functools import reduce

def main():    
    no = int(input("Enter a number : "))
    num=[]
    num1=[]

    print("Enter a numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)

    FData = lambda No1 : No1 % 2 == 0
    Filter_number = list(filter(FData,num))
    print("The list after filtering data is: ")
    print(Filter_number)

    MData = lambda No1 : No1 * No1
    Map_number = list(map(MData,Filter_number))
    print("The list after maping is: ")
    print(Map_number)    

    RData = lambda No1,No2 : No1 + No2
    Reduce_number = reduce(RData,Map_number)
    print("The list after reducing data is: ")
    print(Reduce_number)

if __name__ == "__main__":
    main()
