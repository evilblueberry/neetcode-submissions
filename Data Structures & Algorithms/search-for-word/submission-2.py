class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        visited = set()


        def dfs(r, c, i):

            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visited.add((r, c))

            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in dirs:
                new_row = r + dr
                new_col = c + dc

                if 0 <= new_row < rows:
                    if 0 <= new_col < cols:
                        if (new_row, new_col) not in visited:
                            if dfs(new_row, new_col, i + 1):
                                return True

            visited.remove((r, c))
            return False


        

        for row in range(rows):
            for col in range(cols):
                visited.clear()

                if dfs(row, col, 0):
                    return True

        return False