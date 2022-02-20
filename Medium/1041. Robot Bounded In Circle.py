class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cx, cy = 0, 0   # current position of robot
        dx, dy = 0, 1   # change of x and y if command "G" encountered
        for c in instructions:
            if c == "G":
                cx += dx
                cy += dy
            else:
                # rotate
                sign = 1 if c == "L" else -1
                # trial and error binary math to determine new direction
                if dx:
                    dx, dy = 0, dx * sign
                else:
                    dx, dy = -dy*sign, 0
                
        # robot stays in circle, if returning to original position after one loop
        # or if robot is no longer facing upwards
        return (cx == 0 and cy == 0) or dy !=1