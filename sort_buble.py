
def buble_sort (inp_val):
 """--doc string--"""
    wrk_list = list(map( int, inp_val.split(',') ) )
    l = len(wrk_list)
    for i in range(l-1, -1, -1):
        for j in range(i, -1, -1):
            if wrk_list[i]< wrk_list[j]:
                wrk_list[i], wrk_list[j] = wrk_list[j], wrk_list[i]

    return wrk_list

if __name__=='__main__':
    buble_sort(input())