## 🖊 Pointers and dynamic memory 

어플리케이션의 메모리는 크게 
- Heap
- Stack
- Static / Global
- Code(Text)

로 나뉜다. 

- Code(Text)는 Instructions
- Static / Global : global 변수가 저장되는 곳
- **Stack**은 함수 호출과 모든 지역 변수에 대한 정보들이 저장되는 곳이다. pointer와 call by reference 강의는 [여기](https://www.youtube.com/watch?v=LW8Rfh6TzGg&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_&index=5)
- 지역 변수는 오직 함수 내에서만 존재하기 때문에 함수 실행되는 동안에만 살아있다. 

```c
#include<stdio.h>
int total;
int Square(int x)
{
    return x*x;
}
int SquareOfSum(int x, int y)
{
    int z = Square(x+y);
    return z;
}
int main(){
    int a = 4, b = 8;
    total = SquareOfSum(a,b);
    printf("output = %d", total);
}
```