def largestRectangleArea(self, heights):
    stack = []
    area = 0
    heights.append(0)
    n = len(heights)

    for i in range(n):
        if not stack or heights[i] > heights[stack[-1]]:
            stack.append(i)
        else:
            while stack and heights[i] <= heights[stack[-1]]:
                h = heights[stack[-1]]
                stack.pop()
                w = i if not stack else i - stack[-1] - 1
                area = max(area, h * w)
            stack.append(i)
    return area
