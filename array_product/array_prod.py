#!/usr/local/bin/python3.6

from pprint import pprint, pformat

array = [1, 2, 3, 4, 5]

def array_prod_01(arr):
    prod = 1
    for ix in arr:
        prod = prod * ix
    out_arr = [prod for x in range(len(arr))]
    out_arr = [out_arr[ix]//arr[ix] for ix in range(len(arr))]
    return out_arr

def array_prod_02(arr):
    pref=[]
    for ix in range(len(arr)):
        if ix == 0:
            pref = [arr[0]]
        else:
            pref.append(arr[ix] * pref[ix-1])
    print("prefix: {}".format(pformat(pref)))

    suff=[0 for ix in range(len(arr))] 
    for ix in range(len(arr)):
        rx = len(arr) - 1 - ix
        if rx == (len(arr) - 1):
            suff[rx] = arr[-1]
        else:
            suff[rx] = (arr[rx] * suff[rx+1])
    print("suffix: {}".format(pformat(suff)))
    out_arr = arr
    for ix in range(len(arr)):
        if ix == 0:
            out_arr[ix] = suff[1]
        elif ix == len(arr)-1:
            out_arr[ix] = pref[len(arr)-2]
        else:
            out_arr[ix] = pref[ix-1] * suff[ix+1]

    print("out: {}".format(pformat(out_arr)))


pprint(array)
pprint(array_prod_01(array))


pprint(array)
pprint(array_prod_02(array))
