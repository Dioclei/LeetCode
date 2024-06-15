from typing import List
import heapq

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # compute distances according to the Boustrophedon style board
        rows = len(board)
        cols = len(board[0])

        labels = [[0 for col in range(cols)] for row in range(rows)]
        r = rows - 1
        c = 0
        going_right = True
        label = 1
        while r >= 0:
            labels[r][c] = label
            label += 1
            if going_right:
                if c == cols - 1:
                    # go up instead
                    r = r - 1
                    going_right = False
                else:
                    c = c + 1
            else:
                if c == 0:
                    # go up instead
                    r = r - 1
                    going_right = True
                else:
                    c = c - 1

        max_label = label - 1

        # create a reverse label search for easier computation
        coordinates = [0 for i in range(max_label)]
        for r in range(rows):
            for c in range(cols):
                idx = labels[r][c] - 1
                coordinates[idx] = (r, c)

        # create a min_steps array
        min_steps = [[max_label for c in range(cols)] for r in range(rows)]

        # represent every node as a tuple: (steps_moved, label)
        # i want to move the least amount of steps
        # define a transition helper function
        def get_transitions(node):
            current_steps_moved = node[0]
            label = node[1]
            transitions = []
            for i in range(6):
                dice_roll = i + 1
                new_label = label + dice_roll
                if new_label > max_label:
                    break
                # check if there is a snake or ladder
                c = coordinates[new_label - 1]
                if board[c[0]][c[1]] != -1:
                    new_label = board[c[0]][c[1]]
                # add to transitions
                new_steps_moved = current_steps_moved + 1
                r, c = coordinates[new_label - 1]
                if new_steps_moved < min_steps[r][c]:
                    min_steps[r][c] = new_steps_moved
                    new_node = (new_steps_moved, new_label)
                    transitions.append(new_node)
            return transitions

        # i want to look at the node with the least steps moved for the biggest label first
        pq = []
        first_node = (0, 1)
        heapq.heappush(pq, first_node)
        while len(pq) > 0:
            node = heapq.heappop(pq)
            steps = node[0]
            label = node[1]
            print(steps, label)
            # check if this node is the end
            if label == max_label:
                return steps
            # break infinite loop, it should not take more than max_label steps to complete the puzzle
            if steps > max_label:
                return -1
            # add new nodes
            for new_node in get_transitions(node):
                heapq.heappush(pq, new_node)
        return -1

board = [[1,1,-1],
         [1,1,1],
         [-1,1,1]]
sol = Solution()
print(sol.snakesAndLadders(board))

# Some comments:
# Pretty bad at graphs, so this is a good attempt!
# Can do BFS with a queue, with the min_steps array to memoise minimum distances. It will be the same as this pq solution.


