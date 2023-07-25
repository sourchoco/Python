def solution(n):
    
    arr = []
    
    for x in str(n) :
        arr.append(int(x))
    
    answer = arr[-1:-n:-1]
    
    return answer