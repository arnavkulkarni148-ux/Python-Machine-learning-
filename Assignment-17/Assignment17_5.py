# Checking whether number is prime or not 


def Chk_prime(num):
    if num <= 1:
        return True
    if num == 2:
       return False
    for i in range(2,num):
            if num % i == 0:
                return True
    return False
    
def main():
    Num = int(input("Enter a number: "))
    Ret = Chk_prime(Num)

    if Chk_prime(Num):
        print("Not a Prime Number")
    else:
        print("Prime Number")

if __name__ == "__main__":
    main()
