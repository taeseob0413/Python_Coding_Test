"""
파이썬에서는 정렬된 데이터에서 특정 원소를 찾을 때 bisect 라이브러리의 bisect_left, bisect_right를 사용할 수 있다.
bisect_left(데이터,x) = 정렬된 순서를 유지하면서 x를 삽입할 수 있는 맨 왼쪽 인덱스 반환
bisect_right(데이터,x) = 정렬된 순서를 유지하면서 x를 삽입할 수 있는 맨 오른쪽 인덱스 반환

>>bisect_right(데이터,5)-bisect_left(데이터,5) - 데이터 중에서 5의 갯수를 반환한다.
>>bisect_right(데이터,-1)-bisect_left(데이터,5) - 데이터 중에서 -1~5 사이 원소의 갯수를 반환한다.
"""