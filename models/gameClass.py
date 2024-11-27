import copy
import tkinter as tk
from matplotlib import patches
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
import random
import algorithms
from models.stateClass import State

###########################################


class Game:

    def __init__(self):
        self.hard_History = []
        self.easy_History = []
        self.window = tk.Tk()
        self.isStoped = False
        self.isBlue = False
        self.isRed = False
        self.isMoving = False
        self.isWin = False
        self.isLost = False

        self.goalSquare1 = patches.Rectangle(
            (1, 7), 1, 1, edgecolor="blue", facecolor="none", linewidth=3
        )
        self.goalSquare2 = patches.Rectangle(
            (5, 6), 1, 1, edgecolor="red", facecolor="none", linewidth=3
        )
        self.colors = {
            0: "white",
            1: "black",
            2: "blue",
            3: "#B3E0FF",
            4: "red",
            5: "#FFFFE0",
        }

        self.squaresList = np.array(
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [5, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
                [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        )

        self.lists = [
            np.array(
                [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1, 5, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 5, 1],
                ]
            ),
            np.array(
                [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1, 5, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 5, 1],
                ]
            ),
            np.array(
                [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 0, 0, 1, 5, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 5, 1],
                ]
            ),
        ]

        # self.goals = [
        #     (2, 5),
        #     (1, 1),
        # ]

        self.randomList = random.randint(0, 2)
        self.squaresList = copy.deepcopy(self.lists[self.randomList])
        self.squaresListHard = copy.deepcopy(self.lists[self.randomList])

        self.indices = np.argwhere(self.squaresList == 1)
        self.constantsSquares = [tuple(index) for index in self.indices]
        self.constantsSquaresPlusGoalSquare = [tuple(index) for index in self.indices]
        self.constantsSquaresPlusGoalSquare.append((2, 5))
        self.constantsSquaresPlusGoalSquare.append((1, 1))
        self.constantsSquaresPlusGoalSquare.append((0, 7))
        self.constantsSquares.append((0, 7))

        # print(self.constantsSquares)

        while True:
            self.randomRow = random.randint(0, 6)
            self.randomCol = random.randint(0, 7)
            if (
                self.randomRow,
                self.randomCol,
            ) not in self.constantsSquaresPlusGoalSquare:
                while True:
                    self.randomRowHard = random.randint(0, 6)
                    self.randomColHard = random.randint(0, 7)
                    if (
                        self.randomRowHard,
                        self.randomColHard,
                    ) not in self.constantsSquaresPlusGoalSquare and (
                        self.randomRowHard,
                        self.randomColHard,
                    ) != (
                        self.randomRow,
                        self.randomCol,
                    ):
                        break
                break

        self.redRowCheck = self.randomRowHard
        self.redColCheck = self.randomColHard
        self.blueRowCheck = self.randomRow
        self.blueColCheck = self.randomCol

        self.squaresList[self.randomRow][self.randomCol] = 2
        self.easyList = copy.deepcopy(self.squaresList)

        self.squaresListHard[self.randomRow][self.randomCol] = 2
        self.squaresListHard[self.randomRowHard][self.randomColHard] = 4

        self.state_Hard = State(self.squaresListHard)
        # self.hard_History.append(self.state_Hard.board)
        self.hardList = self.state_Hard.board

        self.state_Easy = State(self.squaresList)
        self.easy_History.append(self.state_Easy.board)
        self.easyList = self.state_Easy.board

        self.rows = len(self.hardList)
        self.cols = len(self.hardList[0])

        self.initialDirectionList1 = [
            (self.randomRow, self.randomCol + 1),
            (self.randomRow, self.randomCol - 1),
            (self.randomRow + 1, self.randomCol),
            (self.randomRow - 1, self.randomCol),
        ]
        self.initialDirectionList2 = [
            (self.randomRowHard, self.randomColHard + 1),
            (self.randomRowHard, self.randomColHard - 1),
            (self.randomRowHard + 1, self.randomColHard),
            (self.randomRowHard - 1, self.randomColHard),
        ]

        self.initialDirectionList12 = [
            (self.randomRow, self.randomCol + 1),
            (self.randomRow, self.randomCol - 1),
            (self.randomRow + 1, self.randomCol),
            (self.randomRow - 1, self.randomCol),
            (self.randomRowHard, self.randomColHard + 1),
            (self.randomRowHard, self.randomColHard - 1),
            (self.randomRowHard + 1, self.randomColHard),
            (self.randomRowHard - 1, self.randomColHard),
        ]

        self.blue_GreyToGreen_Easy()

        for r, w in self.initialDirectionList12:
            if (
                (r, w) not in self.constantsSquares
                and (0 <= r < 7 and 0 <= w < 8)
                and (r, w) != (self.randomRowHard, self.randomColHard)
                and (r, w) != (self.randomRow, self.randomCol)
            ):
                self.hardList[r][w] = 3

        self.fig, (self.ax1) = plt.subplots(figsize=(10, 10))

    # ----------------------------------------------------------------

    def environment(self):
        self.ax1.clear()
        self.fig.patch.set_facecolor("#FFFFE0")
        self.fig.canvas.mpl_connect("key_press_event", self.move)
        self.ax1.add_patch(self.goalSquare1)
        if self.level == "Hard":
            self.ax1.add_patch(self.goalSquare1)
            self.ax1.add_patch(self.goalSquare2)
        self.ax1.axis("off")

    # ----------------------------------------------------------------

    def draw(self):

        self.environment()
        if self.level == "Easy":
            if self.isWin == True:
                self.blue_GreenToGrey_Easy()
            for i in range(self.rows):
                for j in range(self.cols):
                    # الحصول على اللون المناسب للقيمة
                    color = self.colors[self.easyList[i][j]]
                    # رسم مستطيل ملون يمثل كل خلية
                    rect = patches.Rectangle(
                        (j, self.rows - i - 1),
                        1,
                        1,
                        linewidth=0,
                        edgecolor="black",
                        facecolor=color,
                    )
                    self.ax1.add_patch(rect)
                    self.ax1.add_patch(self.goalSquare1)

        else:

            if self.isBlue:
                # self.blue_GreenToGrey_Easy()  # عندما يصل المعب الأزرق الى هدفه يتم جعل المربعات المحيطة بيضاء
                self.blue_GreenToGrey_Hard()

                self.hardList[self.randomRow][self.randomCol] = 0
            if self.isRed:
                self.red_GreenToGrey()

                self.hardList[self.randomRowHard][self.randomColHard] = 0

            if (
                self.isStoped == True
            ):  # في حال توقفت الأحجار عن الحركة يتم تلون المربعات حولها باللون الأخضر
                # print("1" + str(self.hardList))
                if (self.randomRow, self.randomCol) != (1, 1):
                    self.blue_GreyToGreen_Hard()

                if (self.randomRowHard, self.randomColHard) != (2, 5):
                    self.red_GreyToGreen()

            if (self.randomRow, self.randomCol) != (1, 1):

                self.hardList[self.randomRow][self.randomCol] = 2

            else:
                self.hardList[self.randomRow][self.randomCol] = 0

            if (self.randomRowHard, self.randomColHard) != (2, 5):

                self.hardList[self.randomRowHard][self.randomColHard] = 4
            else:
                self.hardList[self.randomRowHard][self.randomColHard] = 0

            self.setSquaresColors()

        self.ax1.set_xlim(0, self.rows + 1)
        self.ax1.set_ylim(0, self.cols + 1)
        self.ax1.set_aspect("equal")

        if self.isRed:
            self.red_GreenToGrey()
            self.randomColHard = 0
            self.randomRowHard = 0
            self.hardList[self.randomRowHard][self.randomColHard] = 1
            self.goalSquare2 = patches.Rectangle(
                (5, 6), 1, 1, edgecolor="black", facecolor="none", linewidth=0
            )
            self.setSquaresColors()

        if self.isBlue:
            self.blue_GreenToGrey_Hard()
            self.randomCol = 0
            self.randomRow = 0
            self.hardList[self.randomRow][self.randomCol] = 1
            self.goalSquare1 = patches.Rectangle(
                (1, 7), 1, 1, edgecolor="black", facecolor="none", linewidth=0
            )
            self.setSquaresColors()

            if self.isWin == False:
                self.updateinitialDirectionList1()
                self.blue_GreyToGreen_Easy()

        self.hardList[0][0] = 1
        self.state_Hard.board[0][0] = 1

        self.hard_History.append(self.state_Hard)
        self.state_Hard = copy.deepcopy(self.state_Hard)
        self.hardList = self.state_Hard.board

        plt.draw()
        self.isStoped == False

    # ----------------------------------------------------------------

    def up(self):
        global currentposition, easyWinCheck
        easyWinCheck = False

        redStopped = True
        blueStopped = True
        if self.level == "Easy":
            while self.randomRow > 1 and (
                self.easyList[self.randomRow - 1][self.randomCol] == 0
                or self.easyList[self.randomRow - 1][self.randomCol] == 3
            ):

                self.easyList[self.randomRow][self.randomCol] = 0
                self.randomRow -= 1
                self.easyList[self.randomRow][self.randomCol] = 2
                self.easyList[self.easyList == 3] = 0
                self.updateinitialDirectionList1()
                self.blue_GreyToGreen_Easy()

                if self.checkWin() == True:

                    self.easyList[self.easyList == 3] = 0
                    easyWinCheck = True

                    # self.draw()
                    self.easy_History.append(self.state_Easy.board)
                    self.state_Easy = copy.deepcopy(self.state_Easy)
                    self.easyList = self.state_Easy.board
                    break
                if self.checkLose() == True:

                    self.easy_History.append(self.state_Easy.board)
                    self.state_Easy = copy.deepcopy(self.state_Easy)
                    self.easyList = self.state_Easy.board
                    break

                self.easy_History.append(self.state_Easy.board)
                self.state_Easy = copy.deepcopy(self.state_Easy)
                self.easyList = self.state_Easy.board

        else:
            while redStopped or blueStopped:
                if self.checkWin() == True:
                    self.goalSquare1 = patches.Rectangle(
                        (1, 7), 1, 1, edgecolor="black", facecolor="none", linewidth=0
                    )
                    self.goalSquare2 = patches.Rectangle(
                        (5, 6), 1, 1, edgecolor="black", facecolor="none", linewidth=0
                    )
                    break
                if self.checkLose() == True:
                    self.red_GreenToGrey()
                    self.blue_GreenToGrey_Hard
                    break
                self.hardList[self.randomRow][self.randomCol] = 0
                self.hardList[self.randomRowHard][self.randomColHard] = 0
                if (self.randomRowHard, self.randomColHard) != (2, 5):
                    (self.randomRow, self.randomCol)
                    if (
                        self.randomRowHard > 1
                        and (
                            self.hardList[self.randomRowHard - 1][self.randomColHard]
                            == 0
                            or self.hardList[self.randomRowHard - 1][self.randomColHard]
                            == 3
                        )
                        and (self.randomRowHard - 1, self.randomColHard)
                        != (self.randomRow, self.randomCol)
                    ):

                        self.randomRowHard -= 1
                        self.redRowCheck = self.randomRowHard
                        self.updateinitialDirectionList2()
                    else:
                        redStopped = False
                else:
                    redStopped = False
                    self.isRed = True

                if (self.randomRow, self.randomCol) != (1, 1):
                    if (
                        self.randomRow > 1
                        and (
                            self.hardList[self.randomRow - 1][self.randomCol] == 0
                            or self.hardList[self.randomRow - 1][self.randomCol] == 3
                        )
                        and (self.randomRow - 1, self.randomCol)
                        != (self.randomRowHard, self.randomColHard)
                    ):
                        self.randomRow -= 1
                        self.blueRowCheck = self.randomRow
                        self.updateinitialDirectionList1()
                    else:
                        blueStopped = False
                else:
                    blueStopped = False
                    self.isBlue = True

                self.hardList[self.randomRow][self.randomCol] = 2
                self.hardList[self.randomRowHard][self.randomColHard] = 4
                self.hardList[self.hardList == 3] = 0

                self.updateinitialDirectionList12()
        self.isStoped = True
        self.draw()
        self.isStoped = False

    def down(self):
        global currentposition
        redStopped = True
        blueStopped = True
        if self.level == "Easy":
            while (
                self.randomRow < 7
                and (self.randomRow + 1, self.randomCol) not in self.constantsSquares
            ):

                self.easyList[self.randomRow][self.randomCol] = 0
                self.randomRow += 1

                self.easyList[self.randomRow][self.randomCol] = 2
                self.easyList[self.easyList == 3] = 0
                self.updateinitialDirectionList1()
                self.blue_GreyToGreen_Easy()

                currentposition = (self.randomRow, self.randomCol)

                if self.checkWin() == True:

                    self.easyList[self.easyList == 3] = 0
                    self.isWin = True

                    self.easy_History.append(self.state_Easy.board)
                    self.state_Easy = copy.deepcopy(self.state_Easy)
                    self.easyList = self.state_Easy.board

                    break
                if self.checkLose() == True:

                    self.draw()
                    self.easy_History.append(self.state_Easy.board)
                    self.state_Easy = copy.deepcopy(self.state_Easy)
                    self.easyList = self.state_Easy.board
                    break

                self.easy_History.append(self.state_Easy.board)
                self.state_Easy = copy.deepcopy(self.state_Easy)
                self.easyList = self.state_Easy.board

        else:
            while redStopped or blueStopped:
                if self.checkWin() == True:
                    self.goalSquare1 = patches.Rectangle(
                        (1, 7), 1, 1, edgecolor="black", facecolor="none", linewidth=0
                    )
                    self.goalSquare2 = patches.Rectangle(
                        (5, 6), 1, 1, edgecolor="black", facecolor="none", linewidth=0
                    )
                    break

                if self.checkLose() == True:

                    self.red_GreenToGrey()
                    self.blue_GreenToGrey_Hard
                    break

                self.hardList[self.randomRow][self.randomCol] = 0
                self.hardList[self.randomRowHard][self.randomColHard] = 0
                if (self.randomRowHard, self.randomColHard) != (2, 5):
                    if (
                        self.randomRowHard < 7
                        and (
                            self.hardList[self.randomRowHard + 1][self.randomColHard]
                            != 1
                        )
                        and (self.randomRowHard + 1, self.randomColHard)
                        != (self.randomRow, self.randomCol)
                    ):

                        self.randomRowHard += 1
                        self.redRowCheck = self.randomRowHard
                        self.updateinitialDirectionList2()
                    else:
                        redStopped = False
                else:
                    redStopped = False
                    self.isRed = True

                if (self.randomRow, self.randomCol) != (1, 1):
                    if (
                        # self.randomRow < 6
                        # and (self.randomRow + 1, self.randomCol)
                        # not in self.constantsSquares
                        self.randomRow < 7
                        and (
                            self.hardList[self.randomRow + 1][self.randomCol] == 0
                            or self.hardList[self.randomRow + 1][self.randomCol] == 3
                        )
                        and (self.randomRow + 1, self.randomCol)
                        != (self.randomRowHard, self.randomColHard)
                    ):
                        # self.hard_History.append(self.state_Hard.board)
                        # self.state_Hard = copy.deepcopy(self.state_Hard)
                        # self.hardList = self.state_Hard.board
                        self.randomRow += 1
                        self.blueRowCheck = self.randomRow
                        self.updateinitialDirectionList1()
                    else:
                        blueStopped = False
                else:
                    blueStopped = False
                    self.isBlue = True

                self.hardList[self.randomRow][self.randomCol] = 2
                self.hardList[self.randomRowHard][self.randomColHard] = 4
                self.hardList[self.hardList == 3] = 0
                # self.draw()
                self.updateinitialDirectionList12()
        self.isStoped == True
        self.draw()
        self.isStoped == False

    def right(self):
        global currentposition
        redStopped = True
        blueStopped = True
        if self.level == "Easy":
            while (
                self.randomCol < 8
                and (self.randomRow, self.randomCol + 1) not in self.constantsSquares
            ):

                self.easyList[self.randomRow][self.randomCol] = 0
                self.randomCol += 1

                self.easyList[self.randomRow][self.randomCol] = 2
                self.easyList[self.easyList == 3] = 0
                self.updateinitialDirectionList1()
                self.blue_GreyToGreen_Easy()

                if self.checkWin() == True:

                    self.easyList[self.easyList == 3] = 0
                    self.isWin = True

                    self.draw()
                    self.easy_History.append(self.state_Easy.board)
                    self.state_Easy = copy.deepcopy(self.state_Easy)
                    self.easyList = self.state_Easy.board
                    break
                if self.checkLose() == True:
                    # self.draw()
                    # self.red_GreenToGrey()
                    # self.blue_GreenToGrey_Easy()

                    self.draw()
                    self.easy_History.append(self.state_Easy.board)
                    self.state_Easy = copy.deepcopy(self.state_Easy)
                    self.easyList = self.state_Easy.board
                    break

                self.easy_History.append(self.state_Easy.board)
                self.state_Easy = copy.deepcopy(self.state_Easy)
                self.easyList = self.state_Easy.board

        else:
            while redStopped or blueStopped:
                if self.checkWin() == True:
                    self.goalSquare1 = patches.Rectangle(
                        (1, 7), 1, 1, edgecolor="black", facecolor="none", linewidth=0
                    )
                    self.goalSquare2 = patches.Rectangle(
                        (5, 6), 1, 1, edgecolor="black", facecolor="none", linewidth=0
                    )
                    break

                if self.checkLose() == True:
                    # self.draw()
                    self.red_GreenToGrey()
                    self.blue_GreenToGrey_Hard

                    break

                self.hardList[self.randomRow][self.randomCol] = 0
                self.hardList[self.randomRowHard][self.randomColHard] = 0
                if (self.randomRowHard, self.randomColHard) != (2, 5):
                    if (
                        self.randomColHard < 8
                        and (
                            self.hardList[self.randomRowHard][self.randomColHard + 1]
                            == 0
                            or self.hardList[self.randomRowHard][self.randomColHard + 1]
                            == 3
                        )
                        and (self.randomRowHard, self.randomColHard + 1)
                        != (self.randomRow, self.randomCol)
                    ):
                        self.randomColHard += 1
                        self.redColCheck = self.randomColHard
                        self.updateinitialDirectionList2()
                    else:
                        redStopped = False
                else:
                    redStopped = False
                    self.isRed = True

                if (self.randomRow, self.randomCol) != (1, 1):
                    if (
                        self.randomCol < 8
                        and (
                            self.hardList[self.randomRow][self.randomCol + 1] == 0
                            or self.hardList[self.randomRow][self.randomCol + 1] == 3
                        )
                        and (self.randomRow, self.randomCol + 1)
                        != (self.randomRowHard, self.randomColHard)
                    ):
                        # self.hard_History.append(self.state_Hard.board)
                        # self.state_Hard = copy.deepcopy(self.state_Hard)
                        # self.hardList = self.state_Hard.board
                        self.randomCol += 1
                        self.blueColCheck = self.randomCol
                        self.updateinitialDirectionList1()
                    else:
                        blueStopped = False
                else:
                    blueStopped = False
                    self.isBlue = True

                self.hardList[self.randomRow][self.randomCol] = 2
                self.hardList[self.randomRowHard][self.randomColHard] = 4
                self.hardList[self.hardList == 3] = 0
                # self.draw()
                self.updateinitialDirectionList12()
        self.isStoped = True
        self.draw()
        self.isStoped = False

    def left(self):
        global currentposition
        redStopped = True
        blueStopped = True
        if self.level == "Easy":
            while (
                self.randomCol > 1
                and (self.randomRow, self.randomCol - 1) not in self.constantsSquares
            ):
                self.easyList[self.randomRow][self.randomCol] = 0
                self.randomCol -= 1

                self.easyList[self.randomRow][self.randomCol] = 2
                self.easyList[self.easyList == 3] = 0
                self.updateinitialDirectionList1()
                self.blue_GreyToGreen_Easy()

                if self.checkWin() == True:

                    self.easyList[self.easyList == 3] = 0
                    self.isWin = True

                    self.draw()
                    self.easy_History.append(self.state_Easy.board)
                    self.state_Easy = copy.deepcopy(self.state_Easy)
                    self.easyList = self.state_Easy.board
                    break
                if self.checkLose() == True:

                    self.draw()
                    self.easy_History.append(self.state_Easy.board)
                    self.state_Easy = copy.deepcopy(self.state_Easy)
                    self.easyList = self.state_Easy.board
                    break

                self.easy_History.append(self.state_Easy.board)
                self.state_Easy = copy.deepcopy(self.state_Easy)
                self.easyList = self.state_Easy.board

        else:
            while redStopped or blueStopped:
                if self.checkWin() == True:
                    self.goalSquare1 = patches.Rectangle(
                        (1, 7), 1, 1, edgecolor="black", facecolor="none", linewidth=0
                    )
                    self.goalSquare2 = patches.Rectangle(
                        (5, 6), 1, 1, edgecolor="black", facecolor="none", linewidth=0
                    )
                    break

                if self.checkLose() == True:
                    # self.draw()
                    self.red_GreenToGrey()
                    self.blue_GreenToGrey_Hard

                    break

                self.hardList[self.randomRow][self.randomCol] = 0
                self.hardList[self.randomRowHard][self.randomColHard] = 0
                if (self.randomRowHard, self.randomColHard) != (2, 5):
                    if (
                        self.randomColHard > 1
                        and (
                            self.hardList[self.randomRowHard][self.randomColHard - 1]
                            == 0
                            or self.hardList[self.randomRowHard][self.randomColHard - 1]
                            == 3
                        )
                        and (self.randomRowHard, self.randomColHard - 1)
                        != (self.randomRow, self.randomCol)
                    ):
                        self.randomColHard -= 1
                        self.redColCheck = self.randomColHard
                        self.updateinitialDirectionList2()
                    else:
                        redStopped = False
                else:
                    redStopped = False
                    self.isRed = True

                if (self.randomRow, self.randomCol) != (1, 1):
                    if (
                        # self.randomCol > 0
                        # and (self.randomRow, self.randomCol - 1)
                        # not in self.constantsSquares
                        self.randomCol > 1
                        and (
                            self.hardList[self.randomRow][self.randomCol - 1] == 0
                            or self.hardList[self.randomRow][self.randomCol - 1] == 3
                        )
                        and (self.randomRow, self.randomCol - 1)
                        != (self.randomRowHard, self.randomColHard)
                    ):
                        # self.hard_History.append(self.state_Hard.board)
                        # self.state_Hard = copy.deepcopy(self.state_Hard)
                        # self.hardList = self.state_Hard.board
                        self.randomCol -= 1
                        self.blueColCheck = self.randomCol
                        self.updateinitialDirectionList1()
                    else:
                        blueStopped = False
                else:
                    blueStopped = False
                    self.isBlue = True

                self.hardList[self.randomRow][self.randomCol] = 2
                self.hardList[self.randomRowHard][self.randomColHard] = 4
                self.hardList[self.hardList == 3] = 0

                self.updateinitialDirectionList12()
        self.isStoped = True
        self.draw()
        self.isStoped = False

    # ----------------------------------------------------------------

    def move(self, event):
        if self.isMoving == True:
            return

        if event.key == "up":
            self.isMoving = True
            self.up()
            if self.isLost == False:
                self.isMoving = False
        if event.key == "down":
            self.isMoving = True
            self.down()
            if self.isLost == False:
                self.isMoving = False
        if event.key == "right":
            self.isMoving = True
            self.right()
            if self.isLost == False:
                self.isMoving = False
        if event.key == "left":
            self.isMoving = True
            self.left()
            if self.isLost == False:
                self.isMoving = False
        # if event.key == "r":
        #     self.reset_game()
        if event.key == "control":
            plt.close()

    # ----------------------------------------------------------------

    def play(self):
        self.draw()
        plt.show()

    # ----------------------------------------------------------------

    def startScreen(self):

        self.window.title("Select Difficulty")
        self.window.geometry("1000x1000")

        main_frame = tk.Frame(self.window, bg="lightblue")
        main_frame.pack(expand=True)

        title = tk.Label(
            main_frame, text="Zero Squares Game", font=("Arial", 20), fg="red"
        )
        title.pack(pady=(200, 200), padx=(200, 200))

        label = tk.Label(
            main_frame, text="Select Level ...", font=("Arial", 16), fg="darkblue"
        )
        label.pack(pady=(0, 10))

        button_frame = tk.Frame(main_frame, bg="lightgrey")
        button_frame.pack()

        easy_button = tk.Button(
            button_frame,
            text="Easy",
            command=lambda: self.start_game("Easy"),
            width=20,
            height=3,
            bg="lightgreen",
            fg="black",
            font=("Arial", 16),
        )
        easy_button.pack(pady=(10, 0), padx=(150, 150))

        hard_button = tk.Button(
            button_frame,
            text="Hard",
            command=lambda: self.start_game("Hard"),
            width=20,
            height=3,
            bg="salmon",
            fg="black",
            font=("Arial", 16),
        )
        hard_button.pack(pady=(50, 200), padx=(200, 200))

        self.window.mainloop()

    # ----------------------------------------------------------------
    def start_game(self, difficulty):
        # game = Game()
        self.level = difficulty
        self.window.destroy()
        self.play()

    # ----------------------------------------------------------------
    def checkWin(self):
        if self.level == "Easy":
            # print((self.randomRow, self.randomCol))
            if (self.randomRow, self.randomCol) == (1, 1):
                plt.suptitle("You Win", color="red", fontsize=20)
                self.easyList[self.randomRow][self.randomCol] = 0
                self.easyList[self.easyList == 3] = 0

                # self.easyList[2][2] = 2
                # plt.pause(0.05)
                self.isWin = True
                self.state_Hard.board[0][0] = 1
                self.state_Hard.board[2][5] = 0
                self.state_Hard.board[1][1] = 0
                self.hard_History.append(self.state_Hard.board)
                return True
            return False

        if self.level == "Hard":

            if (self.redRowCheck, self.redColCheck) == (2, 5) and (
                self.blueRowCheck,
                self.blueColCheck,
            ) == (1, 1):
                plt.suptitle("You Win", color="red", fontsize=20)
                self.hardList[self.hardList == 3] = 0
                # plt.pause(0.05)
                self.isWin = True
                self.state_Hard.board[0][0] = 1
                self.state_Hard.board[2][5] = 0
                self.state_Hard.board[1][1] = 0
                self.hard_History.append(self.state_Hard.board)
                print(self.hard_History)
                return True
            return False

    # ----------------------------------------------------------------
    def checkLose(self):
        if self.level == "Easy":
            # print((self.randomRow, self.randomCol))
            if (self.randomRow, self.randomCol) == (7, 8):
                plt.suptitle("You Lost", color="red", fontsize=20)
                self.easyList[self.randomRow][self.randomCol] = 5
                self.easyList[self.easyList == 3] = 0

                # self.easyList[2][2] = 2
                # plt.pause(0.05)
                self.isWin = True
                return True

            return False

        if self.level == "Hard":

            if (self.redRowCheck, self.redColCheck) == (7, 8) or (
                self.blueRowCheck,
                self.blueColCheck,
            ) == (7, 8):
                plt.suptitle("You Lost", color="red", fontsize=20)
                self.easyList[self.randomRow][self.randomCol] = 5
                self.easyList[self.randomRowHard][self.randomColHard] = 5
                self.hardList[self.hardList == 3] = 0
                self.isLost = True
                self.isWin = True
                print(self.hard_History)
                return True
            return False

    # ----------------------------------------------------------------
    def updateinitialDirectionList12(self):
        self.initialDirectionList12 = [
            (self.randomRow, self.randomCol + 1),
            (self.randomRow, self.randomCol - 1),
            (self.randomRow + 1, self.randomCol),
            (self.randomRow - 1, self.randomCol),
            (self.randomRowHard, self.randomColHard + 1),
            (self.randomRowHard, self.randomColHard - 1),
            (self.randomRowHard + 1, self.randomColHard),
            (self.randomRowHard - 1, self.randomColHard),
        ]

        for r, w in self.initialDirectionList12:
            if (r, w) not in self.constantsSquares and (1 <= r < 8 and 1 <= w < 9):
                self.hardList[r][w] = 3

    # ----------------------------------------------------------------
    def updateinitialDirectionList1(self):
        self.initialDirectionList1 = [
            (self.randomRow, self.randomCol + 1),
            (self.randomRow, self.randomCol - 1),
            (self.randomRow + 1, self.randomCol),
            (self.randomRow - 1, self.randomCol),
        ]

    # ----------------------------------------------------------------
    def setSquaresColors(self):
        for i in range(self.rows):
            for j in range(self.cols):
                color = self.colors[self.hardList[i][j]]
                rect = patches.Rectangle(
                    (j, self.rows - i - 1),
                    1,
                    1,
                    linewidth=1,
                    edgecolor="black",
                    facecolor=color,
                )
                self.ax1.add_patch(rect)  # ارقان الألوان برقم المكعب
                self.ax1.add_patch(self.goalSquare1)
                self.ax1.add_patch(self.goalSquare2)

    # ----------------------------------------------------------------
    def updateinitialDirectionList2(self):
        self.initialDirectionList2 = [
            (self.randomRowHard, self.randomColHard + 1),
            (self.randomRowHard, self.randomColHard - 1),
            (self.randomRowHard + 1, self.randomColHard),
            (self.randomRowHard - 1, self.randomColHard),
        ]

    # ----------------------------------------------------------------
    def blue_GreyToGreen_Easy(self):
        for r, w in self.initialDirectionList1:
            if (r, w) not in self.constantsSquares and (1 <= r < 8 and 1 <= w < 9):
                self.easyList[r][w] = 3

    # ----------------------------------------------------------------
    def blue_GreenToGrey_Easy(self):
        for r, w in self.initialDirectionList1:
            if (r, w) not in self.constantsSquares and (
                1 <= r < 8
                and 1 <= w < 9
                and (r, w) != (self.randomRowHard, self.randomColHard)
            ):
                self.easyList[r][w] = 0

    # ----------------------------------------------------------------
    def blue_GreyToGreen_Hard(self):
        for r, w in self.initialDirectionList1:
            if (
                (r, w) not in self.constantsSquares
                and (1 <= r < 8 and 1 <= w < 9)
                and (r, w) != (self.randomRowHard, self.randomColHard)
            ):
                self.hardList[r][w] = 3

    # ----------------------------------------------------------------
    def blue_GreenToGrey_Hard(self):
        for r, w in self.initialDirectionList1:
            if (r, w) not in self.constantsSquares and (
                1 <= r < 8
                and 1 <= w < 9
                and (r, w) != (self.randomRowHard, self.randomColHard)
            ):
                self.hardList[r][w] = 0

    # ----------------------------------------------------------------
    def red_GreyToGreen(self):

        for r, w in self.initialDirectionList2:
            if (
                (r, w) not in self.constantsSquares
                and (1 <= r < 8 and 1 <= w < 9)
                and (r, w) != (self.randomRow, self.randomCol)
            ):
                self.hardList[r][w] = 3

    # ----------------------------------------------------------------
    def red_GreenToGrey(self):
        for r, w in self.initialDirectionList2:
            if (r, w) not in self.constantsSquares and (
                (1 <= r < 8 and 1 <= w < 9)
                and (r, w) != (self.randomRow, self.randomCol)
            ):
                self.hardList[r][w] = 0

    # ----------------------------------------------------------------
