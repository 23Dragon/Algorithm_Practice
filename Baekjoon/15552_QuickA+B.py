import sys

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    