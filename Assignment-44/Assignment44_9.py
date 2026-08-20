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

    data2 = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[np.nan,76,88],
        'Science':[91,np.nan,85]
    }

    df2 = pd.DataFrame(data2)
    print("Before filling missing values")
    print("-"*50)
    print(df2)
    print("-"*50)

    # Filling missing values with column mean
    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    
    df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

    print("Aftet filling missing values")
    print("-"*50)
    print(df2)
    print("-"*50)



if __name__ == "__main__":
    main()