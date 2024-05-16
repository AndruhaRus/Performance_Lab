n = int(input("Ввделите число N: "))
m = int(input("Ввделите число M: "))
one_List = m * [int(i) for i in range(1, n + 1)]
two_List = [' ']
three_List = []
cnt = 0
while two_List[-1] != 1:
    two_List.clear()
    for j in range(cnt, m + cnt):
        two_List.append(one_List[j])
        cnt += 1
    two_List_copy = two_List.copy()
    three_List.append(two_List_copy)
    cnt -= 1
for k in range(len(three_List)):
    print(three_List[k][0], end='')