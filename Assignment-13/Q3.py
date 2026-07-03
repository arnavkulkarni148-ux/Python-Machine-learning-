# Perfect number checker
def main():
    print("Enter a number :")
    num = int(input())
    Perfect_number = False
    sum = 0

    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
        if sum == num:
            Perfect_number = True 

    if Perfect_number == True:
        print(num,"is a pefect number")
    else:
        print(num,"is not a perfect number")




if __name__ == "__main__":
    main()