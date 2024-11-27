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


def ucs_search(board):
    board[board == 3] = 0
    pathsCosts = []
    startState = St(board)
    visited = []
    priorityqueue = [startState]
    while priorityqueue:

        priorityqueue.sort(key=lambda state: state.cost)

        currentState = priorityqueue.pop(0)

        pathsCosts.append(currentState.cost)

        visited.append(currentState)

        blueIndices = np.argwhere(currentState.board == 2)
        # if blueIndices.size > 0:
        currectBluePosition = [int(blueIndices[0][0]), int(blueIndices[0][1])]

        redIndices = np.argwhere(currentState.board == 4)
        # if redIndices.size > 0:
        currectRedPosition = [int(redIndices[0][0]), int(redIndices[0][1])]

        if currectBluePosition == [1, 1] and currectRedPosition == [2, 5]:

            path = []
            min_cost = currentState.cost
            while currentState.parent is not None:

                path.append(currentState.board)
                currentState = currentState.parent
            len(path)
            path.reverse()
            return path, len(visited), min_cost

        else:

            nextStates = St.next_State(
                currentState,
                [currectBluePosition[0], currectBluePosition[1]],
                [currectRedPosition[0], currectRedPosition[1]],
                # stateObj,
            )

            for each in nextStates:
                if each not in visited:
                    # newPath = path.append(each)
                    # priorityqueue.append(newPath)
                    priorityqueue.append(each)


# def cost(path):
#     cost = 0
#     for each_state in path:
#         cost += each_state.cost

#     return cost


# -------------------------------------------------
def recursive(currentState, visited, path):
    ###### إضافة الحالة الحالية إلى المسار ######
    if not isinstance(currentState, St):
        raise TypeError(
            "The 'state' parameter must be an instance of the 'State' class."
        )
    path.append(currentState.board)
    visited.append(currentState)

    ####### تحديد موقع المكعب الأزرق والأحمر ######
    blueIndices = np.argwhere(currentState.board == 2)
    currectBluePosition = [int(blueIndices[0][0]), int(blueIndices[0][1])]
    redIndices = np.argwhere(currentState.board == 4)
    currectRedPosition = [int(redIndices[0][0]), int(redIndices[0][1])]

    ####### التحقق من الوصول إلى الهدف ######
    if currectBluePosition == [1, 1] and currectRedPosition == [2, 5]:
        return path  # إعادة المسار عند الوصول إلى الهدف

    ####### هنا يتم التعرف على الحالات التالية ######
    nextStates = St.next_State(
        currentState,
        [currectBluePosition[0], currectBluePosition[1]],
        [currectRedPosition[0], currectRedPosition[1]],
    )

    for nextState in nextStates:
        if nextState not in visited:
            result = recursive(nextState, visited, path)
            if result is not None:  # إذا تم العثور على المسار، يتم إرجاعه
                return result

    # إذا لم يتم العثور على مسار، إزالة الحالة الحالية من المسار
    path.pop()
    return None


def dfs_search_recursive(board):
    board[board == 3] = 0
    startState = St(board)

    visited = []
    path = []

    result = recursive(startState, visited, path)

    if result:
        return result, len(visited)  # إعادة المسار وعدد الحالات التي تمت زيارتها
    else:
        return [], len(visited)  # إذا لم يتم العثور على مسار
