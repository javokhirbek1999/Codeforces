n = int(input())

colors = list(input())

i = 0

c = 0

while i+1 != len(colors):
    if colors[i] == colors[i+1]:
        colors.pop(i)
        c+=1
    else:
        i+=1

print(c)
