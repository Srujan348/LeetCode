class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point to the circle within the rectangle
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the distance between the circle's center and this closest point
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y
        
        # If the distance is less than or equal to the radius, they overlap
        return (distance_x ** 2) + (distance_y ** 2) <= radius ** 2