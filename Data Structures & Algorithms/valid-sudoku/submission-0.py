class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # hashtable for each criteria
        # 1. 9 3x3s -> (3 digits + 6 indices) * 3
        # 2. 9 verticals -> (1 digit + 9 indices) * 9
        # 3. 9 horizontals -> 9 digits

        # O(n^2) iterate through 2d list, append to respective hashtables

        ht = [set() for _ in range(27)]

        for i in range(9):
            for j in range(9):
                tile = board[i][j]
                if tile == '.':
                    continue

                squares_idx = (i // 3) * 3 + (j // 3)
                verts_idx = 9 + j
                horis_idx = 18 + i

                if (tile in ht[squares_idx] or
                    tile in ht[verts_idx] or
                    tile in ht[horis_idx]):
                    return False

                ht[squares_idx].add(tile)
                ht[verts_idx].add(tile)
                ht[horis_idx].add(tile)

        return True






