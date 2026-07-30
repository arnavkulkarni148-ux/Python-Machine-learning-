import psutil

def ProcesssInfo():
    print("-"*50)
    print("Information of Running Processes")
    print("-"*50)

    for process in psutil.process_iter(["pid","name","username"]):
        try:
            info = process.info
            print(f"Pid of process is:{info['pid']}")
            print(f"Name of process is:{info['name']}")
            print(f"USername of process is:{info['username']}")
            print("-"*50)
        except (psutil.NoSuchProcess,psutil.AccessDenied):
            pass

def main():
    ProcesssInfo()

if __name__ == "__main__":
    main()