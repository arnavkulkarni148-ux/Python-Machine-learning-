#  Returning string having length more than 5 using filter() and lambda ()

def main():
    
    str1 = ["Arnav","Arya","Class","College","Hi","Python"]
    Length_string = lambda val1 : len(val1) > 5

    Data = list(filter(Length_string,str1))

    print("String having length more than five are: ")
    print(Data)

if __name__ == "__main__":
    main()