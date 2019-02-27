from sys import stdin

# 기존 코드
# arr = int(stdin.readline().split())
# a = arr[0]
# b = arr[1]
# print(a)

# int()의 인자는 무조건 string이여야하는데 stdin.readline().split()이 arr 반환함 

a, b = map(int, input().split())
print(a-b)
