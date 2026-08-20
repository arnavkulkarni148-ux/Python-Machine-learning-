import pandas as pd

def main():

    # Q2

    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }

    df = pd.DataFrame(data)   # Created dataframe of data

    print("-"*50)
    print("Descriptive statistics of data:")
    print(df.describe())
    print("-"*50)

if __name__ == "__main__":
    main()