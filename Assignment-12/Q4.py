# printing upto input number 

def main():
    print("Entet a number: ")
    num = int(input())

    for i in range(1,num+1):
        print(i,end=" ")

if __name__ == "__main__":
    main()
    