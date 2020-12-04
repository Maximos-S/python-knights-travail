from tree import Node


class KnightPathFinder():
    def __init__(self, root):
        self._root = root
        self._considered_positions = set(root)

    def get_valid_moves(self, pos):
        moves = []

        moves.append((pos[0]+2, pos[1]+1))
        moves.append((pos[0]+2, pos[1]-1))
        moves.append((pos[0]-2, pos[1]+1))
        moves.append((pos[0]-2, pos[1]-1))
        moves.append((pos[0]+1, pos[1]+2))
        moves.append((pos[0]+1, pos[1]-2))
        moves.append((pos[0]-1, pos[1]+2))
        moves.append((pos[0]-1, pos[1]-2))

        moves = {move for move in moves if (move[0] < 9 and move[0] > -1) and (move[1] < 9 and move[1] > -1)}
        return moves

    def new_move_positions(self, pos, ):
        validMoves = self.get_valid_moves(pos).difference(self._considered_positions)
        self._considered_positions = self._considered_positions.union(validMoves)
        # print(self._considered_positions)
        # print(validMoves)
        return validMoves 


# knight_moves = KnightPathFinder((6, 7))

# print(knight_moves.new_move_positions((8, 8)))

finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0))) 