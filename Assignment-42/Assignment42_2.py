import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2 )
    return Ans

def KNN_Classifier(x,y,K = 3):

    border = "-"*50

    data = [
        {'Point':'A','X':1,'Y':2,'label':'Red'},
        {'Point':'B','X':2,'Y':3,'label':'Red'},
        {'Point':'C','X':3,'Y':1,'label':'Blue'},
        {'Point':'D','X':6,'Y':5,'label':'Blue'},
    ]

    print(border)

    print(border)
    new_point = {'X':x,'Y':y}

    # Calculating distance
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    sorted_data = sorted(data,key = lambda item: item['distance'])

    print("Nearest Neighbors:")
    for d in sorted_data:
        print(d)
    print(border)

    k_nearest = sorted_data[:K]

    red = sum(1 for i in k_nearest if i['label'] == 'Red')
    blue = sum(1 for i in k_nearest if i['label'] =='Blue')

    # print(f"Red Votes ={red},Blue votes = {blue}")
    if red > blue:
        return "Red"
    else:
        return "Blue"

def main():
    
    x = int(input("Enter X cordinate:"))
    y = int(input("Enter Y Cordinate:"))

    print("Prediction Result:")
    ret1 = KNN_Classifier(x,y,1)
    print("K = 1 Result:",ret1)
    ret2 = KNN_Classifier(x,y,3)
    print("K = 3 Result:",ret2)
    ret3 = KNN_Classifier(x,y,5)
    print("K = 5 Result:",ret3)
   
if __name__ == "__main__":
    main()