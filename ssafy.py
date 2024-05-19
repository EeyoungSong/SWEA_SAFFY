def main():
    T = int(input())

    for test_case in range(1, T + 1):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        ans_list = []

        for elem1 in arr:
            for elem2 in arr:
                ans_list.append((elem1, elem2))
        ans_list.sort()
        print(ans_list)
        ans = sum(ans_list[k-1])


        # 표준출력(화면)으로 답안을 출력합니다.
        print(f"#{test_case} {ans}")
      


if __name__ == "__main__":

    main()