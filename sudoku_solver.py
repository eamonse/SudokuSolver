from copy import deepcopy
from datetime import datetime
from typing import List

# Generic Sudoku Solver
# ******************************
# A sudoku puzzle is one such that given a set of unique characters, each row, column, and 
# square grid can only have 1 each character. See https://masteringsudoku.com/sudoku-rules-beginners/
# for more information on how to play.
#
# Your job is to write a solver that takes a sudoku puzzle and fills in all the characters correctly.
# Puzzles for this assignment use any characters, not just traditional numbers 1-9, and the
# size can vary/is not always 9x9 (side length will always be a square number). Spots that are not
# filled in have None in them.
#
# Tips:
# - Sets are your friend!
# - solve is a wrapper; you will need a recursive version of the solve function
# - It is worthwhile to consider what you should initialize before starting your recursive algorithm
# - If you are not sure where to start, use previous backtracking exercises for inspiration
# 
# Extensions: 
# 1) If you are backtracking in empty cell order, try optimizing the solver by finding more optimal empty 
#    cells to use for your subsequent recursive calls. See how fast you can get the 16x16 test to finish!:)
#    Uncomment the 16x16 advanced test to put things to the test (see if you can get it to run in under 10 min)
# 2) Use tkinter to put a UI around the solver, where you can type in your own puzzles to solve!
# 3) Write a Sudoku puzzle creator

class SudokuSolver:

    # Constructor
    # ************************
    # cell_options param might look like ["W", "L", "F", "S", "T", "R", "N", "G", "P"]
    # The size of the grid will always be the length of cell_options  
    def __init__(self, cell_options:List[str]) -> None:
        pass
    
    # solve
    # *************************
    # Takes a sudoku grid with some values filled in (2D array) and returns a solution grid 
    # with all cells filled in (also a 2D array).  Empty cell values are None.
    def solve(self, grid:List[List[str]]) -> List[List[str]]:
        pass