# printing upto input number 
def Natural_number(num):
     for i in range(1,num+1):
        print(i,end=" ")

def main():
    print("Entet a number: ")
    num = int(input())
    Natural_number(num)

if __name__ == "__main__":
    main()
    