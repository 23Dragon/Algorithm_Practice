if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [int(x) for x in range(1, N+1)]
    result = [0] * M

    solve()