# 백트래킹으로 구현 - 시간복잡도 줄일 필요 있음
def calc_ans():
    temp_arr = []
    for i in range(len(answer)):
        if answer[i] == 1:
            temp_arr.append(arr[i])
    dif_arr.append(max(temp_arr)-min(temp_arr))

def choose(curr_num, cnt):
    if curr_num == n+1:
        if cnt == m:
            calc_ans()
        return
    
    answer.append(0)
    choose(curr_num+1, cnt)
    answer.pop()

    answer.append(1)
    choose(curr_num+1, cnt+1)
    answer.pop()

    return

T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    if m == len(arr):
        print(f'#{test_case}', max(arr)-min(arr))
        continue
    answer = []
    dif_arr = []
    choose(1, 0)
    print(f'#{test_case}', min(dif_arr))



