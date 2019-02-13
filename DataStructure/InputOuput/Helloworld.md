## 백준 입출력 문제 및 파이썬 문법

입력 : 첫째 줄에 A, B가 주어짐 
출력 : 첫째 줄에 A+B 를 출력 

```py
a, b = map(int, input().split())
print(a+b)
```

### map(function, iterable,...)
- iterable 한 아이템 모두에 function을 적용하고 결과로 리스트를 반환하는 일을 함
- 첫번째 인자에는 적용할 메소드, 두번째는 적용할 객체
> 여기서 **iterable** 하다는 뜻은 한번에 객체 맴버 하나씩 리턴할 수 있는 객체 즉 list, str, tuple 같은 놈들이 iterable 한 객체이다. 반복 가능한 이라는 뜻

- int는 여기서 메소드임 인자를 정수로 바꿔주는 역할을 하지

## str.split()은 string을 공백으로 나눠주고 리스트 반환

> 응용
첫 줄에 입력 받고, 두번째 줄부터 N개의 줄에는 명령이 하나씩 주어짐

### 명령창에 입력 받는 방법 
(1) input() 
(2) stdin.readline()

둘다 string으로 받기 때문에 숫자로 변환하기 위해서 int() 함수를 이용하여 변환 
```py
A = int(input())
a, b = map(int , input().split) # input 여러개를 받을 경우 쪼개서 list로 저장된 것을 int 적용 

a = int(stdin.readline())
arr = stdin.readline().split # 들어오는 만큼 쪼개서 arr에 저장
```
