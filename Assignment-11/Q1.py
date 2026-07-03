# Prime numbwer checker

def Check_prime(num):
    if num <= 2:
       return False
    for i in range(2,num):
            if num % i == 0:
                return True
    return False
    


def main():
    print("Enter a number : ")
    num = int(input())
    # prime_number = True 

    # if num <= 2:
    #     print(num,"is not a prime number")

    # else:

    #     for i in range(2,num):
    #         if num % i == 0:
    #             prime_number = False
    #         break
    
    if Check_prime(num):
        print(num,"is not a Prime number")
    else:
        print(num,"is Prime number")
            

if __name__ == "__main__":
    main()
