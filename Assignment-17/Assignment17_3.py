# Returning Factorial of number 

def Fact_number(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    return Fact

def main():
    Value = int(input("Enter a number : "))

    Ret = Fact_number(Value)

    print(f"The Factorial of {Value} is : {Ret}")

if __name__ == "__main__":
    main()