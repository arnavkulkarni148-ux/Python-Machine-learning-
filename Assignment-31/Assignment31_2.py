import schedule
import time

def Display(Message):
    print(Message)

def main():
    print("Enter a message : ")
    Message = input()

    schedule.every(5).seconds.do(Display,Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()