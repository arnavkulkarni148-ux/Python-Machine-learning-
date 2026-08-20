import pandas as pd

def main():
    # Q1

    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }

    df = pd.DataFrame(data)
    df['Total'] = df['Math'] + df['Science'] + df['English']
    print("Before Normalizeing")
    print("-"*50)
    print(df)
    print("-"*50)

    df['Math_Normalized'] = (
        (df['Math'] -df['Math'].min()) /
        (df['Math'].max() - df['Math'].min())
    ) 

    print("After normalizeing")
    print("-"*50)
    print(df[['Name','Math','Math_Normalized']])
    print("-"*50)


if __name__ == "__main__":
    main()