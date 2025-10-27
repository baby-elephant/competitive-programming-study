from collections import Counter
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    xs = list(map(int, data[1:1+n]))

    cnt = Counter(x - 1 for x in xs)  # 0-index化（C++の a[x-1] 相当）

    ans = 0
    for c in cnt.values():
        # a[i] * (a[i] - 1) / 2 * (n - a[i])
        ans += (c * (c - 1) // 2) * (n - c)

    print(ans)

if __name__ == "__main__":
    main()
