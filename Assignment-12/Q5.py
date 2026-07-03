# reverse the number upto user given number
def Reverse_number(num):
      for i in range(num,0,-1):
        print(i,end=" ")

def main():
    print("Enter a number: ")
    num = int(input())
    Reverse_number(num)

if __name__ == "__main__":
    main()