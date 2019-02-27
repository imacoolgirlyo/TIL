## 백준 입출력 문제 및 파이썬 문법

### map(function, iterable,...)
```py
map(function_to_apply, list_of_inputs)
```
- 리스트(혹은 str, tuple)에 있는 아이템 하나 하나에 function을 적용한다 결과로 리스트를 반환하는 일을 함
- 결과로 새로운 리스트를 반환한다는 것을 잊지마셈..
> 여기서 **iterable** 하다는 뜻은 한번에 객체 맴버 하나씩 리턴할 수 있는 객체 즉 list, str, tuple 같은 놈들이 iterable 한 객체이다. 반복 가능한 이라는 뜻

- int는 여기서 메소드임 인자를 정수로 바꿔주는 역할을 하지

## str.split()
string을 공백으로 나눠주고 쪼갠거 리스트 만들어서 **리스트 반환**
```py
txt = "Heavy California"
x = txt.split()
print(x)

# ['Heavy' , 'California']
```

## input().split()
cmd line에 인풋 받고 여러 개면 split()으로 쪼개서 쪼갠거 list 반환
```py
arr = input().split()
print(arr)

# 입력 : 3 4  
# 출력 : ['3', '4']
```

### 명령창에 입력 받는 방법 
(1) input() 
(2) stdin.readline()

둘다 string으로 받기 때문에 숫자로 변환하기 위해서 int() 함수를 이용하여 변환 
```py
A = int(input())
a, b = map(int , input().split()) # input 여러개를 받을 경우 쪼개서 list로 저장된 것을 int 적용 

a = int(stdin.readline())
arr = stdin.readline().split() # 들어오는 만큼 쪼개서 arr에 저장
```

## [a, b = [2, 3]](https://stackoverflow.com/questions/31426095/assign-multiple-values-of-a-list)

python의 리스트 값으로 여러 개 변수 설정 
```py
a,b,c,d = [1,2,3,4]
>>> a
1
>>> b
2
>>> c
3
>>> d
4
```

python3에서는 이 기능이 더 확대됨 리스트 length 보다 변수의 숫자가 적을 때 * operator 사용 
```py
a,b,*c = [1,2,3,4]
>>> a
1
>>> b
2
>>> c
[3,4]
```