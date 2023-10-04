### 그래프 이론

- 그래프 자료구조 : 노드와 노드 사이 간선 정보를 갖는 자료구조
    - ex) 여러개의 도시가 연결되어 ~
    - 그래프의 표현
        - 인접 행렬 : 2차원 배열로 표현 / 플로이드 워셜 / 공간 O(V^2) , 시간 O(1)
        - 인접 리스트 : 리스트로 표현 / 다익스트라 / 공간 O(E), 시간 O(V)
    

- 그래프 알고리즘
    - 그래프 순차 탐색 : BFS/DFS
    - 최단거리 알고리즘 : 다익스트라, 플로이드 워셜, 벨만포드
    - 최소 신장트리 알고리즘 : 크루스칼 알고리즘(그리디)
    - 위상 정렬 알고리즘(큐 or 스택)
    

- 트리 vs 그래프
    - 순환성 X / 순환성 X or O
    - 계층 모델/ 네트워크 모델
    - 루트노드 O / 루트노드 X
    - 부모자식 관계 / 부모자식 관계 X
    - 방향 / 뱡향 or 무방향
    
### 서로소 집합 자료구조(disjoint_sets)

- 서로소 집합 자료주고는 서로소 부분집합으로 나누어진 원소들의 data를 처리하기 위한 자료구조.
- union / find 두 개의 연산으로 이루어져 있음.
- 작동 원리
    - A와 B의 루트노드 A',B' 찾기 >> find
    - B'의 부모 노드로 A'을 설정 >>union
    
- 소스코드

```python
#find 함수의 첫번째 소스코드 >> 이 경우에는 부모 테이블이 각각의 부모와 연결되어 있음.
def find_parent(parent, x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x

#find 함수의 두번째 소스코드 >> 이 경우에는 부모 테이블의 값이 루트노드와 연결되어 있음.
def find_parent1(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent1(parent,parent[x])
    return parent[x]
#union 함수
def union_parent(parent,a,b):
    a=find_parent1(parent,a)
    b=find_parent1(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
```



    