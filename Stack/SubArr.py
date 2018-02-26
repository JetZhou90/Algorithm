def getNum(arr, num):
    if arr == None or len(arr) == 0:
        return 0
    qmin = []
    qmax = []
    i = 0
    j = 0
    res = 0
    while i < len(arr):
        while j < len(arr):
            while qmin and arr[qmin[-1]] > arr[j]:
                qmin.pop()
            qmin.append(j)
            while qmax and arr[qmax[-1]] < arr[j]:
                qmax.pop()
            qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j += 1
        if qmin[0] == i:
            qmin.pop(0)
        if qmax[0] == i:
            qmax.pop(0)
        res += j - i
        i += 1
    return res

print(getNum([2,3,4,5,8],3))