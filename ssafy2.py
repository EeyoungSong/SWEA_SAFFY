T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    people = sorted(list(map(int, input().split())))
    hats = sorted(list(map(int, input().split())))

    print(people)
    print(hats)
    cnt = 0
    for person in people:
        for hat in hats:
           if abs(person - hat) <= 3:
               hats.remove(hat)
               cnt += 1 
               break
        print(people)
        print(hats)
        print(cnt)


    print(f"#{test_case} {cnt}")