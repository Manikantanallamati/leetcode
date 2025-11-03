class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = []
        for i in range(m):
            grid.append([])
            for j in range(n):
                grid[i].append(0)
        for guard in guards:
            grid[guard[0]][guard[1]] = 1
        for wall in walls:
            grid[wall[0]][wall[1]] = 2
        for i in range(m):
            guard_seen = False
            for j in range(n):
                if grid[i][j] == 2:
                    guard_seen = False
                elif grid[i][j] == 1:
                    guard_seen = True
                elif guard_seen == True:
                    grid[i][j] = 3
        for i in range(m-1,-1,-1):
            guard_seen = False
            for j in range(n-1,-1,-1):
                if grid[i][j] == 2:
                    guard_seen = False
                elif grid[i][j] == 1:
                    guard_seen = True
                elif guard_seen == True:
                    grid[i][j] = 3
        for i in range(n-1,-1,-1):
            guard_seen = False
            for j in range(m-1,-1,-1):
                if grid[j][i] == 2:
                    guard_seen = False
                elif grid[j][i] == 1:
                    guard_seen = True
                elif guard_seen == True:
                    grid[j][i] = 3
        for i in range(n):
            guard_seen = False
            for j in range(m):
                if grid[j][i] == 2:
                    guard_seen = False
                elif grid[j][i] == 1:
                    guard_seen = True
                elif guard_seen == True:
                    grid[j][i] = 3
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
        return ans