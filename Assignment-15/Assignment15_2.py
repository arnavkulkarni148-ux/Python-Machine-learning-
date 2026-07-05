# list of even numbers using lambda() and filter ()
def main():

    no = int(input("Enter how many number do you want in list : "))
    num = []

    print("Enter a numbers: ")

    for i in range(no):
        value = int(input())
        num.append(value)
        
    Even_number = lambda x : x % 2 == 0

    Data = list(filter(Even_number,num))
    print("Even numbers from the list are: ")
    print(Data)  

if __name__ == "__main__":
    main()