import pandas as pd
import matplotlib.pyplot as plt


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

    df['Gender'] = ['Male','Male','Female']
    df = pd.get_dummies(df,columns=['Gender'],dtype=int)

    df['Status'] = df['Total'].apply(
    lambda x: 'Pass' if x >= 250 else 'Fail'

    )

    print("-"*50)
    print(df[['Name','Total','Status']])
    print("-"*50)
    passed_stud = (df['Status']== 'Pass').sum()
    print("-"*50)
    print("Passed Students:",passed_stud)
    print("-"*50)





if __name__ == "__main__":
    main()