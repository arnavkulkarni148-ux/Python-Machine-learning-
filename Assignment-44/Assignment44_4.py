import pandas as pd 

def main():

    # Q4

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

    print("Student who scored more than 85 in science are: ")
    print("-"*50)
    print(df[df['Science'] > 85])
    print("-"*50)


if __name__ == "__main__":
    main()