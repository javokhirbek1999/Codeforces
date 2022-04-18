T = int(input())


for _ in range(T):

    word = input()

    if len(word)<=10:
        print(word)
    else:
        temp = word[0]
        temp+=str(len(word[1:len(word)-1]))
        temp+=word[-1]
        
        word = temp
        print(word)


