T = int(input())
for test_case in range(T):
    ans = 0
    a, b, c = list(map(int, input().split()))

    if b >= c:
        ans += b - (c - 1)
        b = c - 1

    if a >= b:
        ans += a - (b - 1)
        a = b - 1
    
    if a <= 0:
        print(-1)
    else:
        print(ans)
