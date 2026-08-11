# ----------------------------------------------------------------------------------
# Importing require library 
# -----------------------------------------------------------------------------------

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

def main():

    Border = "-"*70
    # -------------------------------------------------------------------
    # Step 1: Dataset loading
    # -------------------------------------------------------------------

    print(Border)
    print("Dataset Loading")
    print(Border)

    StudentPerf = "student_performance_ml.csv"
    df = pd.read_csv(StudentPerf) # Dataset loading 
    print("Showing fisrt five entries from the dataset:") 
    print(df.head()) # Showing forst five entries from the dataset 

    print("Total rows in the dataset are:",df.shape[0])
    print("Total Columns in the dataset are:",df.shape[1])
    print("Column names in the dataset are:")
    print(list(df.columns))
    print(Border)

    # -------------------------------------------------------------------
    # Step 2: Data Analysis
    # -------------------------------------------------------------------

    print(Border)
    print("Data Analysis")
    print(Border)

    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']
    print("Shape of X:",X.shape)
    print("Shape of Y:",Y.shape)
    print("Dataset Information:")
    print(df.info())
    print(Border)

    # -------------------------------------------------------------------
    # Step 3: Data Visualisation
    # -------------------------------------------------------------------

    print(Border)
    print("Data Visulisation")
    print(Border)

    plt.scatter(
        df['StudyHours'],
        df['PreviousScore'],
        s = 100,
        marker="o",
        alpha= 0.8,
        edgecolors="black",
        linewidths=1

    )

    plt.title("Study Hours vs Previous Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.show()

    # -------------------------------------------------------------------
    # Step 4: Train-test-split
    # -------------------------------------------------------------------

    print(Border)
    print("Train-test-split")
    print(Border)

    # Splitting the data into training and testing
    X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)
    print("Training data size:",X_train.shape)
    print("Testing data size:",X_test.shape)
    print(Border)

    # -------------------------------------------------------------------
    # Step 5: Model Training
    # -------------------------------------------------------------------

    print(Border)
    print("Model Training")
    print(Border)

    model = DecisionTreeClassifier(max_depth=1) # Creating the model 

    model.fit(X_train,Y_train) # Training the data 
    print(Border)

    # -------------------------------------------------------------------
    # Step 6: Prediction
    # -------------------------------------------------------------------

    print(Border)
    print("Prediction")
    print(Border)

    Y_pred = model.predict(X_test) # Testing the data
    print("Expected answers:") 
    print(list(Y_test))

    print("Predicted answers:")
    print(Y_pred)
    print(Border)

    # -------------------------------------------------------------------
    # Step 7: Accuracy calculator
    # -------------------------------------------------------------------

    print(Border)
    print("Accuracy Calculator")
    print(Border)

    Train_pred = model.predict(X_train)

    # Training accuracy
    Trainingaccuracy = accuracy_score(Y_train,Train_pred)
    # Testing accuracy
    Testingaccuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy of training model is:",Trainingaccuracy*100)
    print("Accuracy of testing model is:",Testingaccuracy*100)
    print(Border)

    # -------------------------------------------------------------------
    # Step 8: Confusion Matrix 
    # -------------------------------------------------------------------

    print(Border)
    print("Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion Matrix is:")
    print(cm)

    # Display confusion matrix graphically

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    disp.plot()

    plt.title("Confusion Matrix")
    plt.show()
    print(Border)

    # ----------------------------------------------------------------------
    # TP, TN, FP, FN
    # ----------------------------------------------------------------------

    print("Confusion Matrix Explanation")

    print("True Postive(TP): Actual pass Predicted pass")
    print("True Negative(TP): Actual fail Predicted fail")
    print("False Postive(FP): Actual fail Predicted pass")
    print("False Negative(FN): Actual pass Predicted fail")

    # --------------------------------------------------------------------
    # Overfitting / Underfitting
    # --------------------------------------------------------------------

    print("\nModel Analysis:")

    if Trainingaccuracy > Testingaccuracy + 0.10:

        print("The model is overfitting.")

    elif Trainingaccuracy < 0.60 and Testingaccuracy < 0.60:

        print("The model is underfitting.")

    else:

        print("The model is performing reasonably well.")

    print(Border)

    # ------------------------------------------------------------------
    # Training three decision model
    # ------------------------------------------------------------------

    print("Training three models and checking there accuracy")
    # model 1: max_depth = 1
    model1 = DecisionTreeClassifier(max_depth=1)
    model1.fit(X_train,Y_train)
    pred1 = model1.predict(X_test)
    acc1 = accuracy_score(Y_test,pred1)

    # model 2: max_depth = 3
    model2 = DecisionTreeClassifier(max_depth=3)
    model2.fit(X_train,Y_train)
    pred2 = model2.predict(X_test)
    acc2 = accuracy_score(Y_test,pred2)

    # model 3: max_depth = None
    model3 = DecisionTreeClassifier()
    model3.fit(X_train,Y_train)
    pred3 = model3.predict(X_test)
    acc3 = accuracy_score(Y_test,pred3)

    # Testing accuracy
    print("Testing accuracy for max_depth = 1:",acc1*100)
    print("Testing accuracy for max_depth = 3:",acc2*100)
    print("Testing accuracy for max_depth = None:",acc3*100)

    # -----------------------------------------------------------------
    # Predicting Result for new students
    # -----------------------------------------------------------------
    print(Border)
    print("Predicting result for new students")
    print(Border)

    NewStudent = pd.DataFrame([{
        'StudyHours': 6,
        'Attendance': 85,
        'PreviousScore': 66,
        'AssignmentsCompleted': 7,
        'SleepHours': 7
    }])

    # Predicting using trained model
    NewResult = model.predict(NewStudent)
    print("Predicted Result:",NewResult[0])

    # -------------------------------------------------------------
    # Step 9: Final conclusion
    # --------------------------------------------------------------

    print(Border)
    print("Final conclusion")
    print(Border)

    print("Decision tree classifier was trained successfully..")
    print("We train the model with three different max_depth..")
    print("Model also predicted the result for new students")

if __name__ == "__main__":
    main()