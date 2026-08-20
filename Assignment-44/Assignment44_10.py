import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

def main():

    # Q9

    data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
    }

    df = pd.DataFrame(data)

    df['Total'] = df['Math'] + df['Science'] + df['English']
    df_sort = df.sort_values(by='Total',ascending=False)

    print("Before droping English column")
    print("-"*50)
    print(df)
    print("-"*50)


    df_drop = df.drop('English',axis=1)
    print("After droping English columns")
    print("-"*50)
    print(df_drop)
    print("-"*50)

if __name__ == "__main__":
    main()