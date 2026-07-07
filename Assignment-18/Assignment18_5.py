# Return addition of prime numbers from the list 

import MarvellousNum

def ListPrime(lst):
    PrimeSum = 0
    for i in lst:
        Ret = MarvellousNum.ChkPrime(i)
        if Ret == True:
            PrimeSum = PrimeSum + i
    return PrimeSum 


def main():
    no = int(input("enter how many numbers do you want in the list: "))
    num = []

    print("Enter a numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)

    Ret = ListPrime(num)

    print("The Addition of prime number in the list is :",Ret)

if __name__ == "__main__":
    main()