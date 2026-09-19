class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x = x1 if xCenter < x1 else (x2 if xCenter > x2 else xCenter)
        closest_y = y1 if yCenter < y1 else (y2 if yCenter > y2 else yCenter)
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        return (dx * dx) + (dy * dy) <= (radius * radius)
