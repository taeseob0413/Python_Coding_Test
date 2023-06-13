""""
다익스트라 알고리즘 : 여러개의 노드가 존재할 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘.
                   음의 간선이 없을 때 정상적으로 동작한다. (GPS 소프트웨어의 기본 알고리즘)
                   그리디 알고리즘으로 분석되기도 한다.

다익스트라 알고리즘 진행 순서
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다. >> 이때 선택된 노드는 방문처리
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신.
5. 3~4번을 반복한다.

다익스트라 알고리즘 종류
1. O(V^2)의 시간복잡도를 따르는 알고리즘 >> 구현 단순 but 느림.
2. O(ElogV)의 시간복잡도를 따르는 알고리즘 >> 구현 복잡 but 빠름.

다익스트라 알고리즘은 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택하는 과정을 반복하는데 이렇게 선택된 노드는 최단거리가 완전히 선택된
노드이므로 더 이상 알고리즘을 반복해도 최단 거리가 줄어들지 않는다.
>>한 단계당 하나의 노드에 대한 최단 거리를 확실하게 찾는 것으로 이해할 수 있음.

또한 위의 과정을 순차 탐색으로 진행할 경우에는 1번 알고리즘, 우선순위 큐를 사용할경우에는 2번 알고리즘에 해당한다.
"""