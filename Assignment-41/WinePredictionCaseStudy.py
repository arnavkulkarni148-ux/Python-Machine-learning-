import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

def WinePrediction(datapath):
    Border = "-"*50

    # Step 1:Dataset loading

    print(Border)
    df = pd.read_csv(datapath)
    print("Some entires form the dataset:")
    print(df.head())
    print("Number of rows in the dataset:",df.shape[0])
    print("Number of columns in the dataset:",df.shape[1])
    print("Columns in the dataset are:")
    print(df.columns)
    print(Border)

    # Step 2: Clean the dataset
    print(Border)
    df.dropna(inplace=True) # Delete the null values from the dataset
    print("Dataset Cleaning complete")
    print(Border)

    # Step 3: Train the Data
    X = df.drop(columns=['Class'])
    Y = df['Class']

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
    print("X_train shape:",X_train.shape)
    print("X_test shape:",X_test.shape)
    print(Border)

    model = DecisionTreeClassifier(max_depth=5)

    model.fit(X_train,Y_train)

    print("Training of the dataset is complete..")
    print(Border)

    # Step 4: Test the dataset

    Y_pred = model.predict(X_test)
    print("Testing of the dataset is complete..")
    print(Border)

    # Step 5: Accuracy check

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy of the dataset is:",accuracy*100,"%")

def main():
    WinePrediction("WinePredictor.csv")

if __name__ == "__main__":
    main()