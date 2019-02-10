[프로그래머스 코딩테스트 연습 > 스택/큐 > 프린터](https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3)

정확도 10점의 코드(+ 런타임 에러), 뭐가 문제였지 

```py

    maxNum = max(priorities)
    temp = location
    
    if(priorities[temp] == maxNum):
        return 1

    while True:
        if(temp == 0 and priorities[0] == maxNum):
            return answer + 1
        else:
            v = priorities[0]
            if(v == maxNum):
                priorities.pop()
                answer = answer +1
                maxNum = max(priorities)
                temp = (temp - 1 + len(priorities))% len(priorities)
                continue
            priorities.pop()
            priorities.append(v)
            temp = (temp - 1 + len(priorities))% len(priorities)

```

접근 방법은 맞았지만 조건을 세세하게 나누는 부분에서 부족하고, 파이썬 list 문법에도 익숙해지는 시간이 필요하다. 
```py

    maxNum = max(priorities)
    answer = 0
  
    while True:
        popValue = priorities.pop()
        if popValue == maxNum:
            answer += 1 ## max가 pop 될때만 진짜로 출력되는 것이니까 순서 카운트
            if(location == 0):
                break
            else:
                location -= 1 # maxNum 이 다른 위치에 있는 경우
            maxNum = max(priorities)
            
        else:
           priorities.append(popValue)
           if(location == 0): # location 이 0 인데 max가 아니면 제일 뒤로
                location = len(priorities)-1
           else: 
                location -= 1

    return answer
```