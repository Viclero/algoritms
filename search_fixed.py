from random import sample


def s(list_, target):
    left, right = 0, len(list_) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_[middle] == target:
            return middle
        if list_[middle] < target:
            left = middle + 1
        else:
            right = middle - 1


print(s([1, 3, 8, 15, 20, 31, 45, 59], 59))

if __name__ == "__main__":
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))

    try:
        target = int(input('Pick a even number between 0-100: '))
        target_index = s(rand_list, target)

        print(f'List: {rand_list}')
        if target_index:
            print(f'Found {target} in index {target_index}')

        print(f'Cannot find {target} in the list')
    except ValueError:
        print('Invalid input')
