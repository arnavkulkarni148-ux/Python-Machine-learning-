import pandas as pd

def main():

    # Q1 

    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }

    df = pd.DataFrame(data)   # Created dataframe of data

    print("-"*50)
    print("Shape of the data:")
    print(df.shape)   # give shape of the dataset
    print("-"*50)

    print("Columns are:")
    print(df.columns)   # show columns from the dataset
    print("-"*50)

    print("Datatype of the data")
    print(df.dtypes)   # give datatpe of the data 
    print("-"*50)

if __name__ == "__main__":
    main()