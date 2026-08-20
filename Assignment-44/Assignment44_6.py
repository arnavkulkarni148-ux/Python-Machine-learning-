import pandas as pd 

def main():

    # Q6

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

    df_sort = df.sort_values(by='Total',ascending=False)
    print("-"*50)
    print(df_sort)
    print("-"*50)

if __name__ == "__main__":
    main()