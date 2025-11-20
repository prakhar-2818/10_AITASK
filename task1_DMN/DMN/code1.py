import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import random



def generate_maze(rows, cols, wall_prob=0.25):
    maze = np.zeros((rows, cols), dtype=int)
    for r in range(rows):
        for c in range(cols):
            if random.random() < wall_prob:
                maze[r][c] = 1  # 1 = wall
    return maze

def bfs(maze, start, keys):
    rows, cols = maze.shape
    visited = set()
    q = deque([start])
    path = []

    while q:
        r, c = q.popleft()

        if (r, c) in visited:
            continue

        visited.add((r, c))
        path.append((r, c))

        # found key
        if (r, c) in keys:
            keys.remove((r, c))

        if not keys:  # stop when done
            break

        # 4 directions
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0 and (nr,nc) not in visited:
                    q.append((nr, nc))

    return path



maze = generate_maze(20, 20, wall_prob=0.30)

# Random key positions
keys = {(random.randint(0,19), random.randint(0,19)) for _ in range(6)}

agent1_start = (0, 0)
agent2_start = (19, 19)

keys_list = list(keys)
keys1 = set(keys_list[:3])
keys2 = set(keys_list[3:])

# BFS paths
path1 = bfs(maze, agent1_start, keys1)
path2 = bfs(maze, agent2_start, keys2)



plt.figure(figsize=(7,7))
plt.title("Simple Dual Maze Navigation (Easy Visualization)")

# Maze background
plt.imshow(maze, cmap="gray_r")

# Draw keys as stars
for ky in keys:
    plt.scatter(ky[1], ky[0], marker="*", s=180, color="gold")

# Draw Agent 1 path (Blue)
p1 = np.array(path1)
plt.plot(p1[:,1], p1[:,0], color="blue", linewidth=2, label="Agent 1")

# Draw Agent 2 path (Red)
p2 = np.array(path2)
plt.plot(p2[:,1], p2[:,0], color="red", linewidth=2, label="Agent 2")

plt.legend()
plt.gca().invert_yaxis()
plt.show()
