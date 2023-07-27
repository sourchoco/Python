def solution(s):
    try : answer = int(s)
    except : answer = -int(s[1:len(s)])
    return answer