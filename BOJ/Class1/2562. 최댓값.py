# 9개의 자연수를 입력받아 리스트에 저장
numbers = [int(input()) for _ in range(9)]

# enumerate를 사용하여 인덱스와 값을 동시에 순회
max_index, max_value = max(enumerate(numbers), key=lambda x: x[1])

# 최댓값과 그 인덱스를 출력
print(max_value)
print(max_index + 1)  # 인덱스는 0부터 시작하므로 1을 더해줌

#숏코딩
print(*max(zip(map(int,open(0)),range(1,10))))
