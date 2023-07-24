def solution(x, n):
    
    answer = []
    
    for y in range(0, n) :
        answer.append(x*(y + 1))
    
    return answer