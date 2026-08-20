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

    df['Gender'] = ['Male','Male','Female']
    df = pd.get_dummies(df,columns=['Gender'],dtype=int)

    df['Status'] = df['Total'].apply(
    lambda x: 'Pass' if x >= 250 else 'Fail'

    )
    df.to_csv('final_student_data.csv', index=False)
    print("-"*50)
    print("DataFrame exported successfully to final_student_data.csv")
    print("-"*50)

if __name__ == "__main__":
    main()