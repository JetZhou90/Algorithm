def sortByStack(stack):
    if len(stack) < 2:
        return stack
    stack1 = []
    while stack:
        cur = stack.pop()
        if len(stack1) == 0 or stack1[-1] >= cur:
            stack1.append(cur)
        else:
            while stack1:
                stack.append(stack1.pop())
            stack1.append(cur)
    while stack1:
        stack.append(stack1.pop())
    return stack

print(sortByStack([3,5,6,7,4,2,1]))
