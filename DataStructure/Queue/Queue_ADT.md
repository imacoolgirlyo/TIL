## Queue ADT(Abstract Data Structure)

> Abstract Data Type 이란 자료 구조의 특징과 기능들을 정리한 것으로 어떻게 구현할 것인가의 내용은 설명하지 않는다. 

### Logical View 

- First-In-First-Out(FIFO) 
- 실생활에서 Queue 는 줄 서는 것과 같은 개념 (먼저 줄 선 놈이 먼저 들어감)
- 무조건 Rear (or tail) 에서는 Data 가 삽입되고 Front(or head) 에서는 Data가 빠지는 구조 

** A list or Collection with the restriction that insertion can be performed at one end(rear) and deletion can be performed at other end(front) **

### Operations
(1) **Enqueue(x) or Push(x)** : rear 에 엘리먼트 삽입 
(2) ** Dequeue() or Pop() ** : front 에 있는 엘리먼트 리턴 후 삭제 
(3) **  front() or Peek() ** : front에 있는 엘리먼트 리턴
(4) IsEmpty() 


> 대부분 자료구조는 직접 구현하지 않고 language libraies에 미리 구현되어있는 자료 구조를 사용한다. 언어에 따라 rear에 엘리먼트를 삽입하는 메소드가 Enqueue가 될수도 있고 Push가 될 수  있다. 

위의 Queue의 (1) ~ (4) 까지의 기능들은 무조건 시간 복잡도가 Constant time or O(1) 이 되어야 한다. 즉 엘리먼트를 넣고 빼고 젤 앞에 값 확인하고 하는 동작들이 O(1)로 동작해야한다. 

- Stack 의 경우 엘리먼트를 넣고(push) 빼는(pop) 동작이 모두 한 군데에서 이루어졌다면 Queue의 경우 한 쪽면(rear)에서는 무조건 Enqueue, 다른 한쪽(front)에서는 무조건 Dequeue만 이루어진다. 같은 곳 일 수 없음!

- Stack 구조 사진 
