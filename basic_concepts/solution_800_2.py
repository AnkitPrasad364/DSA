def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        a.append(x + (x - a[-1]))  # same logic: x + (x - a[n])

        ans = 0
        for i in range(1, len(a)):
            diff = a[i] - a[i - 1]
            ans = max(ans, diff)

        print(ans)

if __name__ == "__main__":
    main()