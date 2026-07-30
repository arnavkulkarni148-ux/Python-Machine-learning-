import psutil
import sys

def processInfo(processName):
    procssFound = False
    print("-"*50)
    for process in psutil.process_iter(["pid","name","username"]):
        try:
            info = process.info
            if (processName == info['name']):
                procssFound = True

                print(f"Process id is:{info['pid']}")
                print(f"Process name is:{info['name']}")
                print(f"Process username is:{info['username']}")
                print("-"*50)
        except(psutil.NoSuchProcess,psutil.AccessDenied):
            pass
    if procssFound == False:
        print("Process not found or it is not running")


def main():
    if(len(sys.argv) == 2):
         print(sys.argv[1])
         ProcessName = sys.argv[1]
         processInfo(ProcessName)
          
    else:
        print("Please enter process name in command line..")
if __name__ == "__main__":
    main()