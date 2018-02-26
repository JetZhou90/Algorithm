def reverse(stack):
    def getAndRemoveLast(stack):
        result = stack.pop()
        if len(stack) == 0:
            return result
        else:
            i = getAndRemoveLast(stack)
            stack.append(result)
            return i

    if len(stack) == 0:
        return
    i = getAndRemoveLast(stack)
    reverse(stack)
    stack.append(i)
    return stack