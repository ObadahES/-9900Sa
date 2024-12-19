import copy
from models.stateClass import State as St
import numpy as np
from queue import PriorityQueue
import time
import tracemalloc
from collections import deque


#####################################################
def get_position(board, value, level):
    result = np.argwhere(board == value)

    # تحقق إذا كان العنصر موجودًا في أكثر من موقع
    if result.size > 0:
        if len(result) > 1:
            print(f"Warning: Value {value} appears in multiple locations: {result}")

        # العودة إلى أول موقع فقط
        return [int(result[0][0]), int(result[0][1])]

    # تحديد القيم الافتراضية بناءً على المستوى
    default_positions = {
        10: {2: [2, 6], 4: [3, 5]},
        20: {6: [3, 7], 7: [3, 2], 8: [1, 5], 2: [2, 1], 4: [3, 4]},
        30: {6: [1, 14], 7: [1, 7], 8: [1, 11], 2: [4, 8], 4: [4, 5]},
    }

    # استرجاع الموقع بناءً على المستوى والقيمة
    return default_positions.get(level, {}).get(value, [])


def dfs_search(board):
    start_time = time.time()
    tracemalloc.start()
    # board[board == 3] = 0
    startState = St(board, None, 0, True, 0)

    visited = set()

    # states = []
    stack = [startState]
    level = 30
    while stack:
        currentState = stack.pop()
        # states.append(currentState)
        visited.add(currentState)

        currectBluePosition = get_position(currentState.board, 2, level)
        currectRedPosition = get_position(currentState.board, 4, level)
        currectGreenLightPosition = get_position(currentState.board, 6, level)
        currectPinkPosition = get_position(currentState.board, 7, level)
        currectOrangePosition = get_position(currentState.board, 8, level)

        if currectRedPosition == [4, 5] and currentState.changed_movement == True:

            currentState.visited_counter += 1
            currentState.changed_movement = False

        # if currectBluePosition == [2, 6] and currectRedPosition == [3, 5]:
        if (
            currectBluePosition == [4, 8]
            and currectRedPosition == [4, 5]
            and currectGreenLightPosition == [1, 14]
            and currectPinkPosition == [1, 7]
            and currectOrangePosition == [1, 11]
            and currentState.visited_counter == 2
            # currectBluePosition == [2, 1]
            # and currectRedPosition == [3, 4]
            # and currectGreenLightPosition == [3, 7]
            # and currectPinkPosition == [3, 2]
            # and currectOrangePosition == [1, 5]
        ):
            path = []

            while currentState.parent is not None:

                path.append(currentState.board)
                currentState = currentState.parent

            path.reverse()
            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            return path, len(visited)

        else:
            nextStates = St.next_State30(
                currentState,
                currectBluePosition,
                currectRedPosition,
                currectGreenLightPosition,
                currectPinkPosition,
                currectOrangePosition,
                currentState.changed_movement,
            )

            for each in nextStates:
                if each not in visited:
                    stack.append(each)


# ----------------------------------------------------------------


def bfs_search(board):
    start_time = time.time()
    tracemalloc.start()
    startState = St(board, None, 0, True, 0)
    visited = []
    queue = deque([startState])
    level = 30
    while queue:
        currentState = queue.popleft()

        # تسجيل الحالة الحالية كزرارة
        board_tuple = tuple(map(tuple, currentState.board))
        if board_tuple in visited:
            continue
        visited.append(board_tuple)

        currectBluePosition = get_position(currentState.board, 2, level)
        currectRedPosition = get_position(currentState.board, 4, level)
        currectGreenLightPosition = get_position(currentState.board, 6, level)
        currectPinkPosition = get_position(currentState.board, 7, level)
        currectOrangePosition = get_position(currentState.board, 8, level)

        if currectRedPosition == [4, 5] and currentState.changed_movement == True:

            currentState.visited_counter += 1
            currentState.changed_movement = False

        if (
            currectBluePosition == [4, 8]
            and currectRedPosition == [4, 5]
            and currectPinkPosition == [1, 7]
            and currectOrangePosition == [1, 11]
            and currectGreenLightPosition == [1, 14]
            and currentState.visited_counter == 2
            # currectBluePosition == [2, 6]
            # and currectRedPosition == [3, 5]
            # and currectGreenLightPosition == [3, 7]
            # and currectPinkPosition == [3, 2]
            # and currectOrangePosition == [1, 5]
        ):
            path = []
            while currentState.parent is not None:
                path.append(currentState.board)
                currentState = currentState.parent
            path.reverse()
            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
            return path, len(visited)

        # الحصول على الحالات التالية
        nextStates = St.next_State30(
            currentState,
            currectBluePosition,
            currectRedPosition,
            currectGreenLightPosition,
            currectPinkPosition,
            currectOrangePosition,
            currentState.changed_movement,
            # currentState.visited_counter,
        )

        for each in nextStates:
            next_board_tuple = tuple(map(tuple, each.board))
            if next_board_tuple not in visited:
                queue.append(each)

    # إذا لم يتم العثور على الحل
    end_time = time.time()
    print(f"No solution found after {end_time - start_time:.4f} seconds")
    return None, len(visited)


# ----------------------------------------------------


def ucs_search(board):
    start_time = time.time()
    tracemalloc.start()

    # إعداد الحالة الابتدائية
    startState = St(board, None, 0, True, 0)
    visited = set()  # استخدام مجموعة لتحسين التحقق من الحالات المزارة
    queue = PriorityQueue()  # قائمة الأولوية (priority queue)
    queue.put((0, startState))  # إضافة الحالة الابتدائية مع تكلفة 0

    level = 30

    while not queue.empty():
        current_cost, currentState = queue.get()  # استخراج الحالة بأقل تكلفة
        if not isinstance(currentState, St):
            raise TypeError(
                "The 'state' parameter must be an instance of the 'State' class."
            )
        # تسجيل الحالة الحالية كحالة مزارة
        board_tuple = tuple(map(tuple, currentState.board))
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        currectBluePosition = get_position(currentState.board, 2, level)
        currectRedPosition = get_position(currentState.board, 4, level)
        currectGreenLightPosition = get_position(currentState.board, 6, level)
        currectPinkPosition = get_position(currentState.board, 7, level)
        currectOrangePosition = get_position(currentState.board, 8, level)

        if currectRedPosition == [4, 5] and currentState.changed_movement == True:

            currentState.visited_counter += 1
            currentState.changed_movement = False

        # if currectBluePosition == [2, 6] and currectRedPosition == [3, 5]:
        if (
            currectBluePosition == [4, 8]
            and currectRedPosition == [4, 5]
            and currectPinkPosition == [1, 7]
            and currectOrangePosition == [1, 11]
            and currectGreenLightPosition == [1, 14]
            and currentState.visited_counter == 2
            # currectBluePosition == [2, 1]
            # and currectRedPosition == [3, 4]
            # and currectGreenLightPosition == [3, 7]
            # and currectPinkPosition == [3, 2]
            # and currectOrangePosition == [1, 5]
        ):
            path = []
            while currentState.parent is not None:
                path.append(currentState.board)
                currentState = currentState.parent
            path.reverse()
            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
            return path, len(visited)

        nextStates = St.next_State30(
            currentState,
            currectBluePosition,
            currectRedPosition,
            currectGreenLightPosition,
            currectPinkPosition,
            currectOrangePosition,
            currentState.changed_movement,
        )

        for each in nextStates:
            next_board_tuple = tuple(map(tuple, each.board))
            if next_board_tuple not in visited:
                queue.put((each.cost, each))

    # إذا لم يتم العثور على الحل
    end_time = time.time()
    print(f"No solution found after {end_time - start_time:.4f} seconds")
    return None, len(visited)


# -------------------------------------------------
def recursive(currentState, visited, path):

    if not isinstance(currentState, St):
        raise TypeError(
            "The 'state' parameter must be an instance of the 'State' class."
        )

    path.append(currentState.board)
    visited.append(currentState)
    currectBluePosition = get_position(currentState.board, 2, 30)
    currectRedPosition = get_position(currentState.board, 4, 30)
    currectGreenLightPosition = get_position(currentState.board, 6, 30)
    currectOrangePosition = get_position(currentState.board, 8, 30)
    currectPinkPosition = get_position(currentState.board, 7, 30)

    if currectRedPosition == [4, 5] and currentState.changed_movement == True:

        currentState.visited_counter += 1
        currentState.changed_movement = False

    if (
        currectBluePosition == [4, 8]
        and currectRedPosition == [4, 5]
        and currectGreenLightPosition == [1, 14]
        and currectPinkPosition == [1, 7]
        and currectOrangePosition == [1, 11]
        and currentState.visited_counter == 2
        # currectBluePosition == [2, 1]
        # and currectRedPosition == [3, 4]
        # and currectGreenLightPosition == [3, 7]
        # and currectPinkPosition == [3, 2]
        # and currectOrangePosition == [1, 5]
    ):
        return path

    nextStates = St.next_State30(
        currentState,
        currectBluePosition,
        currectRedPosition,
        currectGreenLightPosition,
        currectPinkPosition,
        currectOrangePosition,
        currentState.changed_movement,
    )

    for nextState in nextStates:
        if nextState not in visited:
            result = recursive(nextState, visited, path)
            if result is not None:
                return result

    path.pop()
    return None


def dfs_search_recursive(board):
    start_time = time.time()
    tracemalloc.start()
    # board[board == 3] = 0
    startState = St(board, None, 0, True, 0)

    visited = []
    path = []
    result = recursive(startState, visited, path)

    if result:
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Execution Time: {end_time - start_time:.4f} seconds")
        print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
        print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
        return result, len(visited)
    else:
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Execution Time: {end_time - start_time:.4f} seconds")
        print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
        print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
        return [], len(visited)


################################################# heuristic quiz #################################################
def heuristic(state):
    level = 30
    if level == 30:

        xRedGoal = 4
        yRedGoal = 5

        xBlueGoal = 4
        yBlueGoal = 8

        xOrangeGoal = 1
        yOrangeGoal = 11

        xGreenGoal = 1
        yGreenGoal = 14

        xPinkGoal = 1
        yPinkGoal = 7

    if level == 20:

        xRedGoal = 3
        yRedGoal = 4

        xBlueGoal = 2
        yBlueGoal = 1

        xOrangeGoal = 1
        yOrangeGoal = 5

        xGreenGoal = 3
        yGreenGoal = 7

        xPinkGoal = 3
        yPinkGoal = 2

    if level == 10:

        xRedGoal = 3
        yRedGoal = 5

        xBlueGoal = 2
        yBlueGoal = 6

        # xOrangeGoal = 1
        # yOrangeGoal = 5

        # xGreenGoal = 3
        # yGreenGoal = 7

        # xPinkGoal = 3
        # yPinkGoal = 2

    if not isinstance(state, St):
        raise TypeError(
            "The 'state' parameter must be an instance of the 'State' class."
        )

    currectBluePosition = get_position(state.board, 2, level)
    currectRedPosition = get_position(state.board, 4, level)
    currectGreenLightPosition = get_position(state.board, 6, level)
    currectPinkPosition = get_position(state.board, 7, level)
    currectOrangePosition = get_position(state.board, 8, level)

    hRed = abs((xRedGoal - currectRedPosition[0])) + abs(
        (yRedGoal - currectRedPosition[1])
    )
    hBlue = abs((xBlueGoal - currectBluePosition[0])) + abs(
        (yBlueGoal - currectBluePosition[1])
    )
    hGreen = abs((xGreenGoal - currectGreenLightPosition[0])) + abs(
        (yGreenGoal - currectGreenLightPosition[1])
    )
    hOrange = abs((xOrangeGoal - currectOrangePosition[0])) + abs(
        (yOrangeGoal - currectOrangePosition[1])
    )
    hPink = abs((xPinkGoal - currectPinkPosition[0])) + abs(
        (yPinkGoal - currectPinkPosition[1])
    )
    h = hRed + hBlue
    +hGreen + hOrange + hPink

    return h


# ----------------------------------------------------


def advanced_heuristic(state):

    if not isinstance(state, St):
        raise TypeError(
            "The 'state' parameter must be an instance of the 'State' class."
        )

    h = heuristic(state)
    g = state.cost
    f = h + g

    return f


# ----------------------------------------------------


def steepest_Hill_Climbing(board):

    start_time = time.time()
    tracemalloc.start()
    # board[board == 3] = 0
    startState = St(board, None, 0, True, 0)
    currentState = copy.deepcopy(startState)
    level = 30
    visited_states_count = 0
    while True:
        visited_states_count += 1
        currectBluePosition = get_position(currentState.board, 2, level)
        currectRedPosition = get_position(currentState.board, 4, level)
        currectGreenLightPosition = get_position(currentState.board, 6, level)
        currectOrangePosition = get_position(currentState.board, 8, level)
        currectPinkPosition = get_position(currentState.board, 7, level)

        if currectRedPosition == [4, 5] and currentState.changed_movement == True:

            currentState.visited_counter += 1
            currentState.changed_movement = False

        if (
            currectBluePosition == [4, 8]
            and currectRedPosition == [4, 5]
            and currectGreenLightPosition == [1, 14]
            and currectPinkPosition == [1, 7]
            and currectOrangePosition == [1, 11]
            and currentState.visited_counter == 2
            # currectBluePosition == [2, 6]
            # and currectRedPosition == [3, 5]
            # and currectGreenLightPosition == [3, 7]
            # and currectPinkPosition == [3, 2]
            # and currectOrangePosition == [1, 5]
        ):
            path = []
            while currentState.parent is not None:

                path.append(currentState.board)
                currentState = currentState.parent
            len(path)
            path.reverse()
            print(f"Number of visited states: {visited_states_count}")
            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            # print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
            return path

        nextStates = St.next_State30(
            currentState,
            currectBluePosition,
            currectRedPosition,
            currectGreenLightPosition,
            currectPinkPosition,
            currectOrangePosition,
            currentState.changed_movement,
        )

        nextState = min(nextStates, key=heuristic)

        # print(heuristic(currentState))
        # print("currentState.board : ", currentState.board)
        # print(heuristic(nextState))
        # print("nextState.board : ", nextState.board)

        if heuristic(nextState) >= heuristic(currentState):
            print(f"Number of visited states: {visited_states_count}")
            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            # print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
            break

        currentState = nextState


# -------------------------------------------------


def simplest_Hill_Climbing(board):
    start_time = time.time()
    tracemalloc.start()
    # board[board == 3] = 0
    startState = St(board, None, 0, True, 0)
    currentState = copy.deepcopy(startState)

    visited_states_count = 0  # عداد للحالات المزارة
    level = 30

    while True:
        visited_states_count += 1
        currectBluePosition = get_position(currentState.board, 2, level)
        currectRedPosition = get_position(currentState.board, 4, level)
        currectGreenLightPosition = get_position(currentState.board, 6, level)
        currectOrangePosition = get_position(currentState.board, 8, level)
        currectPinkPosition = get_position(currentState.board, 7, level)

        if currectRedPosition == [4, 5] and currentState.changed_movement == True:

            currentState.visited_counter += 1
            currentState.changed_movement = False

        if (
            currectBluePosition == [4, 8]
            and currectRedPosition == [4, 5]
            and currectGreenLightPosition == [1, 14]
            and currectPinkPosition == [1, 7]
            and currectOrangePosition == [1, 11]
            and currentState.visited_counter == 2
            # currectBluePosition == [2, 6]
            # and currectRedPosition == [3, 5]
            # and currectGreenLightPosition == [3, 7]
            # and currectPinkPosition == [3, 2]
            # and currectOrangePosition == [1, 5]
        ):
            path = []
            while currentState.parent is not None:
                path.append(currentState.board)
                currentState = currentState.parent
            path.reverse()

            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            # print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")

            return path, visited_states_count  # إرجاع المسار وعدد الحالات المزارة

        # الحصول على الحالات المجاورة
        nextStates = St.next_State30(
            currentState,
            currectBluePosition,
            currectRedPosition,
            currectGreenLightPosition,
            currectPinkPosition,
            currectOrangePosition,
            currentState.changed_movement,
        )

        stateChanged = False
        for nextState in nextStates:
            # visited_states_count += 1  # تحديث عداد الحالات المزارة
            # print(heuristic(nextState), heuristic(currentState))
            if heuristic(nextState) < heuristic(currentState):
                currentState = nextState
                stateChanged = True
                break

        # إذا لم يتم العثور على تحسين، توقف (local optimum)
        if not stateChanged:
            print("Stuck in local optimum!")
            # print(currentState.board)
            print(f"Number of visited states: {visited_states_count}")
            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
            return [], visited_states_count  # مسار فارغ وعدد الحالات المزارة


# --------------------------------------------------PriorityQueue


def a_Star_Advanced_Heuristic(board):
    start_time = time.time()
    tracemalloc.start()
    # board[board == 3] = 0

    startState = St(board, None, 0, True, 0)
    startState.cost = 0

    priorityQueue = PriorityQueue()
    priorityQueue.put((advanced_heuristic(startState), startState))
    level = 30
    visited = []

    visited_states_count = 0

    while not priorityQueue.empty():

        state_F_Cost, currentState = priorityQueue.get()

        if not isinstance(currentState, St):
            raise TypeError(
                "The 'state' parameter must be an instance of the 'State' class."
            )

        visited_states_count += 1

        currectBluePosition = get_position(currentState.board, 2, level)
        currectRedPosition = get_position(currentState.board, 4, level)
        currectGreenLightPosition = get_position(currentState.board, 6, level)
        currectPinkPosition = get_position(currentState.board, 7, level)
        currectOrangePosition = get_position(currentState.board, 8, level)

        if currectRedPosition == [4, 5] and currentState.changed_movement == True:

            currentState.visited_counter += 1
            currentState.changed_movement = False

        if (
            currectBluePosition == [4, 8]
            and currectRedPosition == [4, 5]
            and currectGreenLightPosition == [1, 14]
            and currectPinkPosition == [1, 7]
            and currectOrangePosition == [1, 11]
            and currentState.visited_counter == 2
            # currectBluePosition == [2, 6]
            # and currectRedPosition == [3, 5]
            # and currectGreenLightPosition == [3, 7]
            # and currectPinkPosition == [3, 2]
            # and currectOrangePosition == [1, 5]
        ):
            path = []
            while currentState.parent is not None:
                path.append(currentState.board)
                currentState = currentState.parent
            path.append(currentState.board)
            path.reverse()

            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")

            return path, visited_states_count

        visited.append(currentState)
        # print("currentState.board", currentState.board)
        nextStates = St.next_State30(
            currentState,
            currectBluePosition,
            currectRedPosition,
            currectGreenLightPosition,
            currectPinkPosition,
            currectOrangePosition,
            currentState.changed_movement,
        )

        for nextState in nextStates:

            if nextState in visited:
                continue

            priorityQueue.put((advanced_heuristic(nextState), nextState))

    # If no solution is found
    end_time = time.time()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
    print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
    return None, visited_states_count


# ------------------------------------------------------


def a_Star_Manhattan(board):

    start_time = time.time()
    tracemalloc.start()
    # board[board == 3] = 0

    startState = St(board, None, 0, True, 0)
    startState.cost = 0

    priorityQueue = PriorityQueue()
    priorityQueue.put((heuristic(startState), startState))

    visited = []

    visited_states_count = 0
    level = 30

    while not priorityQueue.empty():
        state_F_Cost, currentState = priorityQueue.get()

        visited_states_count += 1
        currectBluePosition = get_position(currentState.board, 2, level)
        currectRedPosition = get_position(currentState.board, 4, level)
        currectGreenLightPosition = get_position(currentState.board, 6, level)
        currectPinkPosition = get_position(currentState.board, 7, level)
        currectOrangePosition = get_position(currentState.board, 8, level)

        if currectRedPosition == [4, 5] and currentState.changed_movement == True:

            currentState.visited_counter += 1
            currentState.changed_movement = False
        # print(currectOrangePosition)

        # if currectBluePosition == [2, 6] and currectRedPosition == [3, 5]:
        if (
            currectBluePosition == [4, 8]
            and currectRedPosition == [4, 5]
            and currectGreenLightPosition == [1, 14]
            and currectPinkPosition == [1, 7]
            and currectOrangePosition == [1, 11]
            and currentState.visited_counter == 2
            # currectBluePosition == [2, 6]
            # and currectRedPosition == [3, 5]
            # and currectGreenLightPosition == [3, 7]
            # and currectPinkPosition == [3, 2]
            # and currectOrangePosition == [1, 5]
        ):
            path = []
            while currentState.parent is not None:
                path.append(currentState.board)
                currentState = currentState.parent
            path.append(currentState.board)
            path.reverse()

            end_time = time.time()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"Execution Time: {end_time - start_time:.4f} seconds")
            print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
            print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")

            return path, visited_states_count

        visited.append(currentState)

        nextStates = St.next_State30(
            currentState,
            currectBluePosition,
            currectRedPosition,
            currectGreenLightPosition,
            currectPinkPosition,
            currectOrangePosition,
            currentState.changed_movement,
        )

        for nextState in nextStates:
            if nextState in visited:
                continue

            priorityQueue.put((heuristic(nextState), nextState))

    end_time = time.time()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    path = []
    while currentState.parent is not None:
        path.append(currentState.board)
        currentState = currentState.parent
    path.append(currentState.board)
    path.reverse()

    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Current Memory Usage: {current_memory / 1024:.2f} KB")
    print(f"Peak Memory Usage: {peak_memory / 1024:.2f} KB")
    return path, visited_states_count
