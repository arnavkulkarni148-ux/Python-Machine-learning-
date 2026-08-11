import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("*"*75)
    print("\n")
    # Q1 ->
    # Loading the dataset 
    StudentPerf = "student_performance_ml.csv"
    df = pd.read_csv(StudentPerf)  # csv file loaded with the help of pandas
    print(df.head()) # Show the first five records of dataset
    print(df.tail()) # show the last five records of dataset

    # Total numbers of rows & coulmns
    print("Total numbers of rows and columns are:",df.shape) # using shape function to find numbers of rows & columns

    # List of coulumn names
    print("Column names are:")
    print(df.columns) # using columns to find column names

    # Data type of each column
    print("Datatypes of column are:")
    print(df.dtypes) # dtype display's the datatype of column
    print("\n")
    print("*"*75)

    # Q2 ->
    # Display total number of students in the dataset 
    print("*"*75)
    print("\n")
    print("Total numbers of studnets in the dataset are:",len(df)) # we can also do like this df.shape[0]

    # Count how many students passed and failed
    pass_count = (df['FinalResult'] == 1).sum() # Count the pass Student
    fail_count = (df["FinalResult"] == 0).sum() # count fail studnet
    print("Pass Student:",pass_count)
    print("Fail Student:",fail_count)
    print("\n")

    # Finding the average / maximum / minimum of columns 
    average_StudyHours = df['StudyHours'].mean()
    average_attendence = df['Attendance'].mean()
    max_PrevScore = df['PreviousScore'].max()
    min_SleepHrs = df['SleepHours'].min()

    print("Average Study Hours of student:",average_StudyHours)
    print("Average attendence of student:",average_attendence)
    print("Maximum Previous score of student:",max_PrevScore)
    print("Minimum Sleep Hours of student:",min_SleepHrs)

    #Q4 ->
    print(df['FinalResult'].value_counts())
    pass_percentage = (pass_count/len(df)) * 100
    print("Pass Percentage:",pass_percentage)
    fail_percentage = (fail_count/len(df)) * 100
    print("Fail Percentage:",fail_percentage)

    # Q5
    print("\nObservations:")    
    print("1. Students who study more hours generally have a higher chance of passing.")
    print("2. Students with better attendance tend to achieve better final results.")
    print("3. Lower study hours and attendance are associated with a higher chance of failure.")
    print("4. Both StudyHours and Attendance positively influence FinalResult.")

    #Q6 ->
    # Plotting histogram of StudyHours
    df['StudyHours'].plot(kind='hist', bins=10, edgecolor='black', color='skyblue')
    plt.title('Distribution of Student Study Hours')
    plt.xlabel('StudyHours')
    plt.ylabel('Frequency')
    plt.show()

    print("\nExplanation:")
    print("The histogram shows how StudyHours are distributed among students.")
    print("The tallest bars represent the range where most students study.")
    print("It helps identify whether students generally study fewer or more hours.")

    #Q7 ->
    # Scatter plot -> StudyHours vs PreviousScore
    df.plot(kind='scatter', x='StudyHours', y='PreviousScore', color='blue', alpha=0.7)

    # Add title and labels
    plt.title('StudyHours vs PreviousScore')
    plt.xlabel('Study Hours')
    plt.ylabel('Previous Score')
    plt.show()

    print("\nExplanation:")
    print("Each point represents one student.")
    print("The plot helps observe the relationship between StudyHours and PreviousScore.")

        # Q8 ->
    # Box Plot -> Attendance
    data = df['Attendance']
    plt.boxplot(data)
    plt.title("Box plot of Attendance")
    plt.ylabel("Attendance")
    plt.show()

    # Identify outliers using IQR method
    Q1 = df['Attendance'].quantile(0.25)
    Q3 = df['Attendance'].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[(df['Attendance'] < lower_limit) |
                (df['Attendance'] > upper_limit)]

    print("Attendance Q1:", Q1)
    print("Attendance Q3:", Q3)
    print("Attendance IQR:", IQR)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)

    if len(outliers) > 0:
        print("Outliers are present in Attendance:")
        print(outliers['Attendance'])
    else:
        print("No outliers are present in Attendance.")


    # Q9 ->
    # Plot showing relationship between AssignmentsCompleted and FinalResult

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df['AssignmentsCompleted'],
        df['FinalResult'],
        alpha=0.7
    )

    plt.title("Assignments Completed vs Final Result")
    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result (0 = Fail, 1 = Pass)")
    plt.yticks([0, 1], ['Fail', 'Pass'])
    plt.grid(True)

    plt.show()

    # Observation for Q9
    print("\nObservation:")
    print("The plot shows the relationship between the number of assignments completed")
    print("and the final result. Students who complete more assignments generally")
    print("tend to have a better chance of passing, although completing assignments")
    print("does not guarantee success.")


    # Q10 ->
    # Plot SleepHours against FinalResult

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df['SleepHours'],
        df['FinalResult'],
        alpha=0.7
    )

    plt.title("Sleep Hours vs Final Result")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result (0 = Fail, 1 = Pass)")
    plt.yticks([0, 1], ['Fail', 'Pass'])
    plt.grid(True)

    plt.show()

    # Observation for Q10
    print("\nObservation:")
    print("The plot shows the relationship between SleepHours and FinalResult.")
    print("Sleeping more does not guarantee success. The final result is likely")
    print("affected by several factors such as study hours, attendance, previous")
    print("score, and assignments completed.")

if __name__ == "__main__":
    main()
