class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        bestArea = 0

        def bfs(r, c, bestArea):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 0
                    ):
                        continue
                    area += 1
                    q.append((nr, nc))
                    grid[nr][nc] = 0
            
            bestArea = max(bestArea, area)
            return bestArea

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bestArea = bfs(r, c, bestArea)

        return bestArea 