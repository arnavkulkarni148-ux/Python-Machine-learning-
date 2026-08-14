import math

def EucDistance(P1, P2):
    ans = math.sqrt((P1['S'] - P2['S']) ** 2 + (P1['A'] - P2['A']) ** 2)
    return ans

def KNN_Classifier(S, A, K=3):
    border = "-" * 50
    data = [
        {'S': 2, 'A': 60, 'Result': 'Fail'},
        {'S': 5, 'A': 80, 'Result': 'Pass'},
        {'S': 6, 'A': 85, 'Result': 'Pass'},
        {'S': 1, 'A': 50, 'Result': 'Fail'}
    ]
        
    # Input point dictionary
    new_point = {'S': S, 'A': A}
    
    # Calculate distance from test point to all points in the dataset
    distances = []
    for row in data:
        dist = EucDistance(new_point, row)
        distances.append((dist, row['Result']))
        
    # Sort by distance in ascending order
    distances.sort(key=lambda x: x[0])
    
    # Get the K nearest neighbors
    neighbors = distances[:K]
    
    # Count votes for Pass and Fail
    pass_count = 0
    fail_count = 0
    for _, result in neighbors:
        if result == 'Pass':
            pass_count += 1
        else:
            fail_count += 1
            
    # Predict the class with the majority vote
    if pass_count > fail_count:
        predicted_result = 'Pass'
    else:
        predicted_result = 'Fail'
        
    print(f"Predicted Result: {predicted_result}")
    return predicted_result

def main():
    study_hours = int(input("Enter Study Hours: "))
    attendance = int(input("Enter Attendance: "))

    result = KNN_Classifier(study_hours, attendance)

if __name__ == "__main__":
    main()