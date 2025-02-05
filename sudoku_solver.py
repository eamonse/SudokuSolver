from copy import deepcopy
from datetime import datetime
from typing import List
import math

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
        self.options = cell_options
        self.length = len(cell_options)
        self.chunk_length = int(math.sqrt(self.length))
        #casting go crazy
        self.nones = None

        #set attempt
        self.rows = None
        self.cols = None
        self.options_set = set(cell_options)
        self.big_chunk = None

        

    
    # solve
    # *************************
    # Takes a sudoku grid with some values filled in (2D array) and returns a solution grid 
    # with all cells filled in (also a 2D array).  Empty cell values are None.
    def solve(self, grid:List[List[str]]) -> List[List[str]]:
        self.initialize(grid)
        return self.recursion_solver(grid)

    #    #how to solve this with recursion/backtracking
    #    #i can use backtracking when determining the correct letter within the group
    #    none_within = False
    #    for row in grid:
    #        for col in row:
    #            if col == None:
    #                none_within = True
    #    if none_within == False:
    #        return grid
    #    else:
    #        row_index = 0
    #        for row in grid:
    #            col_index = 0
    #            for col in row:
    #                if col == None:
    #                    
    #                    #identify the chunk its in
    #                    #grab the group of letters in group, row, and col
    #                    #find the ones that are possible
    #                    #only solve if theres a case of one possible letter, otherwise continue
    #                    chunked_grid = self.chunk_grid(grid, ((row_index//self.chunk_length)*self.chunk_length), ((col_index//self.chunk_length)*self.chunk_length))
    #                    group = self.grab_possible_group_letters(chunked_grid)
    #                    #see valid_letters
    #                    row = self.grab_possible_row_letters(grid, row_index)
    #                    col = self.grab_possible_col_letters(grid, col_index)
    #                    final = self.identify_letters(row, col, group)
    #                    for x in final:
                            #grid[row_index][col_index] = x
                            ##choose
                            #grid = self.solve(grid)
                            ##explore
                            #
                            ##unchoose

                            #queens method - check to see if the assumed position is valid, then try substituting in and unchoosing
                            #create valid method to handle the new number and index on grid
                            #check to see if theres no overlap
                            #come back out by resetting the value to None if it doesnt work out
                            #recursion should take care of the rest

    #                        if self.valid_letter(grid, x, row_index, col_index) == True:
                                #if the letter works, add it
    #                           grid[row_index][col_index] = x
                                #somehow explore it
    #                            grid = self.solve(grid)
                                #and unchoose it with None
    #                            grid[row_index][col_index] = None
    #                col_index+=1
    #            row_index+=1
    #        return grid

    
    #the following are the ideas created with the assistance from Benoit

    #the base case would be if there are no more Nones found
    #that could be found by creating a helper function to get a list of the coords of all Nones (if the length of that is 0 there are no Nones)
    # sorting the list to organize by number of valid characters at that coordinate (the less there are the better it is)
    #keep in mind that sorting would have a check if its reversed or not(reverse should equal true), and then the key which HAS to be a method that returns an int (so create a method that thorws back len(final))
    # After its sorted, pop out the value at the end which should be the one with the least amount of values (lowest final len)
    # now grab the possible values that would go with that coordinate (the final with the coordinate)
    # 
    # the actual recursive loop
    # so the choose is still the same (assigning the grid at the coordinate to be the x of x in final)
    # update the sets - update with the value, coords, and remove = True as the sets have possible numbers so i want to get rid of it if im using it
    # recursive call of solved
    # check to see if solved does not equal None (meaning there are no more Nones found as in it reaches base case)
    # return that solved
    # otherwise (no else) try undoing it
    # set the original cord back to None and update the sets, but with remove equaling false which should add back the value as the code didnt work out
    # return None at the end
    # 
    # 
    # 
    # to update the set - if remove is true then it should remove the value from all possible sets
    # if remove is fals then it shoul add that value BACK into the original values



    def recursion_solver(self, grid:List[List[str]]) -> List[List[str]]:
        if len(self.nones) == 0:
            #if there are no Nones within the grid
            return grid
        
        coords = self.nones.pop()
        #coordinates (row,col) of None
        #chunked_grid = self.chunk_grid(grid, coords[0], coords[1])
        #group = self.grab_possible_group_letters(chunked_grid)
        #row = self.grab_possible_row_letters(grid, coords[0])
        #col = self.grab_possible_col_letters(grid, coords[1])
        #coords at 0 is the row index, while coords at 1 is the column index
        #final = self.identify_letters(row, col, group)
        #here is the list of the possible letters that could potentially work

        #the problem must be in the groupings, something isnt working when i combine them all together
        #attmpting to split it up even more into different functions pt 2 in progress

        final = self.valid_numbers(coords[0], coords[1])
       
        
        for letters in final:
            #if self.valid_letter(grid, x, coords[0], coords[1]):
            grid[coords[0]][coords[1]] = letters
            #just remove it from the lists directly with list.remove()
            #if self.val_here(row, letters):
            ##    row.remove(letters)
            #if self.val_here(col, letters):
            #    col.remove(letters)
            #if self.val_here(row, letters):
            #    group.remove(group)

            #too lengthy and weighty, too many things could go wrong/dont wanna check this every time in the recursion...
            #split into more functions
            #i suspect that somewhere here was what was causing my origninal tests to return a Nonetype - where no solution was found

            #attempting sets to avoid list.remove(val)

            self.prepare_sets(letters, coords[0], coords[1])
            solved = self.recursion_solver(grid)
            if solved != None:
                #if it reaches the base case and never has a None then it would have worked
                return solved
            grid[coords[0]][coords[1]] = None
            #if it dont work undo it
            self.unprepare_sets(letters, coords[0], coords[1])
            #dont forget to undo the coordinate as well


            #update the list AGAIN but this time i need to re-add the x value back because it didnt work (use append)
            #the biggest thing is that order doesnt matter its only the direct value that matters
            #so that didnt work


        self.nones.append(coords)
        #coordinates thrown back in
        return None
        #skip over this to come back to later


    #usage is in avoiding the valueError thats thrown when using list.remove(val) and val isnt in list (used in list implementation)
    def val_here(self, list:List[str], str:str) ->bool:
        for x in list:
            if x == str:
                return True
        return False


    #each tuple is a coordinate holding the position of None
    def nones_list(self, grid:List[List[str]]) -> List[tuple]:
        #the tuple would be the row and col index, and its a list to get the coordinates of each
        none_list = []
        row_index = 0
        for row in grid:
            col_index = 0
            for col in row:
                if col == None:
                    coord = (row_index, col_index)
                    none_list.append(coord)
                col_index+=1
            row_index+=1
        return none_list

    
        
    
    #def solve_chunk(self,  grid:List[List[str]], chunked_grid:List[List[str]]) -> List[str]:
    #        group =  self.grab_possible_group_letters(chunked_grid)
    #        row_index = 0
    #        for row in chunked_grid:
    #            col_index = 0
    #            for col in row:
    #                if col == None:
    #                    #grab the group of letters in group, row, and col
    #                    #find the ones that are possible
    #                    #only solve if theres a case of one possible letter, otherwise continue
    #                    row = self.grab_possible_row_letters(grid, row_index)
    #                    col = self.grab_possible_col_letters(grid, col_index)
    #                    final = self.identify_letters(row, col, group)

    #gotta grab all the possible letters that can be used in a specified rows
    #possible letters are defined as letters that are not currently in use within that row
    #params:    grid: the sudoku 2d array it'll analyze
    #           row_number: the row index that the function will 
    def grab_possible_row_letters(self, grid:List[List[str]], row_number:int) -> List[str]:
        possible_letters = self.options
        for col in grid[row_number]:
            if col in possible_letters:
                possible_letters.remove(col)
                #get rid of letters already in use
        return possible_letters
        
            
    #possible letters within a column (same thing as row but col version)
    def grab_possible_col_letters(self, grid:List[List[str]], col_number:int) -> List[str]:
        possible_letters = self.options 
        for row in grid:
            counter = 0
            for col in row:
                if col in possible_letters and counter == col_number:
                    #in every place except the current letter
                    possible_letters.remove(col)
                counter = counter+1
        #for whatever reason, using grid[:,col_number] didn't work (should've grabbed an array of the column numbers directly)
        #attempting to transpose grid did not work either, so the ugly nested for loop had to be used
        return possible_letters

    #finally, the last possible letters should be within the group 
    #the key thing with sudoku is that its split within the numbers not being the same in the row, the column,
    #and finally not in the same grouping (in a standard 9x9 its split into 3x3s)
    #the accepted param MUST be the shortened chunk grid
    def grab_possible_group_letters(self, shortened_grid:List[List[str]]) -> List[str]:
        possible_letters = self.options
        for row in shortened_grid:
            for col in row:
                if col in possible_letters:
                    possible_letters.remove(col)
        return possible_letters

    #this function will chunk the grid into the smaller versions (e.g. the 3x3s of the 9x9) utilizing the sqroot
    #list implementation, works wonderfuflly
    #edit - did not work wonderfully in reality
    def chunk_grid_matrix(self, grid:List[List[str]], row_start:int, col_start:int) -> List[List[str]]:
        row_start = (row_start//self.chunk_length)*self.chunk_length
        col_start = (col_start//self.chunk_length)*self.chunk_length
        #let the method handle adjusting the index to figure out which chunk it is instead of letting that mess in the parameter
        #(former ugly code in the recursive solve method)
        shortened_grid = []
        row_index = 0
        for row in grid:
            col_index = 0
            temp_list = []
            if row_index >= row_start and row_index < (row_start+self.chunk_length):
                #checks to see if its the correct row does not exit out of the chunk grouping
                #now it should check for the column
                for col in row:
                    #time to check to see if its the correct column range
                    if col_index >=col_start and col_index < (col_start+self.chunk_length):
                        temp_list.append(col)
                        #grab every character within the boundaries (this is per col within the row)
                    col_index = col_index + 1
                shortened_grid.append(temp_list)
                #toss the rows together to form the 2D List
            row_index = row_index + 1
        return shortened_grid
        #this returns the small grids individually
        #try creating a set of these to create the entire grid

    #list implementation, how to combine all of the letters that are within all the possible letter lists
    #should return the only available letters left within
    def identify_letters(self, row_letters:List[str], col_letters:List[str], group_letters:List[str]) -> List[str]:
        row_set = set()
        col_set = set()
        group_set = set()       
        final_set = set() 
        final_list = []
        #initialze
        for x in row_letters:
            row_set.add(x)
        for x in col_letters:
            col_set.add(x)
        for x in group_letters:
            group_set.add(x)
        #throw into sets to use intersection to combine it all
        final_set = row_set.intersection(col_set).intersection(group_set)
        for x in final_set:
            final_list.append(x)
        #toss everything in a list and toss it back
        return final_list

    #check to see if the backtrack works and theres no double values
    #look through the row, then the col, then the chunk
    def valid_letter(self, grid:List[List[str]], char:str, row:int,col:int) -> bool:
        col_index = 0
        for x in range(self.length):
            #for every index x (up or down)
            if grid[row][col_index] == char and col_index != col:
                #check within the row (but exlude the original added position)
                return False
            col_index+=1
            
        
        col_index = 0
        for x in range(self.length):
            if grid[col_index][col] == char and row_index != row:
                #check within the col this time (but exlude the original added position), vice versa of the row check
                #should iterate over col BUT exclude the row that the oringinal col is in
                return False
            col_index+=1

        chunk = self.chunk_grid_matrix(grid, ((row//self.chunk_length)*self.chunk_length), ((col//self.chunk_length)*self.chunk_length))
        #WARNING chunk only works with something thats a multiple of chunk length
        #fixed - double divide drops the remainder and gives the back multiple of chunklength, and multiply it again to get the original
        #chunk instead of the very beginning chunk
        row_index = 0
        for r in chunk:
            col_index = 0
            for c in r:
                if chunk[row_index][col_index] == char and row_index != row and col_index != col:
                    #a combination of the previous two since this checks over a 2D list
                    #if the value is equal the the character that was put in AND the row/column are not the same then its not valid
                    return False
                col_index+=1
            row_index+=1

        #if it gets through to here, it'll work in the row, the column, and the box
        return True


        
        

    #didnt get how to work with a set for chunk grid(kept trying to iterate and directly change it) so Benoit helped here
    def chunk_grid_set(self, grid:List[List[str]], x:int, y:int) -> set:
        possibles = set(self.options_set)
        #copy possible letters
        for i in range(self.chunk_length):
            for j in range(self.chunk_length):
                #iterate over the entirety of the chunk
                if grid[x+i][y+j] != None:
                    possibles.remove(grid[x+i][y+j])
                    #if at all the chunk has letters, remove them from possible letters
        return possibles
        #should only contain the real letters now

    def valid_numbers(self, row:int, col:int) -> set:
        cols = self.cols[col]
        rows = self.rows[row]
        big_chunk = self.big_chunk[row//self.chunk_length][col//self.chunk_length]
        valids = cols.intersection(rows).intersection(big_chunk)
        return valids
    
    def initialize(self, grid:List[List[str]]):
        self.nones = self.nones_list(grid)

        
        temp_rows_list = []
        temp_cols_list = []
        for r in grid:
            row = set(self.options_set)
            column = set(self.options_set)
            temp_rows_list.append(row)
            temp_cols_list.append(column)
        row_index = 0
        for row in grid:
            col_index = 0
            for col in row:
                if grid[row_index][col_index] != None:
                    temp_rows_list[row_index].remove(grid[row_index][col_index])
                    temp_cols_list[col_index].remove(grid[row_index][col_index])
                col_index+=1
            row_index+=1
        self.rows = temp_rows_list
        self.cols = temp_cols_list
        

        outer_chunks = []
        for i in range(self.chunk_length):
            inner_chunk = []
            for j in range(self.chunk_length):
                inner_chunk.append(self.chunk_grid_set(grid, i*self.chunk_length, j*self.chunk_length))
            outer_chunks.append(inner_chunk)
        
        self.big_chunk = outer_chunks


    #apparently one of the reasons that my code wasnt working before was because the lists weren't prepared properly
    #benoit recommended as a fix to this to create an update sets method, where i would handle the updates seperately in a helper function

    #preparing the set to explore would be for diving into the recursion and getting rid of used coordinates/letters
    def prepare_sets(self, letter:str, x:int, y:int):
        self.rows[x].remove(letter)
        self.cols[y].remove(letter)
        self.big_chunk[int(x/self.chunk_length)][int(y/self.chunk_length)].remove(letter)

    #unpreparing is the backtracking side of things, where you would add back the coordinates as it backs out (it wouldn't have reached
    # the point need to use this function if the grid was completed)
    def unprepare_sets(self, letter:str, x:int, y:int):
        self.rows[x].add(letter)
        self.cols[y].add(letter)
        self.big_chunk[int(x/self.chunk_length)][int(y/self.chunk_length)].add(letter)

def print_puzzle(puzzle):
    for r in puzzle:
        for c in r:
            if(c == None):
                print(" ", end=" ")
                continue
            print(c, end=" ")
        print()

def main():
    puzzle = [[None, "B", None, None],
                 ["C", None, None, "B"],
                 [None, "A", "D", None],
                 ["D", None, None, "A"]]
    print("Initial Puzzle (4x4):")
    print_puzzle(puzzle)     
    
    solver = SudokuSolver(["A", "B", "C", "D"])
    solved_puzzle = solver.solve(puzzle)
    print()
    print("Solved Puzzle:")
    print_puzzle(solved_puzzle)

    puzzle = [["S","G","F",None,None,None,None,"T",None],
            [None,None,None,"S",None,None,None,None,None],
            [None,None,None,"T",None,"G","W",None,"F"],
            ["T","L",None,None,None,"S","R",None,None],
            [None,None,None,None,"L",None,None,None,None],
            [None,None,"P","F",None,None,None,"L","T"],
            ["F",None,"N","P",None,"L",None,None,None],
            [None,None,None,None,None,"W",None,None,None],
            [None,"T",None,None,None,None,"P","N","G"]]
    print("Initial Puzzle (9x9):")
    print_puzzle(puzzle)  

    solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
    solved_puzzle = solver.solve(puzzle)
    print()
    print("Solved Puzzle:")
    print_puzzle(solved_puzzle)




    puzzle = [["6", "2", "A", None, "G", None, None, None, None, "4", None, "B", None, None, None, None],
            [None, "G", "B", "8", None, None, None, None, None, None, None, "F", None, None, None, None],
            ["9", "D", "F", None, None, None, "E", "3", "2", None, None, None, None, None, "4", "C"],
            [None, None, "4", None, "D", "5", "A", "F", "6", None, "G", "8", "7", None, "9", None],
            ["B", None, None, "5", None, None, "7", None, None, "G", "9", None, "1", None, "A", None],
            [None, None, "8", None, "B", "3", "9", "5", "7", None, None, "2", "4", None, None, "G"],
            ["G", None, None, "4", None, "1", "D", None, None, None, None, None, "6", None, None, "8"],
            ["C", None, "7", "6", "8", None, "G", "2", None, "B", None, None, None, "3", None, None],
            ["E", None, None, None, None, None, None, "9", None, None, "A", None, None, None, "8", "D"],
            ["4", "7", "G", None, None, None, None, "E", "B", None, None, "D", None, "9", None, None],
            ["A", "C", "1", "9", None, None, "2", "B", "G", None, None, None, None, "5", "6", None],
            [None, None, None, "2", "F", "4", None, None, "9", "6", None, None, None, None, None, "A"],
            [None, None, None, "3", None, None, None, "C", None, "8", "E", "G", "9", None, None, None],
            [None, "6", None, None, None, "7", None, None, "1", None, None, "9", "G", None, "C", None],
            ["1", "B", None, None, None, "A", "3", "8", None, "D", "5", "6", "2", None, None, None],
            ["8", "4", "9", "E", "1", "6", None, None, None, None, "2", "3", None, "B", None, None]]
    print("Initial Puzzle (16x16):")
    print_puzzle(puzzle)  

    solver = SudokuSolver(["A", "B", "C", "D", "E", "F", "G", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    solved_puzzle = solver.solve(puzzle)
    print()
    print("Solved Puzzle:")
    print_puzzle(solved_puzzle)



if __name__ == "__main__":
    main()