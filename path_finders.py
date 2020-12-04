from tree.py import Node


class KnightPathFinder():
    def __init__(self, root):
        self._root = root
        self._considered_positions = {root}

    def get_valid_moves(self, pos):
        moves = []

        moves.append(pos[0]+2, pos[1]+1)
        moves.append(pos[0]+2, pos[1]-1)
        moves.append(pos[0]-2, pos[1]+1)
        moves.append(pos[0]-2, pos[1]-1)
        moves.append(pos[0]+1, pos[1]+2)
        moves.append(pos[0]+1, pos[1]-2)
        moves.append(pos[0]-1, pos[1]+2)
        moves.append(pos[0]-1, pos[1]-2)

        moves = [move for move in moves if (moves[0] =< 8 and moves[0] => 0) and (moves[1] =< 8 and moves[1] => 0)]
        return moves