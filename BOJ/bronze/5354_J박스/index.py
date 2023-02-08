from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    if N < 3:
        for _ in range(N):
            print('#' * N)
        print()
    else:
        print('#' * N)
        for _ in range(N - 2):
            print('#' + 'J' * (N - 2) + '#')
        print('#' * N, '\n')