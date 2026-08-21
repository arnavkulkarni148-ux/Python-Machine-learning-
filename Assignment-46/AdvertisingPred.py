import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def AdvertisePred(Datapath):
    Border = "-"*60

    # ---------------------------------------------------------------
    # Step 1 : Get Data
    # ---------------------------------------------------------------

    df = pd.read_csv(Datapath)

    print(Border)
    print("Some entries from the dataset:")
    print(df.head())
    print(Border)

    print("Shape of the dataset:")
    print(df.shape)
    print(Border)

    print(f"Rows in the data:{df.shape[0]}, Columns in the data:{df.shape[1]}")
    print(Border)

    print("Column names from the data:")
    print(df.columns)
    print(Border)

    # ------------------------------------------------------------------
    # Step 2: Clean, prepare and manipulate data
    # ------------------------------------------------------------------

    print("Removing unwanted column..")

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(" Some entries after removing unwanted column")
    print(df.head())
    print(Border)

    print("Total null values from the dataset:")
    print(df.isnull().sum())
    print(Border)

    df.dropna(inplace = True)

    # Separeting indepnedent and dependent variable

    X = df[["TV","radio","newspaper"]]
    Y = df[["sales"]]

    # -----------------------------------------------------------------------
    # Step 3: Train Data
    # -----------------------------------------------------------------------

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)
    print("Model trained succesfully..")
    print(Border)

    # ----------------------------------------------------------------------------
    # Step 4: Test Data
    # ----------------------------------------------------------------------------

    Y_pred = model.predict(X_test)
    print("Model testing done succesfully..")
    print(Border)

    # ----------------------------------------------------------------------------
    # Step 5: Display predicted and actual values 
    # ----------------------------------------------------------------------------

    print("Showing actual values and predicted values")
    print("Showing first 5 entries:")

    print("Actual Answers:")
    print(Y_test[:5])

    print("Predicted Answers")
    print(Y_pred[:5])
    print(Border)

def main():
    AdvertisePred("Advertising (1).csv")
    
if __name__ == "__main__":
    main()