import algorithms
from models.gameClass import Game

######################################

game = Game()

################################ فتح اللعبة للعب =================================

# game.startScreen()
# print(len(game.hard_History))

################################ BFS_Search

# path, visited_count = algorithms.bfs_search(game.hardList)
# print("BfsPath")
# for board in path:
#     print(board)
#     print("\n")
# print("Thr Number Of Boards : ", len(path), "\n")
# print("Thr Number Of visited Boards : ", visited_count, "\n")

################################ DFS_Search

path, visited_count = algorithms.dfs_search(game.hardList)
print("DfsPath")
for board in path:
    print(board)
    print("\n")
print("Thr Number Of Boards : ", len(path), "\n")
print("Thr Number Of visited Boards : ", visited_count, "\n")

################################ DFS_Search_Recursive

path, visited_count = algorithms.dfs_search_recursive(game.hardList)
print("DfsPathR")
for board in path:
    print(board)
    print("\n")
print("Thr Number Of Boards : ", len(path), "\n")
print("Thr Number Of visited Boards : ", visited_count, "\n")

################################ UCS_Search

# path, visited_count, min_cost = algorithms.ucs_search(game.hardList)
# print("UcsPath")
# for board in path:
#     print(board)
#     print("\n")
# print("Thr Number Of Boards : ", len(path), "\n")
# print("Thr Number Of visited Boards : ", visited_count, "\n")
# print("The Minimum Path Cost: ", min_cost)
