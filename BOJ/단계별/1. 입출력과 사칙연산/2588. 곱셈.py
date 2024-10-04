# 내 풀이
a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)

# 다른 사람의 풀이: https://like-a-happy-cat.tistory.com/10
A = int(input())
B = input()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))
