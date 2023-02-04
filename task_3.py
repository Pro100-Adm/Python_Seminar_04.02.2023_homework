my_list = [7, 5, 3, 3, 2]


def s_list(num, lis):
    for i in range(len(lis)):
        if lis[i] < num:
            lis.insert(i, num)
            break
        elif i==len(lis)-1:
            lis.append(num)
            break
    return lis


print(*s_list(2, my_list))
