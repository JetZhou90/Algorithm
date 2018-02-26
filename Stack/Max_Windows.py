def getMaxWindow(arr, w):
    if arr == None or w < 1 or len(arr) < w:
        return
    deque = []
    res = []
    for i in range(len(arr)):
        while deque and arr[deque[-1]] <= arr[i]:
            deque.pop()
        deque.append(i)
        if deque[0] <= i - w:
            deque.pop(0)
        if i-w+1 >= 0:
            res.append(arr[deque[0]])
    return res