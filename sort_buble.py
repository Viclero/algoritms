
def buble_sort(inp_val):
    wrk_list = list(map(int, inp_val.split(',')))

    for i in range(len(wrk_list)-1, -1, -1):
        for j in range(i, -1, -1):
            if wrk_list[i] < wrk_list[j]:
                wrk_list[i], wrk_list[j] = wrk_list[j], wrk_list[i]

    return wrk_list


if __name__ == '__main__':
    print(buble_sort(input()))
