import pandas as pd

def main():
    # Q3

    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }

    df = pd.DataFrame(data)
    df['Total'] = df['Math'] + df['Science'] + df['English']

    df['Gender'] = ['Male','Male','Female']
    df = pd.get_dummies(df,columns=['Gender'],dtype=int)

    gender_data = {
        'Name': ['Amit', 'Sagar', 'Puja'],
        'Gender': ['Male', 'Male', 'Female']
    }

    gender_df = pd.DataFrame(gender_data)
    print(gender_df)

    group_df = pd.merge(
        df,
        gender_df,on='Name'
    )

    avg_marks = group_df.groupby('Gender')[
        ['Math','Science','English']
    ].mean()

    print("-"*50)
    print(avg_marks)
    print("-"*50)

if __name__ == "__main__":
    main()