class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited= set()
        deq=deque()
        dire= [(0,1),(1,0),(0,-1),(-1,0)]

        rows = len(grid)
        cols = len(grid[0])
        count=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count+=1
                    visited.add((i,j))
                    deq.append((i,j))

                    while deq:
                        elem_row,elem_col = deq.popleft()
                        for di in dire:
                            new_row = elem_row + di[0]
                            new_col = elem_col + di[1]
                            if 0 <= new_row < rows and 0 <= new_col<cols and grid[new_row][new_col] == '1' and (new_row,new_col) not in visited:
                                deq.append((new_row,new_col))
                                visited.add((new_row,new_col))

        return count

        