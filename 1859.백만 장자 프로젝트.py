T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    while len(arr) > 1:
        max_idx = arr.index(max(arr))
        max_num = arr[max_idx]
        profit_arr = [max_num - x for x in arr[:max_idx]]
        ans += sum(profit_arr)
        arr = arr[max_idx+1:]
    print(f"#{test_case}", ans)