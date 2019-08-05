# dfs

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [([0] * len(board[0])) for line in range(len(board))]
                    res = self.dfs(board, i, j, visited, word)
                    if res == True:
                        return True

        return False

    def dfs(self, board, i, j, visited, word):
        if len(word) == 0:
            return True
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and visited[i][j] == 0 and board[i][j] == word[0]:
            visited[i][j] = 1
            if self.dfs(board, i - 1, j, visited, word[1:]) or \
            self.dfs(board, i + 1, j, visited, word[1:]) or \
            self.dfs(board, i, j - 1, visited, word[1:]) or \
            self.dfs(board, i, j + 1, visited, word[1:]):
                return True

            visited[i][j] = 0
        else:
            return False
