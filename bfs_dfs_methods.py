from models.stateClass import State as St
import numpy as np

#####################################################


def dfs_search(board):

    board[board == 3] = 0
    startState = St(board)

    visited = []
    states = []
    stack = [startState]

    while stack:
        currentState = stack.pop()
        states.append(currentState)
        visited.append(currentState)

        blueIndices = np.argwhere(currentState.board == 2)
        # if blueIndices.size > 0:
        currectBluePosition = [int(blueIndices[0][0]), int(blueIndices[0][1])]
        redIndices = np.argwhere(currentState.board == 4)
        # if redIndices.size > 0:
        currectRedPosition = [int(redIndices[0][0]), int(redIndices[0][1])]

        # if np.array_equal(currentState.board, goal):
        if currectBluePosition == [1, 1] and currectRedPosition == [2, 5]:
            path = []

            while currentState.parent is not None:

                path.append(currentState.board)
                currentState = currentState.parent

            path.reverse()
            return path, len(visited)

        else:
            nextStates = St.next_State(
                currentState,
                [currectBluePosition[0], currectBluePosition[1]],
                [currectRedPosition[0], currectRedPosition[1]],
            )

            for each in nextStates:
                if each not in visited:

                    stack.append(each)


# ----------------------------------------------------------------
def bfs_search(board):

    board[board == 3] = 0

    startState = St(board)
    visited = []
    queue = [startState]

    while queue:
        currentState = queue.pop(0)
        visited.append(currentState)

        blueIndices = np.argwhere(currentState.board == 2)
        # if blueIndices.size > 0:
        currectBluePosition = [int(blueIndices[0][0]), int(blueIndices[0][1])]

        redIndices = np.argwhere(currentState.board == 4)
        # if redIndices.size > 0:
        currectRedPosition = [int(redIndices[0][0]), int(redIndices[0][1])]

        if currectBluePosition == [1, 1] and currectRedPosition == [2, 5]:
            path = []
            while currentState.parent is not None:

                path.append(currentState.board)
                currentState = currentState.parent

            path.reverse()
            return path, len(visited)

        else:

            nextStates = St.next_State(
                currentState,
                [currectBluePosition[0], currectBluePosition[1]],
                [currectRedPosition[0], currectRedPosition[1]],
                # stateObj,
            )

            for each in nextStates:
                if each not in visited:
                    queue.append(each)
