# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
a = int(input())
for i in range(a):
    print(i+1)


'''* 연산자는 언패킹 연산자로, range 객체에서 생성된 숫자들을 개별 인수로 변환합니다.
print 함수는 언패킹된 숫자들을 공백으로 구분하여 출력합니다.'''
print(*range(1, int(input()) + 1))
