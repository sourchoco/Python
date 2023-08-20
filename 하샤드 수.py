def solution(x):
    
    denom = 0
    
    for y in list(str(x)) :
        denom += int(y)
        
    return x%denom==0