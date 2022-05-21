# 내 풀이
a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)

# 다른 사람의 풀이: https://imototot.tistory.com/194
a = int(input())
b = input()

a1 = a * int(b[2])
a2 = a * int(b[1])
a3 = a * int(b[0])
a4 = a * int(b)

print (a1, a2, a3, a4, sep='\n')
