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