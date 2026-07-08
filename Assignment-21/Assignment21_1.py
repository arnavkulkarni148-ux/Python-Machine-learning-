
import threading

# Global lists to store the results
# primes = []
# non_primes = []

def PrimeNum(number_list):
    primes=[]
    for No in number_list:
        if No < 2: 
            continue
        prime_number = True

        for i in range(2, No):
            if No % i == 0:
                prime_number = False
                break
        if prime_number:
            primes.append(No)
    print("Prime Numbers:",primes)
        
def NonPrimeNum(number_list):
    non_primes = []
    for No in number_list:
        if No <= 1:
            non_primes.append(No)
            continue
       
        for i in range(2, No):
            if No % i == 0:
                non_primes.append(No)
                break
    print("Non Prime Number:",non_primes)
          
def main():
    no = int(input("Ente how many numbers do you want in the list: "))
    num = []

    print("Enter a numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)

    Prime = threading.Thread(target=PrimeNum,args=(num,))
    NonPrime = threading.Thread(target=NonPrimeNum,args=(num,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()
    
if __name__ == "__main__":
    main()