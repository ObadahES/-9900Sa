import copy
import numpy as np

import algorithms
import sys

sys.setrecursionlimit(5000)
###########################################


class State:
    def __init__(
        self, board=None, parent=None, cost=0, changed_movement=False, visited_counter=0
    ):
        self.board = board
        self.parent = parent
        self.goals = [(1, 1), (2, 2)]
        self.cost = cost
        self.visited_counter = visited_counter
        self.changed_movement = changed_movement

    # ----------------------------------------------------------------

    def set_Board(self, board):
        self.board = board

    # ----------------------------------------------------------------

    def get_Board(self):
        return self.board

    # ----------------------------------------------------------------

    def __eq__(self, other):
        # مقارنة الكائنات بناءً على المصفوفة board فقط
        if isinstance(other, State):
            return np.array_equal(self.board, other.board)
        return False

    # ----------------------------------------------------------------

    def __lt__(self, other):
        # Compare based on heuristic values (or other criteria)
        if isinstance(other, State):
            return algorithms.advanced_heuristic(self) < algorithms.advanced_heuristic(
                other
            )
        return False

    # ----------------------------------------------------------------

    def __hash__(self):
        # تحويل المصفوفة numpy.ndarray إلى tuple بحيث تصبح قابلة للتجزئة
        return hash(tuple(map(tuple, self.board)))

    # ----------------------------------------------------------------
    def squaremove(
        teststate,
        nextstate,
        row,
        column,
        currentColorRow,
        currentColorCol,
        r,
        w,
        squareValue,
        color,
        color_Cost,
        colorOver=True,
        decision=False,
    ):
        # color_Cost = 0
        color_conditions = {
            "Red": [1, 2, 6, 7, 8],
            "Blue": [1, 4, 6, 7, 8],
            "Orange": [2, 6, 7, 4, 1],
            "Green": [2, 4, 7, 8, 1],
            "Pink": [2, 6, 4, 8, 1],
        }

        nextCondation = color_conditions.get(color, [])

        if (
            (
                teststate.board[currentColorRow + r][currentColorCol + w]
                not in nextCondation
                or decision == True
            )
            and nextstate.board[currentColorRow + r][currentColorCol + w]
            not in nextCondation
            and (0 < currentColorRow < row)
            and (0 < currentColorCol < column)
        ):
            decision = True

            nextstate.board[currentColorRow][currentColorCol] = 0
            currentColorRow += r
            currentColorCol += w
            nextstate.board[currentColorRow][currentColorCol] = squareValue
            # color_Cost+=1

            color_Cost += abs(r) + abs(w)
            return (
                color_Cost,
                nextstate,
                colorOver,
                currentColorRow,
                currentColorCol,
                decision,
            )

        else:
            colorOver = False
            decision = False
            return (
                color_Cost,
                nextstate,
                colorOver,
                currentColorRow,
                currentColorCol,
                decision,
            )

    def next_State20(
        state,
        currentBlue,
        currentRed,
        currentGreenLight,
        currentPink,
        currentOrange,
    ):

        nextSteps = []
        stepsList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        teststate = copy.deepcopy(state)
        # print("teststate", teststate.board)
        # print(currentOrange)
        for r, w in stepsList:

            red_Decision = False
            blue_Decision = False
            orange_Decision = False
            pink_Decision = False
            green_Decision = False

            nextstate = copy.deepcopy(state)
            blueOver = True
            redOver = True
            orangeOver = True
            greenLightOver = True
            pinkOver = True

            if currentRed != [3, 4]:
                currentRedRow, currentRedCol = currentRed
            else:
                currentRedRow, currentRedCol = 3, 4

            if currentBlue != [2, 1]:
                currentBlueRow, currentBlueCol = currentBlue
            else:
                currentBlueRow, currentBlueCol = 2, 1

            if currentPink != [3, 2]:
                currentPinkRow, currentPinkCol = currentPink
            else:
                currentPinkRow, currentPinkCol = 3, 2

            if currentOrange != [1, 5]:
                currentOrangeRow, currentOrangeCol = currentOrange
            else:
                currentOrangeRow, currentOrangeCol = 1, 5
            if currentGreenLight != [3, 7]:
                currentGreenLightRow, currentGreenLightCol = currentGreenLight
            else:
                currentGreenLightRow, currentGreenLightCol = 3, 7

            _Cost = 0

            while redOver or blueOver or orangeOver or greenLightOver or pinkOver:

                if (currentRedRow, currentRedCol) == (3, 4):
                    if nextstate.board[currentRedRow][currentRedCol] not in [
                        2,
                        7,
                        8,
                        6,
                        1,
                    ]:
                        nextstate.board[3][4] = 0
                    redOver = False
                else:
                    (
                        _Cost,
                        # red_Cost,
                        nextstate,
                        redOver,
                        currentRedRow,
                        currentRedCol,
                        red_Decision,
                    ) = State.squaremove(
                        teststate,
                        nextstate,
                        4,
                        8,
                        currentRedRow,
                        currentRedCol,
                        r,
                        w,
                        4,
                        "Red",
                        _Cost,
                        # red_Cost,
                        redOver,
                        red_Decision,
                    )

                if (currentBlueRow, currentBlueCol) == (2, 1):
                    if nextstate.board[currentBlueRow][currentBlueCol] not in [
                        7,
                        4,
                        8,
                        6,
                        1,
                    ]:
                        nextstate.board[2][1] = 0
                    blueOver = False
                else:

                    (
                        _Cost,
                        # blue_Cost,
                        nextstate,
                        blueOver,
                        currentBlueRow,
                        currentBlueCol,
                        blue_Decision,
                    ) = State.squaremove(
                        teststate,
                        nextstate,
                        4,
                        8,
                        currentBlueRow,
                        currentBlueCol,
                        r,
                        w,
                        2,
                        "Blue",
                        _Cost,
                        # blue_Cost,
                        blueOver,
                        blue_Decision,
                    )

                if (currentPinkRow, currentPinkCol) == (3, 2):
                    if nextstate.board[currentPinkRow][currentPinkCol] not in [
                        2,
                        4,
                        8,
                        6,
                        1,
                    ]:
                        nextstate.board[3][2] = 0
                    pinkOver = False
                else:

                    (
                        _Cost,
                        # pink_Cost,
                        nextstate,
                        pinkOver,
                        currentPinkRow,
                        currentPinkCol,
                        pink_Decision,
                    ) = State.squaremove(
                        teststate,
                        nextstate,
                        4,
                        8,
                        currentPinkRow,
                        currentPinkCol,
                        r,
                        w,
                        7,
                        "Pink",
                        _Cost,
                        # pink_Cost,
                        pinkOver,
                        pink_Decision,
                    )

                if (currentGreenLightRow, currentGreenLightCol) == (3, 7):
                    if nextstate.board[currentGreenLightRow][
                        currentGreenLightCol
                    ] not in [2, 4, 8, 7, 1]:
                        nextstate.board[3][7] = 0
                    greenLightOver = False
                else:

                    (
                        _Cost,
                        # green_Cost,
                        nextstate,
                        greenLightOver,
                        currentGreenLightRow,
                        currentGreenLightCol,
                        green_Decision,
                    ) = State.squaremove(
                        teststate,
                        nextstate,
                        4,
                        8,
                        currentGreenLightRow,
                        currentGreenLightCol,
                        r,
                        w,
                        6,
                        "Green",
                        _Cost,
                        # green_Cost,
                        greenLightOver,
                        green_Decision,
                    )

                if (currentOrangeRow, currentOrangeCol) == (1, 5):
                    if nextstate.board[currentOrangeRow][currentOrangeCol] not in [
                        2,
                        4,
                        7,
                        6,
                        1,
                    ]:
                        nextstate.board[1][5] = 0
                    orangeOver = False
                else:

                    (
                        _Cost,
                        # orange_Cost,
                        nextstate,
                        orangeOver,
                        currentOrangeRow,
                        currentOrangeCol,
                        orange_Decision,
                    ) = State.squaremove(
                        teststate,
                        nextstate,
                        4,
                        8,
                        currentOrangeRow,
                        currentOrangeCol,
                        r,
                        w,
                        8,
                        "Orange",
                        _Cost,
                        orangeOver,
                        orange_Decision,
                    )

            if nextstate != state:
                # print("nextstate.board", nextstate.board)
                # print("state.board", state.board)
                nextSteps.append(
                    State(
                        nextstate.board,
                        state,
                        cost=state.cost + _Cost,
                        # + red_Cost
                        # + green_Cost
                        # + blue_Cost
                        # + pink_Cost
                        # + orange_Cost,
                    )
                )
        # print(len(nextSteps))
        # for nextStep in nextSteps:
        #     # print(nextStep.cost)
        #     print("next", nextStep.board)
        return nextSteps

    # ----------------------------------------------------------------

    def next_State10(
        state,
        currentBlue,
        currentRed,
    ):

        if not isinstance(state, State):
            raise TypeError(
                "The 'state' parameter must be an instance of the 'State' class."
            )

        nesxSteps = []
        stepsList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        teststate = copy.deepcopy(state)
        # print("teststate", teststate.board)

        for r, w in stepsList:

            nextstate = copy.deepcopy(state)
            blueOver = True
            redOver = True
            if currentRed != [3, 5]:
                currentRedRow, currentRedCol = currentRed
            else:
                currentRedRow, currentRedCol = 3, 5

            if currentBlue != [2, 6]:
                currentBlueRow, currentBlueCol = currentBlue
            else:
                currentBlueRow, currentBlueCol = 2, 6
            _Cost = 0
            red_Decision = False
            blue_Decision = False

            while redOver or blueOver:

                if (currentRedRow, currentRedCol) == (3, 5):
                    if nextstate.board[currentRedRow][currentRedCol] not in [
                        2,
                        1,
                    ]:
                        nextstate.board[3][5] = 0
                    redOver = False
                else:
                    (
                        _Cost,
                        nextstate,
                        redOver,
                        currentRedRow,
                        currentRedCol,
                        red_Decision,
                    ) = State.squaremove(
                        teststate,
                        nextstate,
                        7,
                        11,
                        currentRedRow,
                        currentRedCol,
                        r,
                        w,
                        4,
                        "Red",
                        _Cost,
                        redOver,
                        red_Decision,
                    )

                if (currentBlueRow, currentBlueCol) == (2, 6):
                    if nextstate.board[currentBlueRow][currentBlueCol] not in [
                        # 7,
                        4,
                        # 8,
                        # 6,
                        1,
                    ]:
                        nextstate.board[2][6] = 0
                    blueOver = False
                else:

                    (
                        _Cost,
                        nextstate,
                        blueOver,
                        currentBlueRow,
                        currentBlueCol,
                        blue_Decision,
                    ) = State.squaremove(
                        teststate,
                        nextstate,
                        7,
                        11,
                        currentBlueRow,
                        currentBlueCol,
                        r,
                        w,
                        2,
                        "Blue",
                        _Cost,
                        blueOver,
                        blue_Decision,
                    )

            if nextstate != state:
                nesxSteps.append(
                    State(
                        nextstate.board,
                        state,
                        cost=state.cost + _Cost,
                        # + blue_Cost + red_Cost,
                    )
                )
        # print(len(nesxSteps))
        # for nesxStep in nesxSteps:
        #     print("next", nesxStep.board)
        return nesxSteps

    # ----------------------------------------------------------------
    def squaremove30(
        teststate,
        nextstate,
        row,
        column,
        currentColorRow,
        currentColorCol,
        r,
        w,
        squareValue,
        color,
        color_Cost,
        colorOver=True,
        decision=False,
        lost=False,
    ):
        # color_Cost = 0
        color_conditions = {
            "Red": [1, 2, 6, 7, 8],
            "Blue": [1, 4, 6, 7, 8],
            "Orange": [2, 6, 7, 4, 1],
            "Green": [2, 4, 7, 8, 1],
            "Pink": [2, 6, 4, 8, 1],
        }

        nextCondation = color_conditions.get(color, [])

        if (
            (
                teststate.board[currentColorRow + r][currentColorCol + w]
                not in nextCondation
                or decision == True
            )
            and nextstate.board[currentColorRow + r][currentColorCol + w]
            not in nextCondation
            and (0 < currentColorRow < row)
            and (0 < currentColorCol < column)
        ):
            decision = True

            nextstate.board[currentColorRow][currentColorCol] = 0
            currentColorRow += r
            currentColorCol += w
            nextstate.board[currentColorRow][currentColorCol] = squareValue
            if (currentColorRow, currentColorCol) == (5, 8):
                lost = True

            color_Cost += abs(r) + abs(w)
            return (
                color_Cost,
                nextstate,
                colorOver,
                currentColorRow,
                currentColorCol,
                decision,
                lost,
            )

        else:
            colorOver = False
            decision = False
            return (
                color_Cost,
                nextstate,
                colorOver,
                currentColorRow,
                currentColorCol,
                decision,
                lost,
            )

    def next_State30(
        state,
        currentBlue,
        currentRed,
        currentGreenLight,
        currentPink,
        currentOrange,
        changed_movement,
        # visited_counter,
    ):
        if not isinstance(state, State):
            raise TypeError(
                "The 'state' parameter must be an instance of the 'State' class."
            )
        nesxSteps = []
        stepsList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        teststate = copy.deepcopy(state)
        # print(teststate.board)

        for r, w in stepsList:

            lost = False
            nextstate = copy.deepcopy(state)

            blueOver = True
            redOver = True
            orangeOver = True
            greenLightOver = True
            pinkOver = True

            if currentRed != [4, 5]:
                currentRedRow, currentRedCol = currentRed
            else:
                currentRedRow, currentRedCol = 4, 5

            if currentBlue != [4, 8]:
                currentBlueRow, currentBlueCol = currentBlue
            else:
                currentBlueRow, currentBlueCol = 4, 8

            if currentPink != [1, 7]:
                currentPinkRow, currentPinkCol = currentPink
            else:
                currentPinkRow, currentPinkCol = 1, 7

            if currentOrange != [1, 11]:
                currentOrangeRow, currentOrangeCol = currentOrange
            else:
                currentOrangeRow, currentOrangeCol = 1, 11

            if currentGreenLight != [1, 14]:
                currentGreenLightRow, currentGreenLightCol = currentGreenLight
            else:
                currentGreenLightRow, currentGreenLightCol = 1, 14

            _Cost = 0

            red_Decision = False
            blue_Decision = False
            orange_Decision = False
            pink_Decision = False
            green_Decision = False
            # print(visited_counter)
            while redOver or blueOver or orangeOver or greenLightOver or pinkOver:

                if (
                    (currentRedRow, currentRedCol)
                    == (
                        4,
                        5,
                    )
                    and nextstate.visited_counter == 2
                    and nextstate.changed_movement == False
                ):
                    if nextstate.board[currentRedRow][currentRedCol] not in [
                        2,
                        7,
                        8,
                        6,
                        1,
                    ]:
                        nextstate.board[4][5] = 0
                    redOver = False
                else:
                    if (currentRedRow, currentRedCol) == (4, 5):
                        nextstate.changed_movement = True
                    (
                        _Cost,
                        nextstate,
                        redOver,
                        currentRedRow,
                        currentRedCol,
                        red_Decision,
                        lost,
                    ) = State.squaremove30(
                        teststate,
                        nextstate,
                        6,
                        15,
                        currentRedRow,
                        currentRedCol,
                        r,
                        w,
                        4,
                        "Red",
                        _Cost,
                        redOver,
                        red_Decision,
                        lost,
                    )

                if (currentBlueRow, currentBlueCol) == (4, 8):
                    if nextstate.board[currentBlueRow][currentBlueCol] not in [
                        7,
                        4,
                        8,
                        6,
                        1,
                    ]:
                        nextstate.board[4][8] = 0
                    blueOver = False
                else:

                    (
                        _Cost,
                        nextstate,
                        blueOver,
                        currentBlueRow,
                        currentBlueCol,
                        blue_Decision,
                        lost,
                    ) = State.squaremove30(
                        teststate,
                        nextstate,
                        6,
                        15,
                        currentBlueRow,
                        currentBlueCol,
                        r,
                        w,
                        2,
                        "Blue",
                        _Cost,
                        blueOver,
                        blue_Decision,
                        lost,
                    )

                if (currentPinkRow, currentPinkCol) == (1, 7):
                    if nextstate.board[currentPinkRow][currentPinkCol] not in [
                        2,
                        4,
                        8,
                        6,
                        1,
                    ]:
                        nextstate.board[1][7] = 0
                    pinkOver = False
                else:

                    (
                        _Cost,
                        # pink_Cost,
                        nextstate,
                        pinkOver,
                        currentPinkRow,
                        currentPinkCol,
                        pink_Decision,
                        lost,
                    ) = State.squaremove30(
                        teststate,
                        nextstate,
                        6,
                        15,
                        currentPinkRow,
                        currentPinkCol,
                        r,
                        w,
                        7,
                        "Pink",
                        _Cost,
                        # pink_Cost,
                        pinkOver,
                        pink_Decision,
                        lost,
                    )

                if (currentGreenLightRow, currentGreenLightCol) == (1, 14):
                    if nextstate.board[currentGreenLightRow][
                        currentGreenLightCol
                    ] not in [2, 4, 8, 7, 1]:
                        nextstate.board[1][14] = 0
                    greenLightOver = False
                else:

                    (
                        _Cost,
                        # green_Cost,
                        nextstate,
                        greenLightOver,
                        currentGreenLightRow,
                        currentGreenLightCol,
                        green_Decision,
                        lost,
                    ) = State.squaremove30(
                        teststate,
                        nextstate,
                        6,
                        15,
                        currentGreenLightRow,
                        currentGreenLightCol,
                        r,
                        w,
                        6,
                        "Green",
                        _Cost,
                        # green_Cost,
                        greenLightOver,
                        green_Decision,
                        lost,
                    )

                if (currentOrangeRow, currentOrangeCol) == (1, 11):
                    if nextstate.board[currentOrangeRow][currentOrangeCol] not in [
                        2,
                        4,
                        7,
                        6,
                        1,
                    ]:
                        nextstate.board[1][11] = 0
                    orangeOver = False
                else:

                    (
                        _Cost,
                        # orange_Cost,
                        nextstate,
                        orangeOver,
                        currentOrangeRow,
                        currentOrangeCol,
                        orange_Decision,
                        lost,
                    ) = State.squaremove30(
                        teststate,
                        nextstate,
                        6,
                        15,
                        currentOrangeRow,
                        currentOrangeCol,
                        r,
                        w,
                        8,
                        "Orange",
                        _Cost,
                        orangeOver,
                        orange_Decision,
                        lost,
                    )

            if nextstate != state and not lost:
                nesxSteps.append(
                    State(
                        nextstate.board,
                        state,
                        cost=state.cost + _Cost,
                        visited_counter=nextstate.visited_counter,
                        changed_movement=nextstate.changed_movement,
                    )
                )
        # print(len(nesxSteps))
        # for nesxStep in nesxSteps:
        #     print("next", nesxStep.board)
        return nesxSteps
        # return nesxSteps, changed_movement
