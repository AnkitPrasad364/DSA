def can_sort_boxes(t, test_cases):
    results = []
    for n, k, arr in test_cases:
        if k == 1:
            results.append("YES" if arr == sorted(arr) else "NO")
        else:
            results.append("YES")
    return results

# Example usage:
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((n, k, arr))

results = can_sort_boxes(t, test_cases)
for res in results:
    print(res)