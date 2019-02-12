# 목표 시간 11시 
from sys import stdin

stack = []
for x in range(int(stdin.readline())):
    arr = stdin.readline().split()
    if arr[0] == "pop":
        if stack: print(stack.pop())
        else :print(-1)
       
    elif arr[0] == "push":
        stack.append(arr[1])
        
    elif arr[0]== "top":
        if stack: print(stack[-1])
        else: print(-1)
        
    
    elif arr[0]=="size":
        if stack: print(len(stack))
        else: print(0)
    elif arr[0] == "empty":
        if stack: print(0)
        else: print(1)
    else:
        pass
