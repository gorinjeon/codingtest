# 첫 번째 줄: 정수의 개수 N 입력
N = int(input())

# 두 번째 줄: N개의 정수를 공백으로 구분하여 입력받아 리스트로 저장
numbers = list(map(int, input().split()))

# 세 번째 줄: 찾으려는 정수 v 입력
v = int(input())

# 리스트에서 v의 개수를 셈
count = numbers.count(v)

# 결과 출력
print(count)
