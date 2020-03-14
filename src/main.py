from board import Board, State
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))
state = State.generateFromTxt(dir_path + "/../levels/2.txt")

print(state)

