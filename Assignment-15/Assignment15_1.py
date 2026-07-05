# Square of each number with lambda function and help of map function 
def main():
    num = [2,3,4,5,6,7,8]

    square = lambda x: x * x  # lambda function (lambda arguments : expression )

    Data  = list(map(square , num))  # map function [map(function,iterable)]

    print("The square of each number in the list is :")
    print(Data)
    

if __name__ =="__main__":
    main()