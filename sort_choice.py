
def get_sort(input_ll):
    len_list = len(input_ll)
    for i in range(len_list):
        min = i
        for m in range(i, len_list):
            if input_ll[m] < input_ll[min]:
                min = m

        input_ll[i], input_ll[min] = input_ll[min], input_ll[i]

    return input_ll


print(get_sort([4, 5, 3, 9, 1, 7]))
