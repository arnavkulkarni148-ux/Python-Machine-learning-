import psutil
import os
import sys
import time

def DisplayProcess(LogFileName):
    fobj = open(LogFileName,"w")
    fobj.write("-"*50+"\n")
    fobj.write("Information of Running Processes\n")
    fobj.write("-"*50+"\n")

    for process in psutil.process_iter(["pid","name","username"]):
        try:
            info = process.info

            fobj.write(f"Process Name :{info['name']}\n")
            fobj.write(f"PID :{info['pid']}\n")
            fobj.write(f"Username :{info['username']}\n")
            fobj.write("-"*50+"\n")

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    fobj.close()

def CreateLogFile(DirectoryName):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = "Marvellous_%s.log" %timestamp
    logFile = os.path.join(DirectoryName,FileName)
    print("Log File Created Successfully")
    DisplayProcess(logFile)

def DirectoryCheck(FolderName):
    Ret = os.path.exists(FolderName)

    if Ret == True:
        Ret = os.path.isdir(FolderName)

        if Ret == False:
            print("Unable to proceed as the given path exists but it is not a directory.")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets created successfully")

    CreateLogFile(FolderName)

def main():
    if len(sys.argv) == 2:
        directoryName = sys.argv[1]
        DirectoryCheck(directoryName)
    else:
        print("Error: Invalid number of arguments")
        print("Please enter directory name in command line..")
        print("python filename directoryname: <- Provide like these")

if __name__ == "__main__":
    main()