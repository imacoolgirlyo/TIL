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

### Operations (추가, 삽입, 검색)

```py
class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def setRoot(self, val):
        self.root = Node(val)
```


1) Retrieve / find

a = [8, 10, 12, 15, 17, 20 , 25, null, null]
retrieve(10)
- search space는 start 와 end 포인트가 가리키고 있는 공간 : n
- search space의 중간 값과 먼저 비교 
- 찾고자 하는 값이 작으면 왼쪽으로 이동, 크면 오른쪽으로 이동
- 중간 값 15보다 10이 작기 때문에 space 는 [8, 10 ,12] 로 반으로 줄게됨 : n/2
- space가 n/4, n/8 ... 1로 줄어듬

이번엔 4를 탐색해보면 , 제일 처음 중간 값 15, 10,8 비교 후 원하는 값을 찾지 못했음으로 '값을 찾지 못했다'고 반환 후 탐색 종료 한다. 

이진탐색트리의 탐색 연산에 소요되는 계산복잡성은 트리의 높이 h 에 따라 결정된다. 
높이 h는 꼭대기 루트 노드 ~ 마지막 자식이 없는 입새 노드 까지의 '엣지' 수의 최대값이다. 

```py
def find(self, val):
    if(self.findNode(self.root ,val) is False):
        return False
    else:
        return True

def findNode(self, currentNode ,val):
    if(currentNode is None):
        return False
    elif(val == currentNode.val):
        return currentNode
    elif(val < currentNode.val):
        return self.findNode(currentNode.leftChild , val)
    else:
        return self.findNode(currnetNode.rightChild , val)
```

### Worst Case
unbalanced binary search tree 의 search space는 
- n , n-1, n-2 , ... 1
- 1), 2), 3) 이 O(n)

2) Insert
값을 이진 탐색 트리에 추가하는 연산을 살펴보자. 삽입 연산은 반드시 잎새노드에서 이루어지게 된다. 
이진탐색트리의 삽입 연산에 소요되는 계산복잡성은 탐색 연산 처럼 트리의 높이가 h 일때 O(h)이다. 값을 삽입할 위치를 찾기 위해서 최대 h번 비교를 해야하기 때문이다. 

```py
def insert(self, val):
    if(self.root is None): # 트리에 아무것도 없을때
        self.setRoot(val) 
    else:
        self.insertNode(self.root , val)

def insertNode(self , currentNode , val): # val이 넣고자 하는 값
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                current.leftChild = Node(val)
        elif(val > currnetNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild ,val)
            else: 
                currentNode.rightChild = Node(val)
```

3) Delete 

삭제 결과로 이진탐색트리 속성이 깨질 수 있기 때문에 모든 경우의 수를 따져야 한다. 
- case 1 : 삭제할 노드에 자식노드가 없는 경우 
그냥 하나만 삭제하면 됨 
- case 2 : 삭제할 노드에 자식노드가 하나 있는 경우
해당 노드를 지우고, 해당 노드의 자식노드와 부모를 연결해주면 된다. 왼쪽 자식들은 무조건 부모보다 작기 때문에 왼쪽 자식의 자식들 또한 다 작거나 같은 상태. 이진탐색트리의 속성 때문이다. 
- case 3 : 삭제할 노드에 자식노드가 두개 있는 경우 

> 참고 
[이진탐색트리 (Binary Search Tree)](https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/)

```c
#include<iostream>
using namespace std;
struct Node {
    int data;
    struct Node*left;  // pointers to left node
    struct Node*right;
};

// root에서 부터 값 확인 
struct Node* Delete(struct Node*root , int data){
    if(root === NULL ) return root;
    else if(data < root->data) root->left = Delete(root->left ,data )
    else (data > data-> data) root-> right = Delete(root -> right , data)
    else // 값을 찾은 경우
    {   
        //Case 1 : No child
        if(root -> left == NULL && root -> right == NULL ){
            delete root;
            root = NULL;
            
        }
        // Case 2 : One child
        else if(root->left == NULL){
            struct Node * temp // current node의 주소값 저장하고 
            root = root -> right;
            delete temp; 
            
        }
        else if(root ->right == NULL){
            struct Node * temp // current node의 주소값 저장하고 
            root = root -> left;
            delete temp; 
            
        }
        // Case 3 : 2 children
        else {
            struct Node* temp = FindMin(root -> right);
            root -> data = temp -> data;
            root -> right = Delete(root -> right, temp ->data);

        }

    }
    return root
}
```