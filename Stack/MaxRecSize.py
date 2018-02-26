def maxRecSize(map):
    def maxRecFromBottom(height):
        if height == None or len(height) == 0:
            return 0
        stack = []
        maxArea = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] >= height[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                maxArea = max(maxArea, (i-k-1) * height[j])
            stack.append(i)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            maxArea = max(maxArea, (len(height)-k-1) * height[j])
        return maxArea

    if map == None or len(map) == 0 or len(map[0]) == 0:
        return 0
    height = [0 for i in range(len(map[0]))]
    maxArea = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            height[j] = 0 if map[i][j] == 0 else height[j] + 1
        maxArea = max(maxArea, maxRecFromBottom(height))
    return maxArea