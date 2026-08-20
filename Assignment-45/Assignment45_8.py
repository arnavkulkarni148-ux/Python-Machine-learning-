import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Q8

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

    plt.figure(figsize=(7, 5))

    plt.hist(df['Math'], bins=5, edgecolor='black')

    plt.xlabel('Math Marks')
    plt.ylabel('Number of Students')
    plt.title('Distribution of Math Marks')

    plt.show()






if __name__ == "__main__":
    main()