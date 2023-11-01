class Solution:
    def trap(self, height) -> int:
        stack = []
        water = 0
        current = 0

        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                water += distance * bounded_height
            stack.append(current)
            current += 1

        return water
