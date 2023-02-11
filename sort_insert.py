
def sort_insert(inp_ll):
    wrk_list = list(map(int, inp_ll.split(',')))

    for i in range(len(wrk_list)):
        pos = i
        while pos > 0 and wrk_list[pos-1] > wrk_list[pos]:
            wrk_list[pos-1], wrk_list[pos] = wrk_list[pos], wrk_list[pos-1]
            pos -= 1

    return ','.join(str(i) for i in wrk_list)


print(sort_insert(input('Enter list for sort:')))
