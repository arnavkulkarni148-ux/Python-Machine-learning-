import schedule
import time

def Display(Message):
    print(Message)

def main(): 
    print("Enter a message : ")
    Message = input()
    print("Enter a time interval in seconds : ")
    TimeInterval = int(input())

    if(TimeInterval > 0):
        schedule.every(TimeInterval).seconds.do(Display,Message)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Time interval should be greater than 0..")

if __name__ == "__main__":
    main()