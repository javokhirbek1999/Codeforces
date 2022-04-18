n = int(input())

c = 0

for i in range(n):
    arr = input().split(" ")

    if arr.count('1')>1:
        c+=1

print(c)
