import pandas as pd 
import matplotlib.pyplot as plt

def main():

    # Q7

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

    plt.figure(figsize=(7,5))
    plt.bar(df_sort['Name'],df_sort['Total'])
    plt.xlabel("Name of student")
    plt.ylabel("Total Marks")
    plt.title("Student Name vs Total")
    plt.show()


if __name__ == "__main__":
    main()