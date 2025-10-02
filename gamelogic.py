# gamelogic.py

import math
import random

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

class Game:
    def __init__(self):
        self.board = [EMPTY]*9

    def check_winner(self):
        win_patterns = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] != EMPTY:
                return self.board[a]
        if EMPTY not in self.board:
            return "Draw"
        return None

    def available_moves(self):
        return [i for i,v in enumerate(self.board) if v == EMPTY]

    def minimax(self, depth, is_max, alpha, beta):
        winner = self.check_winner()
        if winner == PLAYER_O: return 10 - depth, None
        if winner == PLAYER_X: return -10 + depth, None
        if winner == "Draw": return 0, None

        if is_max:
            best_score, best_move = -math.inf, None
            for idx in self.available_moves():
                self.board[idx] = PLAYER_O
                score,_ = self.minimax(depth+1, False, alpha, beta)
                self.board[idx] = EMPTY
                if score > best_score:
                    best_score, best_move = score, idx
                alpha = max(alpha, best_score)
                if beta <= alpha: break
            return best_score, best_move
        else:
            best_score, best_move = math.inf, None
            for idx in self.available_moves():
                self.board[idx] = PLAYER_X
                score,_ = self.minimax(depth+1, True, alpha, beta)
                self.board[idx] = EMPTY
                if score < best_score:
                    best_score, best_move = score, idx
                beta = min(beta, best_score)
                if beta <= alpha: break
            return best_score, best_move

    def best_ai_move(self):
        if self.board.count(EMPTY) == 9:
            return random.choice([0,2,6,8])
        _, move = self.minimax(0, True, -math.inf, math.inf)
        return move
