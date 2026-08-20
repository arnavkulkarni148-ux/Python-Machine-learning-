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
    df_sort = df.sort_values(by='Total',ascending=False)

    Amit = df[df['Name'] == 'Amit'].iloc[0]

    subjects = ['Math','Science','English']
    marks = [Amit['Math'], Amit['Science'], Amit['English']]

    plt.figure(figsize=(7,5))

    plt.plot(subjects,marks,marker = 'o')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit's Marks across all subjects")
    plt.grid(True)
    plt.show() 

if __name__ == "__main__":
    main()