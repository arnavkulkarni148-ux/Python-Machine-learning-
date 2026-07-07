# Module

def ChkPrime(No):
    if No < 2:
        return False
    if No == 2 :
        return True
    for i in range(2,No):
        if No % i == 0:
            return False
    return True
