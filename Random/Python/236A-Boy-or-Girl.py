username = input()


n = len(set(username))

if n%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
