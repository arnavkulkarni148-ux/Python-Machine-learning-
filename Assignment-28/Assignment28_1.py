import os 

def main():
    print("Enter a file name: ")
    FileName = input()
    count = 0

    ret = os.path.exists(FileName)

    if ret == True:
        fobj = open(FileName,"r")
        for lines in fobj:
            count = count + 1 
        fobj.close()
        print(f"Total Number of lines in {FileName} : {count}")    

    else:
        print("File is not present")
    
if __name__ == "__main__":
    main()