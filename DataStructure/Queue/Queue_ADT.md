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

- Queue 구조 사진 

### Aplications 

- Queue는 어떤 자원을 공유해야하는 상황에서 한번에 하나씩만 요청을 처리할 수 있을 때 사용된다. 제일 먼저 들어온 요청을 제일 먼저 처리해야 한다. 
- 네트워크에 연결되어 있는 프린터는 문서를 처리 할 때 Queue 로 동작되는데 프린터는 한번에 하나의 문서만 프린트 할 수 있다. 만약 프린터가 문서를 출력하고 있을 때 다른 문서의 출력 요청이 온다면 차례대로 queue에 쌓이면서 출력 순서를 정한다. 
- 컴퓨터 안의 processor 또한 공유 되어야 하는 자원이다. processor는 한번에 하나의 프로그램 만 처리할 수 있다. 

## Implemations of Queue 
 Queue의  Enqueue, Dequeue, 첫번째 엘리먼트 값 확인하는 동작들은 Queue에 엘리먼트가 몇개가 있던지 간에 상관없이 constant time or O(1)으로 동작할 수 있어야한다. 

 Queue는 1) Array 2) Linked Listsn두가지 형태로 구현이 가능하다. 

### 1) List Implementation

파이썬에서 리스트로 스택을 구현하기는 쉽다. 한쪽 end에서만 삽입, 삭제가 이루어지기 때
문에 O(1)으로 가능하다. 

```
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop() # 3

```
하지만 queue는 양쪽 엔드에서 데이터가 들어오고 (Enqueue) 나갈 수 있어야 한다. (Dequeue)
list로 구현한다면 

```
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.pop(0) # 1
queue.pop(0) # 2
queue.pop(0) # 3
```
하지만 리스트의 첫번쨰 인덱스에서 값이 삭제된다면 리스트에 있는 모든 값들이 한칸 씩 앞으로 당겨져야 하기 때문에 결국 제일 앞의 값을 꺼내는데는 리스트의 크기만큼 시간이 소요된다 O(N)

queue를 구현하기 위해서 파이썬에서는 양 쪽 end에서 append와 pop이 빠르도록 만들어놨다.

```
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
queue.popleft()
'Eric'
queue.popleft()
'John'
queue
deque(['Michael','Terry', 'Graham'])

```
변수 front, tail 을 지정해서 만드는 방법은 ? 

### 2) Linked list Implementation 