from sys import stdin

for _ in range(int(input())):
    N = int(input())
    print(f'{N} is odd' if N % 2 else f'{N} is even')
