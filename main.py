import numpy as np
import algorithms
from models.gameClass import Game
from models.stateClass import State as St

######################################

game = Game()


test_board10 = np.array(
    [
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
        [1, 4, 1, 0, 1, 1, 0, 0, 0, 1, 2, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
)

test_board20 = np.array(
    [
        [0, 0, 0, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 4, 0, 1, 1, 1],
        [1, 0, 7, 2, 0, 0, 0, 0, 1],
        [1, 0, 6, 1, 0, 0, 1, 8, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
)

test_board30 = np.array(
    [
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 4, 2, 6, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
)


# test_board = np.array(
#     [
#         [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 0, 0, 4, 1, 1, 1, 0, 1, 1, 0, 1],
#         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 6, 1, 0, 0, 1],
#         [1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#     ]
# )


# state_test = St(test_board30)
# currectRedPosition = [2, 1]
# currectBluePosition = [2, 2]
# currectGreenLightPosition = [2, 3]
# currectOrangePosition = [3, 1]
# currectPinkPosition = [3, 2]

# currectBluePosition = [2, 3]
# currectRedPosition = [1, 4]
# currectGreenLightPosition = [3, 2]
# currectPinkPosition = [2, 1]
# currectOrangePosition = [3, 7]


# nextStates = St.next_State30(
#     state_test,
#     currectBluePosition,
#     currectRedPosition,
#     currectGreenLightPosition,
#     currectPinkPosition,
#     currectOrangePosition,
# )
# for n in nextStates:
#     print(n.board)

################################ فتح اللعبة للعب =================================

# game.startScreen()
# print(len(game.hard_History))

################################ BFS_Search

# path, visited_count = algorithms.bfs_search(test_board30)
# print("BfsPath")
# for board in path:
#     print(board)
#     print("\n")
# print("Thr Number Of Boards : ", len(path), "\n")
# print("Thr Number Of visited Boards : ", visited_count, "\n")

################################ DFS_Search

# path, visited_count = algorithms.dfs_search(test_board30)
# print("DfsPath")
# # for board in path:
# #     print(board)
# #     print("\n")
# print("Thr Number Of Boards : ", len(path), "\n")
# print("Thr Number Of visited Boards : ", visited_count, "\n")

################################ DFS_Search_Recursive

# path, visited_count = algorithms.dfs_search_recursive(test_board30)
# print("DfsPathR")
# # for board in path:
# #     print(board)
# #     print("\n")
# print("Thr Number Of Boards : ", len(path), "\n")
# print("Thr Number Of visited Boards : ", visited_count, "\n")

################################ UCS_Search

# path, visited_count, min_cost = algorithms.ucs_search(test_board30)
path, visited_count = algorithms.ucs_search(test_board30)
print("UcsPath")
for board in path:
    print(board)
    print("\n")
print("Thr Number Of Boards : ", len(path), "\n")
print("Thr Number Of visited Boards : ", visited_count, "\n")
# print("The Minimum Path Cost: ", min_cost)

################################ Steepest_Hill_Climbing_Search

# path = algorithms.steepest_Hill_Climbing(test_board30)
# print("Steepest_Hill_ClimbingPath")
# # print(path)
# if path is None:
#     print("Stuck in local optimum!")
# else:
#     for board in path:
#         print(board)
#         print("\n")
#     print("Thr Number Of Boards : ", len(path), "\n")

################################ Simplest_Hill_Climbing_Search

# path, visited_states_count = algorithms.simplest_Hill_Climbing(test_board30)
# print("Simplest_Hill_ClimbingPath")
# # print(path)
# if path is None:
#     print("Stuck in local optimum!")
# else:
#     for board in path:
#         print(board)
#         print("\n")
#     print("Thr Number Of Boards : ", len(path), "\n")
#     if visited_states_count is None:
#         print("Thr Number Of Visited Boards : ", None, "\n")
#     else:
#         print("Thr Number Of Visited Boards : ", visited_states_count, "\n")


################################ A* + ManHatten


# path, visited_states_count = algorithms.a_Star_Manhattan(test_board30)
# print("A_Star_ManhattenPath")
# if path is None:
#     print("Stuck in local optimum!")
# else:
#     # for board in path:
#     #     print(board)
#     #     print("\n")
#     print("Thr Number Of Boards : ", len(path), "\n")
#     if visited_states_count is None:
#         print("Thr Number Of Visited Boards : ", None, "\n")
#     else:
#         print("Thr Number Of Visited Boards : ", visited_states_count, "\n")


################################ A* + Advanced_Heuristic


# path, visited_states_count = algorithms.a_Star_Advanced_Heuristic(test_board30)
# print("A_Star_Advanced_HeuristicPath")
# # print(path)
# if path is None:
#     print("Stuck in local optimum!")
#     print("visited_states_count", visited_states_count)
# else:
#     for board in path:
#         print(board)
#         print("\n")
#         print("Thr Number Of Boards : ", len(path), "\n")
#     if visited_states_count is None:
#         print("Thr Number Of Visited Boards : ", None, "\n")
#     else:
#         print("Thr Number Of Visited Boards : ", visited_states_count, "\n")
