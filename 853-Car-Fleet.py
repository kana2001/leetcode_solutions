class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = []
        for i in range(n):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort(key = lambda x: x[0])

        # (target - position) / speed + 1 to find how many turns to get to the target
        stack = []
        for i in range(n-1, -1, -1):
            turns = ((target - pos_speed[i][0]) / (pos_speed[i][1])) + 1
            if stack and turns <= stack[-1]:
                continue
            stack.append(turns)
        return len(stack)



    
        