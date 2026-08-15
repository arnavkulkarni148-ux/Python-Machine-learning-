import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def MarvellousPlayPredictor(datapath):
    # Step 1: Get Data
    df = pd.read_csv(datapath)
    print("-" * 50)
    print("Some entries from the data:")
    print("-" * 50)
    print(df.head())
    print("-" * 50)

    df.dropna(inplace=True)  # Deleting empty data if exists

    print("Total rows from the dataset:", df.shape[0])
    print("Total columns from the dataset:", df.shape[1])
    print("-" * 50)

    # Step 2: Clean, prepare and manipulate
    WeatherEncoder = LabelEncoder()
    df['Wether'] = WeatherEncoder.fit_transform(df['Wether'])

    TemperatureEncoder = LabelEncoder()
    df['Temperature'] = TemperatureEncoder.fit_transform(df['Temperature'])

    print("Data after encoding")
    print("-" * 50)
    print(df.head())
    print("-" * 50)

    X = df[['Wether', 'Temperature']]
    Y = df['Play']

    # Step 3: Train Data
    Model = KNeighborsClassifier(n_neighbors=3)
    Model.fit(X, Y)
    print("Model Train successfully")
    print("-" * 50)

    # Step 4: Test Data
    print("Enter Weather and Temperature for prediction..")

    print("Weather options:", list(WeatherEncoder.classes_))
    weather = input("Enter weather: ")

    print("Temperature options:", list(TemperatureEncoder.classes_))
    temp = input("Enter temperature: ")

    WeatherValue = WeatherEncoder.transform([weather])[0]
    TempValue = TemperatureEncoder.transform([temp])[0]

    TestData = [[WeatherValue, TempValue]]

    Prediction = Model.predict(TestData)

    print("Prediction:", Prediction)
    print("-" * 50)

def CheckAccuracy(datapath):
    # Load dataset
    df = pd.read_csv(datapath)

    # Remove empty data
    df.dropna(inplace=True)

    # Encode Weather 
    WeatherEncoder = LabelEncoder()
    df["Wether"] = WeatherEncoder.fit_transform(df["Wether"])

    # Encode Temperature
    TemperatureEncoder = LabelEncoder()
    df["Temperature"] = TemperatureEncoder.fit_transform(df["Temperature"])

    # Input and Output
    X = df[["Wether", "Temperature"]]
    Y = df["Play"]

    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.5, random_state=42
    )

    print("\nAccuracy for different values of K")
    print("-" * 50)

    # Check accuracy for different K values
    for K in range(1, 11):
        Model = KNeighborsClassifier(n_neighbors=K)

        # Train model
        Model.fit(X_train, Y_train)

        # Predict testing data
        YPrediction = Model.predict(X_test)

        # Calculate accuracy
        Accuracy = accuracy_score(Y_test, YPrediction)

        print("K =", K, "Accuracy =", Accuracy * 100, "%")

def main():
    datapath = "MarvellousInfosystems_PlayPredictor.csv"
    MarvellousPlayPredictor(datapath)
    CheckAccuracy(datapath)

if __name__ == "__main__":
    main()