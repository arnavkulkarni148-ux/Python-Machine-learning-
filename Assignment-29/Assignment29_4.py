import os
import sys

def main():
    Data1 = []
    Data2 = []
    if (len(sys.argv) == 3):
        FileName1 = sys.argv[1]
        FileName2 = sys.argv[2]

        if (os.path.exists(FileName1) and (os.path.exists(FileName2))):
            fobj1 = open(FileName1,"r")
            fobj2 = open(FileName2,"r")
            for i in fobj1:
                Data1.append(i)
            for i in fobj2:
                Data2.append(i)

            if Data1 == Data2:
                print("Sucess")
            else:
                print("Failure")
                
            fobj1.close()
            fobj2.close()
        else:
            print("File not Exists in the current diractory....")
    else:
        print("Please enter two file names in command line ")

if __name__ == "__main__":
    main()