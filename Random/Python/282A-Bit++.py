n = int(input())


X = 0

for i in range(n):

    op = input()

    if op[0] == '+' and op[1] == '+' or op[-1] == '+' and op[-2] == '+':
        X+=1
    elif op[0] == '-' and op[1] == '-' or op[-1] == '-' and op[-2] == '-':
        X-=1
    else:
        pass

print(X)
