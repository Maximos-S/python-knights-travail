from tree import Node


class KnightPathFinder():
    def __init__(self, root):
        self._root = Node(root)
        self._considered_positions = set((root, ))

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

        moves = {move for move in moves if (move[0] < 8 and move[0] > -1) and (move[1] < 8 and move[1] > -1)}
        return moves

    def new_move_positions(self, pos, ):
        validMoves = self.get_valid_moves(pos).difference(self._considered_positions)
        self._considered_positions = self._considered_positions.union(validMoves)

        return validMoves 

    def build_move_tree(self,):
        valid_moves = self.new_move_positions(self._root.value)
        print(valid_moves)
        for move in valid_moves:
            child = Node(move)
            self._root.add_child(child)

        children = [child for child in self._root.children]
        while len(children):
            valid_moves = self.new_move_positions(children[0].value)
            for move in valid_moves:
                child = Node(move)
                children[0].add_child(child)

            children.extend(children[0].children)
            children.pop(0)

        print(self._root.children[0].children[0])


# knight_moves = KnightPathFinder((6, 7))

# print(knight_moves.new_move_positions((8, 8)))
finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder._root.children)
