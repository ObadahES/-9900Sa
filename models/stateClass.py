import copy
import numpy as np

###########################################


class State:
    def __init__(self, board=None, parent=None):
        self.board = board
        self.parent = parent
        self.goals = [(1, 1), (2, 2)]

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

    def __hash__(self):
        # تحويل المصفوفة numpy.ndarray إلى tuple بحيث تصبح قابلة للتجزئة
        return hash(tuple(map(tuple, self.board)))

    # ----------------------------------------------------------------

    def next_State(state, currentBlue, currentRed):
        # تأكد من أن المتغير state هو كائن من نوع State
        if not isinstance(state, State):
            raise TypeError(
                "The 'state' parameter must be an instance of the 'State' class."
            )

        # نسخ البورد للحفاظ على محتوى الحالة الأصلية
        # initial_board = copy.deepcopy(state.board)
        nesxSteps = []

        # حركات لأربعة اتجاهات
        stepsList = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
        ]  ## تم استدعاء توابع الحركة بطريقة مختلفة

        # تكرار لكل اتجاه للحركة
        for r, w in stepsList:
            nextstate = copy.deepcopy(state)  # نسخة مستقلة للخطوة
            blueOver = True
            redOver = True
            currentRedRow, currentRedCol = currentRed
            currentBlueRow, currentBlueCol = currentBlue

            while redOver or blueOver:
                # حركة للمكعب الأحمر
                if (
                    0 < currentRedRow + r < 8
                    and 0 < currentRedCol + w < 9
                    and nextstate.board[currentRedRow + r][currentRedCol + w]
                    not in [1, 2]
                    and (currentRedRow, currentRedCol) != (2, 5)
                    and (currentRedRow + r, currentRedCol + w) != (7, 8)
                ):
                    nextstate.board[currentRedRow][
                        currentRedCol
                    ] = 0  # مسح الموضع الحالي
                    currentRedRow += r
                    currentRedCol += w
                    nextstate.board[currentRedRow][
                        currentRedCol
                    ] = 4  # تعيين الموضع الجديد للمكعب الأحمر
                else:
                    redOver = False

                # حركة للمكعب الأزرق
                if (
                    0 < currentBlueRow + r < 8
                    and 0 < currentBlueCol + w < 9
                    and nextstate.board[currentBlueRow + r][currentBlueCol + w]
                    not in [1, 4]
                    and (currentBlueRow, currentBlueCol) != (1, 1)
                    and (currentBlueRow + r, currentBlueCol + w) != (7, 8)
                ):
                    nextstate.board[currentBlueRow][
                        currentBlueCol
                    ] = 0  # مسح الموضع الحالي
                    currentBlueRow += r
                    currentBlueCol += w
                    nextstate.board[currentBlueRow][
                        currentBlueCol
                    ] = 2  # تعيين الموضع الجديد للمكعب الأزرق
                else:
                    blueOver = False

            nesxSteps.append(State(nextstate.board, state))
        # print("next", nesxSteps)
        return nesxSteps

    # ----------------------------------------------------------------
