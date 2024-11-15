import bfs_dfs_methods
from models.gameClass import Game

######################################

game = Game()

################################ فتح اللعبة للعب =================================

# game.startScreen()
# print(len(game.hard_History))

################################ BFS_Search

path, visited_count = bfs_dfs_methods.bfs_search(game.hardList)
print("BfsPath")
for board in path:
    print(board)
    print("\n")
print("Thr Number Of Boards : ", len(path), "\n")
print("Thr Number Of visited Boards : ", visited_count, "\n")

################################ DFS_Search

# path, visited_count = bfs_dfs_methods.dfs_search(game.hardList)
# print("DfsPath")
# for board in path:
#     print(board)
#     print("\n")
# print("Thr Number Of Boards : ", len(path), "\n")
# print("Thr Number Of visited Boards : ", visited_count, "\n")
