#Q13  Symmetric Difference

M = int(input()) #tells how many to store
a = set(map(int, input().split())) #stores that many

N = int(input())
b = set(map(int, input().split()))

result = a.symmetric_difference(b)

for i in sorted(result):
    print(i)
