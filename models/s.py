# import copy
# import numpy as np

# import algorithms
# import sys

# sys.setrecursionlimit(2000)
# ###########################################


# class State:
#     def __init__(
#         self, board=None, parent=None, cost=0, red_changed=False, red_visits=0
#     ):
#         self.board = board
#         self.parent = parent
#         self.goals = [(1, 1), (2, 2)]
#         self.cost = cost
#         # self.red_visits = red_visits
#         # self.red_changed = red_changed

#     # ----------------------------------------------------------------

#     def set_Board(self, board):
#         self.board = board

#     # ----------------------------------------------------------------

#     def get_Board(self):
#         return self.board

#     # ----------------------------------------------------------------

#     def __eq__(self, other):
#         # مقارنة الكائنات بناءً على المصفوفة board فقط
#         if isinstance(other, State):
#             return np.array_equal(self.board, other.board)
#         return False

#     # ----------------------------------------------------------------

#     def __lt__(self, other):
#         # Compare based on heuristic values (or other criteria)
#         if isinstance(other, State):
#             return algorithms.advanced_heuristic(self) < algorithms.advanced_heuristic(
#                 other
#             )
#         return False

#     # ----------------------------------------------------------------

#     def __hash__(self):
#         # تحويل المصفوفة numpy.ndarray إلى tuple بحيث تصبح قابلة للتجزئة
#         return hash(tuple(map(tuple, self.board)))

#     # ----------------------------------------------------------------
#     def squaremove(
#         teststate,
#         nextstate,
#         row,
#         column,
#         currentColorRow,
#         currentColorCol,
#         r,
#         w,
#         # colorOver,
#         squareValue,
#         color,
#         color_Cost,
#     ):
#         # color_Cost = 0
#         color_conditions = {
#             "Red": [1, 2, 6, 7, 8],
#             "Blue": [1, 4, 6, 7, 8],
#             "Orange": [2, 6, 7, 4, 1],
#             "Green": [2, 4, 7, 8, 1],
#             "Pink": [2, 6, 4, 8, 1],
#         }

#         nextCondation = color_conditions.get(color, [])

#         if (
#             teststate.board[currentColorRow + r][currentColorCol + w]
#             not in nextCondation
#         ):
#             if (
#                 nextstate.board[currentColorRow + r][currentColorCol + w]
#                 not in nextCondation
#                 # and (currentColorRow, currentColorCol) != (3, 4)
#                 and (row < currentColorRow < row)
#                 and (row < currentColorCol < column)
#             ):
#                 nextstate.board[currentColorRow][currentColorCol] = 0
#                 currentColorRow += r
#                 currentColorCol += w
#                 nextstate.board[currentColorRow][currentColorCol] = squareValue

#                 color_Cost += abs(r) + abs(w)

#         #     else:
#         #         colorOver = False
#         # else:
#         #     colorOver = False
#         return color_Cost, nextstate

#     def next_State(
#         state,
#         currentBlue,
#         currentRed,
#         currentGreenLight,
#         currentPink,
#         currentOrange,
#     ):
#         print(currentBlue)
#         # تأكد من أن المتغير state هو كائن من نوع State
#         if not isinstance(state, State):
#             raise TypeError(
#                 "The 'state' parameter must be an instance of the 'State' class."
#             )
#         # cost = 0
#         nesxSteps = []
#         stepsList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#         teststate = copy.deepcopy(state)
#         print("teststate", teststate.board)
#         for r, w in stepsList:

#             nextstate = copy.deepcopy(state)
#             blueOver = True
#             redOver = True
#             orangeOver = True
#             greenLightOver = True
#             pinkOver = True
#             if currentRed != [3, 4]:
#                 currentRedRow, currentRedCol = currentRed
#             else:
#                 currentRedRow, currentRedCol = 3, 4

#             if currentBlue != [2, 1]:
#                 currentBlueRow, currentBlueCol = currentBlue
#             else:
#                 currentBlueRow, currentBlueCol = 2, 1

#             if currentPink != [3, 2]:
#                 currentPinkRow, currentPinkCol = currentPink
#             else:
#                 currentPinkRow, currentPinkCol = 3, 2

#             if currentOrange != [1, 5]:
#                 currentOrangeRow, currentOrangeCol = currentOrange
#             else:
#                 currentOrangeRow, currentOrangeCol = 1, 5
#             if currentGreenLight != [3, 7]:
#                 currentGreenLightRow, currentGreenLightCol = currentGreenLight
#             else:
#                 currentGreenLightRow, currentGreenLightCol = 3, 7

#             red_Cost = 0
#             blue_Cost = 0
#             orange_Cost = 0
#             pink_Cost = 0
#             greenLight_Cost = 0

#             while redOver or blueOver or orangeOver or greenLightOver or pinkOver:
#                 # حركة للمكعب الأحمر
#                 if (currentRedRow, currentRedCol) == (3, 4):
#                     nextstate.board[3][4] = 0
#                     redOver = False
#                 else:
#                     red_Cost, nextstate = State.squaremove(
#                         teststate,
#                         nextstate,
#                         4,
#                         8,
#                         currentRedRow,
#                         currentRedCol,
#                         r,
#                         w,
#                         4,
#                         "Red",
#                         red_Cost,
#                     )
#                     redOver = False
#                     # if teststate.board[currentRedRow + r][currentRedCol + w] not in [
#                     #     2,
#                     #     6,
#                     #     7,
#                     #     8,
#                     #     1,
#                     # ]:
#                     #     if (
#                     #         nextstate.board[currentRedRow + r][currentRedCol + w]
#                     #         not in [
#                     #             2,
#                     #             6,
#                     #             7,
#                     #             8,
#                     #             1,
#                     #         ]
#                     #         and (currentRedRow, currentRedCol) != (3, 4)
#                     #         and (0 < currentRedRow < 4)
#                     #         and (0 < currentRedCol < 8)
#                     #     ):
#                     #         nextstate.board[currentRedRow][currentRedCol] = 0
#                     #         currentRedRow += r
#                     #         currentRedCol += w
#                     #         nextstate.board[currentRedRow][currentRedCol] = 4

#                     #         red_Cost += abs(r) + abs(w)

#                     #     else:
#                     #         redOver = False
#                     # else:
#                     #     redOver = False
#                 # حركة للمكعب الأزرق
#                 if (currentBlueRow, currentBlueCol) == (2, 1):
#                     nextstate.board[2][1] = 0
#                     blueOver = False
#                 else:
#                     if teststate.board[currentBlueRow + r][currentBlueCol + w] not in [
#                         4,
#                         6,
#                         7,
#                         8,
#                         1,
#                     ]:
#                         if (
#                             nextstate.board[currentBlueRow + r][currentBlueCol + w]
#                             not in [
#                                 4,
#                                 6,
#                                 7,
#                                 8,
#                                 1,
#                             ]
#                             and (currentBlueRow, currentBlueCol) != (2, 1)
#                             and (0 < currentBlueRow < 4)
#                             and (0 < currentBlueCol < 8)
#                         ):
#                             nextstate.board[currentBlueRow][currentBlueCol] = 0
#                             # if (currentBlueRow, currentBlueCol) != (2, 1):
#                             currentBlueRow += r
#                             currentBlueCol += w
#                             nextstate.board[currentBlueRow][currentBlueCol] = 2

#                             blue_Cost += abs(r) + abs(w)

#                         else:
#                             blueOver = False
#                     else:
#                         blueOver = False

#                 if (currentPinkRow, currentPinkCol) == (3, 2):
#                     nextstate.board[3][2] = 0
#                     pinkOver = False
#                 else:
#                     if teststate.board[currentPinkRow + r][currentPinkCol + w] not in [
#                         2,
#                         4,
#                         6,
#                         8,
#                         1,
#                     ]:
#                         if (
#                             nextstate.board[currentPinkRow + r][currentPinkCol + w]
#                             not in [
#                                 2,
#                                 4,
#                                 6,
#                                 8,
#                                 1,
#                             ]
#                             and (currentPinkRow, currentPinkCol) != (3, 2)
#                             and (0 < currentPinkRow < 4)
#                             and (0 < currentPinkCol < 8)
#                         ):

#                             # print("currentPinkRow", currentPinkRow)
#                             nextstate.board[currentPinkRow][currentPinkCol] = 0
#                             # if (currentPinkRow, currentPinkCol) != (3, 2):
#                             currentPinkRow += r
#                             currentPinkCol += w
#                             nextstate.board[currentPinkRow][currentPinkCol] = 7

#                             pink_Cost += abs(r) + abs(w)

#                         else:
#                             pinkOver = False
#                     else:
#                         pinkOver = False
#                 if (currentOrangeRow, currentOrangeCol) == (1, 5):
#                     nextstate.board[1][5] = 0
#                     orangeOver = False
#                 else:
#                     if teststate.board[currentOrangeRow + r][
#                         currentOrangeCol + w
#                     ] not in [
#                         2,
#                         6,
#                         7,
#                         8,
#                         1,
#                     ]:
#                         if (
#                             nextstate.board[currentOrangeRow + r][currentOrangeCol + w]
#                             not in [
#                                 2,
#                                 6,
#                                 7,
#                                 8,
#                                 1,
#                             ]
#                             and (
#                                 currentOrangeRow,
#                                 currentOrangeCol,
#                             )
#                             != (
#                                 1,
#                                 5,
#                             )
#                             and (0 < currentOrangeRow < 4)
#                             and (0 < currentOrangeCol < 8)
#                         ):

#                             nextstate.board[currentOrangeRow][currentOrangeCol] = 0
#                             # if (currentOrangeRow, currentOrangeCol) != (1, 5):
#                             currentOrangeRow += r
#                             currentOrangeCol += w
#                             nextstate.board[currentOrangeRow][currentOrangeCol] = 8

#                             orange_Cost += abs(r) + abs(w)

#                         else:
#                             orangeOver = False
#                     else:
#                         orangeOver = False
#                 if (currentGreenLightRow, currentGreenLightCol) == (3, 7):
#                     nextstate.board[3][7] = 0
#                     greenLightOver = False
#                 else:
#                     if teststate.board[currentGreenLightRow + r][
#                         currentGreenLightCol + w
#                     ] not in [2, 4, 7, 8, 1]:
#                         if (
#                             nextstate.board[currentGreenLightRow + r][
#                                 currentGreenLightCol + w
#                             ]
#                             not in [
#                                 2,
#                                 4,
#                                 1,
#                                 7,
#                                 8,
#                             ]
#                             and (
#                                 currentGreenLightRow,
#                                 currentGreenLightCol,
#                             )
#                             != (
#                                 3,
#                                 7,
#                             )
#                             and (0 < currentGreenLightRow < 4)
#                             and (0 < currentGreenLightCol < 8)
#                         ):
#                             nextstate.board[currentGreenLightRow][
#                                 currentGreenLightCol
#                             ] = 0
#                             if (currentGreenLightRow, currentGreenLightCol) != (3, 7):
#                                 currentGreenLightRow += r
#                                 currentGreenLightCol += w
#                                 nextstate.board[currentGreenLightRow][
#                                     currentGreenLightCol
#                                 ] = 6

#                             greenLight_Cost += abs(r) + abs(w)

#                         else:
#                             greenLightOver = False
#                     else:
#                         greenLightOver = False

#                 # teststate = copy.deepcopy(nextstate)
#             if nextstate != state:
#                 nesxSteps.append(
#                     State(
#                         nextstate.board,
#                         state,
#                         cost=state.cost
#                         + blue_Cost
#                         + red_Cost
#                         + pink_Cost
#                         + greenLight_Cost
#                         + orange_Cost,
#                     )
#                 )
#         print(len(nesxSteps))
#         for nesxStep in nesxSteps:
#             print("next", nesxStep.board)
#         return nesxSteps

#     # ----------------------------------------------------------------

#     # def next_State2(
#     #     state,
#     #     currentBlue,
#     #     currentRed,
#     #     currentGreenLight,
#     #     currentPink,
#     #     currentOrange,
#     # ):

#     #     if not isinstance(state, State):
#     #         raise TypeError(
#     #             "The 'state' parameter must be an instance of the 'State' class."
#     #         )

#     #     nesxSteps = []
#     #     stepsList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#     #     teststate = copy.deepcopy(state)
#     #     print("teststate", teststate.board)
#     #     for r, w in stepsList:

#     #         nextstate = copy.deepcopy(state)
#     #         # teststate = copy.deepcopy(state)
#     #         blueOver = True
#     #         redOver = True
#     #         orangeOver = True
#     #         greenLightOver = True
#     #         pinkOver = True
#     #         if currentRed != [4, 5]:
#     #             currentRedRow, currentRedCol = currentRed
#     #         else:
#     #             currentRedRow, currentRedCol = 4, 5
#     #         # print(currentRedRow)
#     #         if currentBlue != [4, 8]:
#     #             currentBlueRow, currentBlueCol = currentBlue
#     #         else:
#     #             currentBlueRow, currentBlueCol = 4, 8

#     #         if currentPink != [1, 7]:
#     #             currentPinkRow, currentPinkCol = currentPink
#     #         else:
#     #             currentPinkRow, currentPinkCol = 1, 7

#     #         if currentOrange != [1, 11]:
#     #             currentOrangeRow, currentOrangeCol = currentOrange
#     #         else:
#     #             currentOrangeRow, currentOrangeCol = 1, 11
#     #         if currentGreenLight != [1, 14]:
#     #             currentGreenLightRow, currentGreenLightCol = currentGreenLight
#     #         else:
#     #             currentGreenLightRow, currentGreenLightCol = 1, 14
#     #         red_Cost = 0
#     #         blue_Cost = 0
#     #         orange_Cost = 0
#     #         pink_Cost = 0
#     #         greenLight_Cost = 0

#     #         while redOver or blueOver or orangeOver or greenLightOver or pinkOver:
#     #             # حركة للمكعب الأحمر
#     #             if (currentRedRow, currentRedCol) == (4, 5):
#     #                 if nextstate.board[currentRedRow][currentRedCol] not in [
#     #                     2,
#     #                     6,
#     #                     7,
#     #                     8,
#     #                 ]:
#     #                     nextstate.board[4][5] = 0

#     #                 redOver = False
#     #             else:

#     #                 if teststate.board[currentRedRow + r][currentRedCol + w] not in [
#     #                     1,
#     #                     2,
#     #                     6,
#     #                     7,
#     #                     8,
#     #                 ]:

#     #                     if (
#     #                         nextstate.board[currentRedRow + r][currentRedCol + w]
#     #                         not in [
#     #                             1,
#     #                             2,
#     #                             6,
#     #                             7,
#     #                             8,
#     #                         ]
#     #                         and (currentRedRow, currentRedCol) != (4, 5)
#     #                         and (0 < currentRedRow < 5)
#     #                         and (0 < currentRedCol < 15)
#     #                     ):

#     #                         nextstate.board[currentRedRow][currentRedCol] = 0
#     #                         if (currentRedRow, currentRedCol) != (4, 5):
#     #                             currentRedRow += r
#     #                             currentRedCol += w
#     #                             nextstate.board[currentRedRow][currentRedCol] = 4

#     #                         red_Cost += abs(r) + abs(w)

#     #                     else:
#     #                         redOver = False

#     #                 else:
#     #                     redOver = False
#     #             # حركة للمكعب الأزرق
#     #             if (currentBlueRow, currentBlueCol) == (4, 8):
#     #                 if nextstate.board[currentBlueRow][currentBlueCol] not in [
#     #                     4,
#     #                     6,
#     #                     7,
#     #                     8,
#     #                 ]:
#     #                     nextstate.board[4][8] = 0
#     #                 blueOver = False
#     #             else:
#     #                 if teststate.board[currentBlueRow + r][currentBlueCol + w] not in [
#     #                     1,
#     #                     4,
#     #                     6,
#     #                     7,
#     #                     8,
#     #                 ]:
#     #                     if (
#     #                         nextstate.board[currentBlueRow + r][currentBlueCol + w]
#     #                         not in [
#     #                             1,
#     #                             4,
#     #                             6,
#     #                             7,
#     #                             8,
#     #                         ]
#     #                         and (currentBlueRow, currentBlueCol) != (4, 8)
#     #                         and (0 < currentBlueRow < 5)
#     #                         and (0 < currentBlueCol < 15)
#     #                     ):
#     #                         nextstate.board[currentBlueRow][currentBlueCol] = 0
#     #                         if (currentBlueRow, currentBlueCol) != (4, 8):
#     #                             currentBlueRow += r
#     #                             currentBlueCol += w
#     #                             nextstate.board[currentBlueRow][currentBlueCol] = 2

#     #                         blue_Cost += abs(r) + abs(w)

#     #                     else:
#     #                         blueOver = False
#     #                 else:
#     #                     blueOver = False
#     #             if (currentPinkRow, currentPinkCol) == (1, 7):
#     #                 if nextstate.board[currentPinkRow][currentPinkCol] not in [
#     #                     2,
#     #                     4,
#     #                     6,
#     #                     8,
#     #                 ]:
#     #                     nextstate.board[1][7] = 0

#     #                 pinkOver = False
#     #             else:
#     #                 if teststate.board[currentPinkRow + r][currentPinkCol + w] not in [
#     #                     1,
#     #                     2,
#     #                     4,
#     #                     6,
#     #                     8,
#     #                 ]:
#     #                     if (
#     #                         nextstate.board[currentPinkRow + r][currentPinkCol + w]
#     #                         not in [
#     #                             1,
#     #                             2,
#     #                             4,
#     #                             6,
#     #                             8,
#     #                         ]
#     #                         and (currentPinkRow, currentPinkCol) != (1, 7)
#     #                         and (0 < currentPinkRow < 5)
#     #                         and (0 < currentPinkCol < 15)
#     #                     ):

#     #                         nextstate.board[currentPinkRow][currentPinkCol] = 0
#     #                         if (currentPinkRow, currentPinkCol) != (1, 7):
#     #                             currentPinkRow += r
#     #                             currentPinkCol += w
#     #                             nextstate.board[currentPinkRow][currentPinkCol] = 7

#     #                         pink_Cost += abs(r) + abs(w)

#     #                     else:
#     #                         pinkOver = False
#     #                 else:
#     #                     pinkOver = False
#     #             if (currentOrangeRow, currentOrangeCol) == (1, 11):
#     #                 if nextstate.board[currentOrangeRow][currentOrangeCol] not in [
#     #                     2,
#     #                     4,
#     #                     6,
#     #                     7,
#     #                 ]:
#     #                     nextstate.board[1][11] = 0

#     #                 orangeOver = False
#     #             else:
#     #                 if teststate.board[currentOrangeRow + r][
#     #                     currentOrangeCol + w
#     #                 ] not in [
#     #                     1,
#     #                     2,
#     #                     4,
#     #                     6,
#     #                     7,
#     #                 ]:
#     #                     if (
#     #                         nextstate.board[currentOrangeRow + r][currentOrangeCol + w]
#     #                         not in [
#     #                             1,
#     #                             2,
#     #                             4,
#     #                             6,
#     #                             7,
#     #                         ]
#     #                         and (
#     #                             currentOrangeRow,
#     #                             currentOrangeCol,
#     #                         )
#     #                         != (
#     #                             1,
#     #                             11,
#     #                         )
#     #                         and (0 < currentOrangeRow < 5)
#     #                         and (0 < currentOrangeCol < 15)
#     #                     ):

#     #                         nextstate.board[currentOrangeRow][currentOrangeCol] = 0
#     #                         if (currentOrangeRow, currentOrangeCol) != (1, 11):
#     #                             currentOrangeRow += r
#     #                             currentOrangeCol += w
#     #                             nextstate.board[currentOrangeRow][currentOrangeCol] = 8

#     #                         orange_Cost += abs(r) + abs(w)

#     #                     else:
#     #                         orangeOver = False
#     #                 else:
#     #                     orangeOver = False
#     #             if (currentGreenLightRow, currentGreenLightCol) == (1, 14):
#     #                 if nextstate.board[currentOrangeRow][currentOrangeCol] not in [
#     #                     2,
#     #                     4,
#     #                     7,
#     #                     8,
#     #                 ]:
#     #                     nextstate.board[1][14] = 0

#     #                 greenLightOver = False
#     #             else:
#     #                 if teststate.board[currentGreenLightRow + r][
#     #                     currentGreenLightCol + w
#     #                 ] not in [2, 4, 7, 8, 1]:
#     #                     if (
#     #                         nextstate.board[currentGreenLightRow + r][
#     #                             currentGreenLightCol + w
#     #                         ]
#     #                         not in [
#     #                             2,
#     #                             4,
#     #                             1,
#     #                             7,
#     #                             8,
#     #                         ]
#     #                         and (
#     #                             currentGreenLightRow,
#     #                             currentGreenLightCol,
#     #                         )
#     #                         != (1, 14)
#     #                         and (0 < currentGreenLightRow < 5)
#     #                         and (0 < currentGreenLightCol < 15)
#     #                     ):
#     #                         nextstate.board[currentGreenLightRow][
#     #                             currentGreenLightCol
#     #                         ] = 0
#     #                         if (currentGreenLightRow, currentGreenLightCol) != (1, 14):
#     #                             currentGreenLightRow += r
#     #                             currentGreenLightCol += w
#     #                             nextstate.board[currentGreenLightRow][
#     #                                 currentGreenLightCol
#     #                             ] = 6

#     #                         greenLight_Cost += abs(r) + abs(w)

#     #                     else:
#     #                         greenLightOver = False
#     #                 else:
#     #                     greenLightOver = False

#     #             # teststate = copy.deepcopy(nextstate)
#     #         if nextstate != state:
#     #             nesxSteps.append(
#     #                 State(
#     #                     nextstate.board,
#     #                     state,
#     #                     cost=state.cost
#     #                     + blue_Cost
#     #                     + red_Cost
#     #                     + pink_Cost
#     #                     + greenLight_Cost
#     #                     + orange_Cost,
#     #                 )
#     #             )
#     #     print(len(nesxSteps))
#     #     for nesxStep in nesxSteps:
#     #         print("next", nesxStep.board)
#     #     return nesxSteps

#     # ----------------------------------------------------------------

#     def next_State1(
#         state,
#         currentBlue,
#         currentRed,
#         # currentGreenLight,
#         # currentPink,
#         # currentOrange,
#     ):
#         # print(currentBlue)
#         # تأكد من أن المتغير state هو كائن من نوع State
#         if not isinstance(state, State):
#             raise TypeError(
#                 "The 'state' parameter must be an instance of the 'State' class."
#             )
#         # cost = 0
#         nesxSteps = []
#         stepsList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#         teststate = copy.deepcopy(state)
#         # print("teststate", teststate.board)
#         for r, w in stepsList:
#             # cost += 1
#             nextstate = copy.deepcopy(state)
#             # teststate = copy.deepcopy(state)
#             blueOver = True
#             redOver = True
#             if currentRed != [3, 5]:
#                 currentRedRow, currentRedCol = currentRed
#             else:
#                 currentRedRow, currentRedCol = 3, 5
#             # print(currentRedRow)
#             if currentBlue != [2, 6]:
#                 currentBlueRow, currentBlueCol = currentBlue
#             else:
#                 currentBlueRow, currentBlueCol = 2, 6

#             red_Cost = 0
#             blue_Cost = 0

#             while redOver or blueOver:
#                 # حركة للمكعب الأحمر
#                 if (currentRedRow, currentRedCol) == (3, 5):
#                     nextstate.board[3][5] = 0
#                     redOver = False
#                 else:

#                     if teststate.board[currentRedRow + r][currentRedCol + w] not in [
#                         2,
#                         6,
#                         7,
#                         8,
#                         1,
#                     ]:

#                         if (
#                             nextstate.board[currentRedRow + r][currentRedCol + w]
#                             not in [
#                                 2,
#                                 6,
#                                 7,
#                                 8,
#                                 1,
#                             ]
#                             and (currentRedRow, currentRedCol) != (3, 5)
#                             and (0 < currentRedRow < 7)
#                             and (0 < currentRedCol < 11)
#                         ):

#                             nextstate.board[currentRedRow][currentRedCol] = 0
#                             if (currentRedRow, currentRedCol) != (3, 5):
#                                 currentRedRow += r
#                                 currentRedCol += w
#                                 nextstate.board[currentRedRow][currentRedCol] = 4

#                             red_Cost += abs(r) + abs(w)

#                         else:
#                             redOver = False

#                     else:
#                         redOver = False
#                 # حركة للمكعب الأزرق
#                 if (currentBlueRow, currentBlueCol) == (2, 6):
#                     nextstate.board[2][6] = 0
#                     blueOver = False
#                 else:
#                     if teststate.board[currentBlueRow + r][currentBlueCol + w] not in [
#                         4,
#                         6,
#                         7,
#                         8,
#                         1,
#                     ]:
#                         if (
#                             nextstate.board[currentBlueRow + r][currentBlueCol + w]
#                             not in [
#                                 4,
#                                 6,
#                                 7,
#                                 8,
#                                 1,
#                             ]
#                             and (currentBlueRow, currentBlueCol) != (2, 6)
#                             and (0 < currentBlueRow < 7)
#                             and (0 < currentBlueCol < 11)
#                         ):
#                             nextstate.board[currentBlueRow][currentBlueCol] = 0
#                             if (currentBlueRow, currentBlueCol) != (2, 6):
#                                 currentBlueRow += r
#                                 currentBlueCol += w
#                                 nextstate.board[currentBlueRow][currentBlueCol] = 2

#                             blue_Cost += abs(r) + abs(w)

#                         else:
#                             blueOver = False
#                     else:
#                         blueOver = False

#             if nextstate != state:
#                 nesxSteps.append(
#                     State(
#                         nextstate.board,
#                         state,
#                         cost=state.cost + blue_Cost + red_Cost,
#                     )
#                 )
#         # print(len(nesxSteps))
#         # for nesxStep in nesxSteps:
#         #     print("next", nesxStep.board)
#         return nesxSteps

#     # ----------------------------------------------------------------

#     def next_State2(
#         state,
#         currentBlue,
#         currentRed,
#         currentGreenLight,
#         currentPink,
#         currentOrange,
#         # redGoalCount,
#     ):
#         global r
#         if not isinstance(state, State):
#             raise TypeError(
#                 "The 'state' parameter must be an instance of the 'State' class."
#             )
#         nesxSteps = []
#         stepsList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#         teststate = copy.deepcopy(state)
#         # print(teststate.board)

#         for r, w in stepsList:

#             lost = False
#             nextstate = copy.deepcopy(state)
#             blueOver = True
#             redOver = True
#             orangeOver = True
#             greenLightOver = True
#             pinkOver = True

#             if currentRed != [4, 5]:
#                 currentRedRow, currentRedCol = currentRed
#             else:
#                 currentRedRow, currentRedCol = 4, 5

#             if currentBlue != [4, 8]:
#                 currentBlueRow, currentBlueCol = currentBlue
#             else:
#                 currentBlueRow, currentBlueCol = 4, 8

#             if currentPink != [1, 7]:
#                 currentPinkRow, currentPinkCol = currentPink
#             else:
#                 currentPinkRow, currentPinkCol = 1, 7

#             if currentOrange != [1, 11]:
#                 currentOrangeRow, currentOrangeCol = currentOrange
#             else:
#                 currentOrangeRow, currentOrangeCol = 1, 11

#             if currentGreenLight != [1, 14]:
#                 currentGreenLightRow, currentGreenLightCol = currentGreenLight
#             else:
#                 currentGreenLightRow, currentGreenLightCol = 1, 14

#             red_Cost = 0
#             blue_Cost = 0
#             orange_Cost = 0
#             pink_Cost = 0
#             greenLight_Cost = 0

#             pA = True
#             rA = True
#             bA = True
#             gA = True
#             oA = True

#             # print(nextstate.red_visits)
#             while redOver or blueOver or orangeOver or greenLightOver or pinkOver:
#                 # حركة للمكعب الأحمر
#                 if (currentRedRow, currentRedCol) == (4, 5):
#                     # if nextstate.red_visits == 2:
#                     if nextstate.board[currentRedRow][currentRedCol] not in [
#                         2,
#                         7,
#                         6,
#                         8,
#                     ]:
#                         nextstate.board[4][5] = 0
#                     redOver = False

#                     # if not state.red_changed:  # إذا لم يغير المربع الأحمر موقعه
#                     #     redOver = False
#                     # else:
#                     #     nextstate.red_visits += 1
#                     #     nextstate.red_changed = False

#                     # if state.red_changed:
#                     #     if state.red_visits == 1:
#                     #         nextstate.red_visits += 2
#                     #     else:
#                     #         nextstate.red_visits += 1
#                     #     nextstate.red_changed = False

#                     # redOver = False

#                 else:
#                     if (
#                         teststate.board[currentRedRow + r][currentRedCol + w]
#                         not in [
#                             2,
#                             6,
#                             7,
#                             8,
#                             1,
#                         ]
#                         or rA == False
#                     ):
#                         rA = False
#                         # if redGoalCount == 2:
#                         if (
#                             nextstate.board[currentRedRow + r][currentRedCol + w]
#                             not in [
#                                 2,
#                                 6,
#                                 7,
#                                 8,
#                                 1,
#                             ]
#                             # and redGoalCount <= 2
#                             and (
#                                 (currentRedRow, currentRedCol)
#                                 != (4, 5)
#                                 # nextstate.red_visits
#                                 # != 2
#                             )
#                             and (0 < currentRedRow < 5)
#                             and (0 < currentRedCol < 15)
#                         ):

#                             nextstate.board[currentRedRow][currentRedCol] = 0
#                             if (currentRedRow, currentRedCol) != (4, 5):
#                                 currentRedRow += r
#                                 currentRedCol += w
#                                 # redOver = False
#                                 nextstate.board[currentRedRow][currentRedCol] = 4

#                             # nextstate.red_changed = True

#                             if (currentRedRow, currentRedCol) == (5, 8):

#                                 print("Red cube reached (5, 8). Exiting while loop.")
#                                 lost = True
#                                 redOver = False
#                                 break
#                             red_Cost += abs(r) + abs(w)

#                         else:
#                             redOver = False

#                     else:
#                         redOver = False
#                 # حركة للمكعب الأزرق
#                 if (currentBlueRow, currentBlueCol) == (4, 8):
#                     if nextstate.board[currentBlueRow][currentBlueCol] not in [
#                         7,
#                         4,
#                         6,
#                         8,
#                     ]:
#                         nextstate.board[4][8] = 0
#                     blueOver = False
#                 else:
#                     if (
#                         teststate.board[currentBlueRow + r][currentBlueCol + w]
#                         not in [
#                             4,
#                             6,
#                             7,
#                             8,
#                             1,
#                         ]
#                         or bA == False
#                     ):
#                         bA = False
#                         if (
#                             nextstate.board[currentBlueRow + r][currentBlueCol + w]
#                             not in [
#                                 4,
#                                 6,
#                                 7,
#                                 8,
#                                 1,
#                             ]
#                             and (currentBlueRow, currentBlueCol) != (4, 8)
#                             and (0 < currentBlueRow < 5)
#                             and (0 < currentBlueCol < 15)
#                         ):
#                             nextstate.board[currentBlueRow][currentBlueCol] = 0
#                             if (currentBlueRow, currentBlueCol) != (4, 8):
#                                 currentBlueRow += r
#                                 currentBlueCol += w
#                                 nextstate.board[currentBlueRow][currentBlueCol] = 2

#                                 # تحقق إذا وصل المكعب الأزرق إلى الإحداثي (5, 8)
#                                 if (currentBlueRow, currentBlueCol) == (5, 8):
#                                     print(
#                                         "Blue cube reached (5, 8). Exiting while loop."
#                                     )
#                                     lost = True
#                                     blueOver = False
#                                     break

#                             blue_Cost += abs(r) + abs(w)

#                         else:
#                             blueOver = False
#                     else:
#                         blueOver = False

#                 if (currentPinkRow, currentPinkCol) == (1, 7):
#                     if nextstate.board[currentPinkRow][currentPinkCol] not in [
#                         2,
#                         4,
#                         8,
#                         6,
#                     ]:
#                         nextstate.board[1][7] = 0
#                     pinkOver = False
#                 else:
#                     if (
#                         teststate.board[currentPinkRow + r][currentPinkCol + w]
#                         not in [2, 4, 6, 8, 1]
#                         or pA == False
#                     ):
#                         pA = False
#                         if (
#                             nextstate.board[currentPinkRow + r][currentPinkCol + w]
#                             not in [
#                                 2,
#                                 4,
#                                 1,
#                                 6,
#                                 8,
#                             ]
#                             and (
#                                 currentPinkRow,
#                                 currentPinkCol,
#                             )
#                             != (1, 7)
#                             and (0 < currentPinkRow < 5)
#                             and (0 < currentPinkCol < 15)
#                         ):
#                             nextstate.board[currentPinkRow][currentPinkCol] = 0
#                             if (currentPinkRow, currentPinkCol) != (1, 7):
#                                 currentPinkRow += r
#                                 currentPinkCol += w
#                                 nextstate.board[currentPinkRow][currentPinkCol] = 7

#                                 if (currentPinkRow, currentPinkCol) == (
#                                     5,
#                                     8,
#                                 ):
#                                     print(
#                                         "Pink cube reached (5, 8). Exiting while loop."
#                                     )
#                                     lost = True
#                                     pinkOver = False
#                                     break

#                             pink_Cost += abs(r) + abs(w)

#                         else:
#                             pinkOver = False
#                     else:
#                         pinkOver = False

#                 if (currentOrangeRow, currentOrangeCol) == (1, 11):
#                     if nextstate.board[currentOrangeRow][currentOrangeCol] not in [
#                         2,
#                         4,
#                         6,
#                         7,
#                     ]:
#                         nextstate.board[1][11] = 0
#                     orangeOver = False
#                 else:
#                     if (
#                         teststate.board[currentOrangeRow + r][currentOrangeCol + w]
#                         not in [
#                             2,
#                             6,
#                             7,
#                             4,
#                             1,
#                         ]
#                         or oA == False
#                     ):
#                         oA = False

#                         if (
#                             nextstate.board[currentOrangeRow + r][currentOrangeCol + w]
#                             not in [
#                                 2,
#                                 6,
#                                 7,
#                                 4,
#                                 1,
#                             ]
#                             and (
#                                 currentOrangeRow,
#                                 currentOrangeCol,
#                             )
#                             != (1, 11)
#                             and (0 < currentOrangeRow < 5)
#                             and (0 < currentOrangeCol < 15)
#                         ):

#                             if (currentOrangeRow, currentOrangeCol) != (1, 11):
#                                 nextstate.board[currentOrangeRow][currentOrangeCol] = 0
#                                 currentOrangeRow += r
#                                 currentOrangeCol += w
#                                 nextstate.board[currentOrangeRow][currentOrangeCol] = 8

#                                 if (currentOrangeRow, currentOrangeCol) == (5, 8):
#                                     print(
#                                         "Orange cube reached (5, 8). Exiting while loop."
#                                     )
#                                     lost = True
#                                     orangeOver = False
#                                     break
#                             else:
#                                 nextstate.board[currentOrangeRow][currentOrangeCol] = 0

#                             orange_Cost += abs(r) + abs(w)

#                         else:
#                             orangeOver = False
#                     else:
#                         orangeOver = False

#                 if (currentGreenLightRow, currentGreenLightCol) == (1, 14):
#                     if nextstate.board[currentGreenLightRow][
#                         currentGreenLightCol
#                     ] not in [2, 4, 8, 7]:
#                         nextstate.board[1][14] = 0
#                     greenLightOver = False
#                 else:
#                     if (
#                         teststate.board[currentGreenLightRow + r][
#                             currentGreenLightCol + w
#                         ]
#                         not in [2, 4, 7, 8, 1]
#                         or gA == False
#                     ):
#                         gA = False
#                         if (
#                             nextstate.board[currentGreenLightRow + r][
#                                 currentGreenLightCol + w
#                             ]
#                             not in [
#                                 2,
#                                 4,
#                                 1,
#                                 7,
#                                 8,
#                             ]
#                             and (
#                                 currentGreenLightRow,
#                                 currentGreenLightCol,
#                             )
#                             != (1, 14)
#                             and (0 < currentGreenLightRow < 5)
#                             and (0 < currentGreenLightCol < 15)
#                         ):
#                             nextstate.board[currentGreenLightRow][
#                                 currentGreenLightCol
#                             ] = 0
#                             if (currentGreenLightRow, currentGreenLightCol) != (1, 14):
#                                 currentGreenLightRow += r
#                                 currentGreenLightCol += w
#                                 nextstate.board[currentGreenLightRow][
#                                     currentGreenLightCol
#                                 ] = 6

#                                 if (currentGreenLightRow, currentGreenLightCol) == (
#                                     5,
#                                     8,
#                                 ):
#                                     print(
#                                         "Green cube reached (5, 8). Exiting while loop."
#                                     )
#                                     lost = True
#                                     greenLightOver = False
#                                     break

#                             greenLight_Cost += abs(r) + abs(w)

#                         else:
#                             greenLightOver = False
#                     else:
#                         greenLightOver = False

#             if nextstate != state and not lost:
#                 nesxSteps.append(
#                     State(
#                         nextstate.board,
#                         state,
#                         cost=state.cost
#                         + blue_Cost
#                         + red_Cost
#                         + pink_Cost
#                         + greenLight_Cost
#                         + orange_Cost,
#                         # red_visits=nextstate.red_visits,
#                         # red_changed=nextstate.red_changed,
#                     )
#                 )
#         # print(len(nesxSteps))
#         # for nesxStep in nesxSteps:
#         #     print("next", nesxStep.board)
#         return nesxSteps
