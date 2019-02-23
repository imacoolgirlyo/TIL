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

1. 프로그램이 실행되면, 제일 먼저 stack에 main 함수가 실행되게 된다. Global 에는 total 변수가 저장된다. 
2. main() 함수가 실행되면서 지역 변수 a와 b가 같은 stack-frame에 저장된다. 
3. SquareOfSum 함수가 호출되면서 스택에 push 되고 마찬가지로 지역 변수 x, y, z가 저장된다.
4. Square 함수가 호출되어 스택에 push 된 후 마찬가지로 변수 x가 같은 스택 프레임에 있게된다.

스택에 가장 위에 있는 함수가 실행될때는 나머지 함수들은 자기 차례가 올때까지 실행이 정지된다. 제일 위의 함수가 결과를 리턴하여 종료되면 스택에서 pop 된다. 

여기서 total 전역 변수는 어디 함수에도 속해있지 않기 때문에 전역변수로 Global에 저장되고 어디에서든지 접근할 수 있다. 

5. SquareSum(a,b)의 결과 값을 total 에 저장 하고 printf 함수가 stack push 되어 실행된다. 
6. main 함수의 실행이 끝나면 스택에서 제거되고 마찬가지로 Global 에서도 전역변수 total이 제거된다. 

+ 자바스크립트 엔진도 콜 스택이란 스택을 가지고 있는데 이 곳에서 실제로 호출된 함수가 쌓이고 값을 리턴하면서 스택에서 빠진다. 똑같은 동작 !