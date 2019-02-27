# a, b = map(int, input().split())
# print(a+b)

arr = input().split()
print(arr)

# 한 줄에 여러 개 입력 받는 경우, 그리고 입력 값이 숫자여야하는 경우

# input().split()의 인자, 리턴값 
# 그렇다면 input().split() 은 list 인가 ? ㅇㅇ list래 split() 함수가 string으로 리스트를 만들어 리스트를 반환
# a , b 처럼 ,로 선언하는건 어떤거지

# 데이터 타입 확인은 type()