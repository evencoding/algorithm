from sys import stdin

input = stdin.readline

found = False

for i in range(1, 6):
    name = input()
    if 'FBI' in name: 
        print(i, end = ' ')
        found = True
        
if not found: print('HE GOT AWAY!')