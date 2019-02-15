자료 구조의 핵심 기능은 아래와 같다. 
1) 삽입 (insert)
2) 삭제 (remove)
3) 검색 (search)

### Array에서 기능들의 시간 복잡도 
1) 삽입 (insert) : O(1) 
2) 삭제 (remove) : O(n) // 최악 : 삭제하면 한칸씩 엘리먼트 이동
3) 검색 (search) : O(n) // 최악 : 엘리먼트 모두 확인해야하는 경우

### Linked list에서 기능들의 시간 복잡도 
1) 삽입 (insert) : O(1) // head에 값 추가하는 경우
2) 삭제 (remove) : O(n) // 최악 : 마지막 요소 삭제하기 위해서 모든 노드 들리기
3) 검색 (search) : O(n) // 최악 : 엘리먼트 모두 확인해야하는 경우

** But !!!!! 검색에 있어서 n 번의 값 비교는 최악임** 

Binary Search Tree를 이용하면 1),2),3) 을 O(logN)으로 구현 가능
최악의 경우 O(n)이 걸리지만, balanced BST를 이용하여 최악의 경우 걸러내겠음 
> balanced BST : 왼쪽 서브트리의 높이와 오른쪽 서브트리의 높이가 1 이상 차이나지 않는 이진 탐색 트리 구조 

## Binary Search Tree 이진 탐색 트리란 머냐

이진 트리안의 모든 노드들에서 왼쪽 서브트리는 루트 값보다 항상 값이 작거나 같고 오른쪽 서브트리는 항상 큰 이진 트리 구조

1) Search 

a = [8, 10, 12, 15, 17, 20 , 25, null, null]
Search(10)
- search space는 start 와 end 포인트가 가리키고 있는 공간 : n
- search space의 중간 값과 먼저 비교 
- 찾고자 하는 값이 작으면 왼쪽으로 이동, 크면 오른쪽으로 이동
- 중간 값 15보다 10이 작기 때문에 space 는 [8, 10 ,12] 로 반으로 줄게됨 : n/2
- space가 n/4, n/8 ... 1로 줄어듬

### Worst Case
unbalanced binary search tree 의 search space는 
- n , n-1, n-2 , ... 1
- 1), 2), 3) 이 O(n)

