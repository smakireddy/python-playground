"""
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc.
Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.

Example :

input:
grid = [[1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011

"""

from collections import deque


def shortestCellPath(grid, sr, sc, tr, tc):
    Q = deque()
    Q.append((sr, sc, 0))
    seen = {sr, sc}
    R = len(grid)
    C = len(grid[0])
    print(f'R,C -> {R},{C}')
    while len(Q) > 0:
        r, c, level = Q.popleft()
        print(f"r,c,level -> {r},{c},{level}")
        print(f'grid[tr][tc] -> {grid[tr][tc]}')
        if (r, c) == (tr, tc):
            return level

        for (nr, nc) in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            print(f"nr,nc -> {nr},{nc}")
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in seen:
                Q.append((nr, nc, level + 1))
                seen.add((nr, nc))

    return -1


if __name__ == '__main__':
    grid = [[1, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 1]]

    sr = 0
    sc = 0
    tr = 2
    tc = 0
    result = shortestCellPath(grid, sr, sc, tr, tc)
    print(result)
