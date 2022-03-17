def make_table(p):
    global table

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]

        if p[i] == p[j]:
            j += 1
            table[i] = j

if __name__ == "__main__":
    pattern = "abacaba"
    table = [0] * len(pattern)
    make_table(pattern)
    print(table)
