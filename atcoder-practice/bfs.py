from collections import deque

# ファイルから入力を読み取る関数
def read_input_from_file(filepath):
    with open(file_path, 'r') as f:
        # 最初の行：H, W
        H, W = map(int, f.readline().strip().split())
        # 2行目：start座標
        start_r, start_c = map(int, f.readline().strip().split())
        # 3行目：goal座標
        goal_r, goal_c = map(int, f.readline().strip().split())
        # 残りの行：マップ情報
        grid = [f.readline().strip() for _ in range(H)]
    
    return H, W, (start_r - 1, start_c - 1), (goal_r - 1, goal_c - 1), grid

def bfs(H, W, start, goal, grid):
    
    
    Q = deque()
    visited = []
    for i in range(H):
      visited.append([-1]*W)
    
    Q.append(start)
    visited[start[0]][start[1]] = 0

    while Q:
        i,j = Q.popleft()
        
        for i2,j2 in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
           if visited[i2][j2] == -1 and 0 <= i2 < H and 0 <= j2 < W and grid[i2][j2] != "#":
               
               visited[i2][j2] = visited[i][j] + 1
               Q.append((i2,j2))
        
    return visited[goal[0]][goal[1]]   
               
if __name__ == "__main__":
    file_path = "./sample.txt"  # テストデータが保存されたファイルのパス
    H, W, start, goal, grid = read_input_from_file(file_path)
    
    print(bfs(H, W, start, goal, grid))
    
    
    
    
