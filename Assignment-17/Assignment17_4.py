# Addition of factors of a number 

def Add_Factors(No):
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            sum = sum + i
    return sum

def main():
    Num = int(input("Enter a number: "))
    Ret = Add_Factors(Num)

    print(f"The Addition of factors of {Num} is {Ret}")

if __name__ == "__main__":
    main()