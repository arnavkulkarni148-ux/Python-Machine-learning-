import pandas as pd 

def main():

    # Q5

    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
    }

    df = pd.DataFrame(data)
    df['Total'] = df['Math'] + df['Science'] + df['English']
    print("-"*50)
    print(df)
    print("-"*50)

    df['Name'] = df["Name"].replace('Pooja','Puja')
    print("After Name changing")
    print("-"*50)
    print(df)
    print("-"*50)

if __name__ == "__main__":
    main()