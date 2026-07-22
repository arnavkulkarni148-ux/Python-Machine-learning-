import os
import sys

def main():
    if (len(sys.argv) == 2):
        FileName = sys.argv[1]
        Ret = os.path.exists(FileName)
        if Ret:
           fobj = open(FileName,"r")
           fobj1 = open("Demo.txt","w")

           for line in fobj:
            #    print(line)
               fobj1.write(line)
           print(f"Create Demo.txt and copy contents of {FileName} into Demo.txt")   
           fobj.close()
           fobj1.close()
        else:
            print("File not Exists ")
    else:
        print("Provide the file name in command line..")

if __name__ == "__main__":
    main()