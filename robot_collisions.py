class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Bundle data: [position, health, direction, original_index]
        robots = []
        for i in range(len(positions)):
            robots.append([positions[i], healths[i], directions[i], i])
            
        # Sort by position
        robots.sort(key=lambda x: x[0])
        
        stack = [] # Acts as stack for 'R' moving robots
        survivors = []
        
        for robot in robots:
            if robot[2] == 'L':
                while stack and stack[-1][1] < robot[1]:
                    stack.pop()
                    robot[1] -= 1
                    
                if not stack:
                    survivors.append(robot)
                elif stack[-1][1] == robot[1]:
                    stack.pop() # mutual destruction
                else:
                    stack[-1][1] -= 1 # stack robot wins
            else:
                stack.append(robot)
                
        # Combine remaining 'R' robots
        survivors.extend(stack)
        
        # Sort by original index
        survivors.sort(key=lambda x: x[3])
        
        return [robot[1] for robot in survivors]
