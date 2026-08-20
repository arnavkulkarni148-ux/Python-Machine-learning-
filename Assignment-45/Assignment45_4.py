import pandas as pd
import matplotlib.pyplot as plt


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

    df['Gender'] = ['Male','Male','Female']
    df = pd.get_dummies(df,columns=['Gender'],dtype=int)

    sagar = df[df['Name'] == 'Sagar'].iloc[0]

    subjects = ['Math', 'Science', 'English']
    marks = [sagar['Math'], sagar['Science'], sagar['English']]

    plt.figure(figsize=(6, 6))

    plt.pie(
        marks,
        labels=subjects,
        autopct='%1.1f%%'
    )

    plt.title("Sagar's Subject Marks")

    plt.show()




if __name__ == "__main__":
    main()