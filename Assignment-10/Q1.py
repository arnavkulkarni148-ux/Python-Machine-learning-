# multiplication table 

def Mult_table(num):
     for i in range(1,11):
        print(num,"X",i,"=",num*i)

def main():
    print("Enter a number : ")
    num = int(input())
    print("Multiplication table of",num,"is:")
    Mult_table(num)
  


if __name__ == "__main__":
    main()