from unittest import TestCase
from sudoku_solver import SudokuSolver

class SudokuSolverStudentTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_possible_row_letters(self): 
        puzzle = [["A", "B", "C", "D"],
                 ["C", None, "A", "B"],
                 ["B", "A", "D", None],
                 ["D", None, "B", "A"]]

        solver = SudokuSolver(["A", "B", "C", "D"])
        letters = solver.grab_possible_row_letters(puzzle, 1)
        self.assertEqual(letters, ["D"])

        solver = SudokuSolver(["A", "B", "C", "D"])
        letters = solver.grab_possible_row_letters(puzzle, 2)
        self.assertEqual(letters, ["C"])

        solver = SudokuSolver(["A", "B", "C", "D"])
        letters = solver.grab_possible_row_letters(puzzle, 3)
        self.assertEqual(letters, ["C"])



        puzzle = [[None,None,"N","F",None,None,None,"R","L"],
                [None,"R","S",None,"L",None,None,None,"G"],
                [None,None,None,None,None,None,None,None,"W"],
                [None,"T","F","R",None,None,None,None,None],
                [None,None,"G",None,"F",None,"S",None,None],
                [None,None,None,None,None,"W","R","F",None],
                ["T",None,None,None,None,None,None,None,None],
                ["N",None,None,None,"W",None,"G","P",None],
                ["G","S",None,None,None,"N","L",None,None]]
        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        letters = solver.grab_possible_row_letters(puzzle, 7)
        self.assertEqual(letters, ["L", "F", "S", "T", "R"])





    def test_possible_col_letters(self): 
        puzzle = [["A", "B", "C", "D"],
                 ["C", None, "A", "B"],
                 ["B", "A", "D", None],
                 ["D", None, "B", "A"]]
        solver = SudokuSolver(["A", "B", "C", "D"])
        letters = solver.grab_possible_col_letters(puzzle, 1)
        self.assertEqual(letters, ["C","D"])





    def test_possible_group_letters(self): 
        puzzle = [["A", "B", "C", "D"],
                 ["C", None, "A", "B"],
                 ["B", "A", "D", None],
                 ["D", None, "B", "A"]]

        solver = SudokuSolver(["A", "B", "C", "D"])
        chunked_grid = solver.chunk_grid(puzzle, 0, 0)
        letters = solver.grab_possible_group_letters(chunked_grid)
        self.assertEqual(letters, ["D"])

        solver = SudokuSolver(["A", "B", "C", "D"])
        chunked_grid = solver.chunk_grid(puzzle, 2, 0)
        letters = solver.grab_possible_group_letters(chunked_grid)
        self.assertEqual(letters, ["C"])

        solver = SudokuSolver(["A", "B", "C", "D"])
        chunked_grid = solver.chunk_grid(puzzle, 2, 2)
        letters = solver.grab_possible_group_letters(chunked_grid)
        self.assertEqual(letters, ["C"])



        puzzle = [[None,None,"N","F",None,None,None,"R","L"],
                [None,"R","S",None,"L",None,None,None,"G"],
                [None,None,None,None,None,None,None,None,"W"],
                [None,"T","F","R",None,None,None,None,None],
                [None,None,"G",None,"F",None,"S",None,None],
                [None,None,None,None,None,"W","R","F",None],
                ["T",None,None,None,None,None,None,None,None],
                ["N",None,None,None,"W",None,"G","P",None],
                ["G","S",None,None,None,"N","L",None,None]]

        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        chunked_grid = solver.chunk_grid(puzzle, 0, 0)
        letters = solver.grab_possible_group_letters(chunked_grid)
        self.assertEqual(letters, ["W", "L", "F", "T", "G", "P"])

        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        chunked_grid = solver.chunk_grid(puzzle, 3, 3)
        letters = solver.grab_possible_group_letters(chunked_grid)
        self.assertEqual(letters, ["L", "S", "T", "N", "G", "P"])

        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        chunked_grid = solver.chunk_grid(puzzle, 6, 6)
        letters = solver.grab_possible_group_letters(chunked_grid)
        self.assertEqual(letters, ["W", "F", "S", "T", "R", "N"])




    def test_chunk_grid(self):
        puzzle = [["A", "B", "C", "D"],
                 ["C", None, "A", "B"],
                 ["B", "A", "D", None],
                 ["D", None, "B", "A"]]
        solver = SudokuSolver(["A", "B", "C", "D"])
        chunked_grid = solver.chunk_grid(puzzle, 0, 0)
        answer = [["A","B"],
                  ["C",None]]
        self.assertEqual(chunked_grid, answer)
        self.assertEqual(len(chunked_grid[0]), 2)
        solver = SudokuSolver(["A", "B", "C", "D"])
        chunked_grid = solver.chunk_grid(puzzle, 0, 0)
        answer = [["B","A"],
                  ["D",None]]



        puzzle = [[None,None,"N","F",None,None,None,"R","L"],
                [None,"R","S",None,"L",None,None,None,"G"],
                [None,None,None,None,None,None,None,None,"W"],
                [None,"T","F","R",None,None,None,None,None],
                [None,None,"G",None,"F",None,"S",None,None],
                [None,None,None,None,None,"W","R","F",None],
                ["T",None,None,None,None,None,None,None,None],
                ["N",None,None,None,"W",None,"G","P",None],
                ["G","S",None,None,None,"N","L",None,None]]

        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        chunked_grid = solver.chunk_grid(puzzle, 0, 0)
        answer = [[None,None,"N"],
                  [None,"R","S"],
                  [None,None,None]]
        self.assertEqual(chunked_grid, answer)
        self.assertEqual(len(chunked_grid[0]), 3)
        
        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        chunked_grid = solver.chunk_grid(puzzle, 0, 3)
        answer = [["F",None,None],
                  [None,"L",None],
                  [None,None,None]]
        self.assertEqual(chunked_grid, answer)
        self.assertEqual(len(chunked_grid[0]), 3)




    def test_identify_letters(self): 
        puzzle = [[None,None,"N","F",None,None,None,"R","L"],
                [None,"R","S",None,"L",None,None,None,"G"],
                [None,None,None,None,None,None,None,None,"W"],
                [None,"T","F","R",None,None,None,None,None],
                [None,None,"G",None,"F",None,"S",None,None],
                [None,None,None,None,None,"W","R","F",None],
                ["T",None,None,None,None,None,None,None,None],
                ["N",None,None,None,"W",None,"G","P",None],
                ["G","S",None,None,None,"N","L",None,None]]

        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        chunked_grid = solver.chunk_grid(puzzle, 0, 0)
        col = solver.grab_possible_col_letters(puzzle, 0)
        group = solver.grab_possible_group_letters(chunked_grid)
        row = solver.grab_possible_row_letters(puzzle, 0)
        final = solver.identify_letters(row, col, group)
        correct_letters = True
        answer = ["W", "P"]
        if len(final) != len(answer):
            correct_letters = False
        for x in final:
            if x not in answer:
                correct_letters = False
        self.assertTrue(correct_letters)

        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        chunked_grid = solver.chunk_grid(puzzle, 3, 3)
        col = solver.grab_possible_col_letters(puzzle, 3)
        group = solver.grab_possible_group_letters(chunked_grid)
        row = solver.grab_possible_row_letters(puzzle, 3)
        final = solver.identify_letters(row, col, group)
        correct_letters = True
        answer = ["L", "S", "N", "G", "P"]
        for x in final:
            if x not in answer:
                correct_letters = False
        self.assertTrue(correct_letters)




    def test_valid_letters(self):
        puzzle = [["A", "B", "C", "D"],
                 ["C", None, "A", "B"],
                 ["B", "A", "D", None],
                 ["D", None, "B", "A"]]
        solver = SudokuSolver(["A", "B", "C", "D"])
        is_valid = solver.valid_letter(puzzle, "D", 1, 1)
        self.assertTrue(is_valid)
        is_valid = solver.valid_letter(puzzle, "C", 2, 3)
        self.assertTrue(is_valid)



        puzzle = [[None,None,"N","F",None,None,None,"R","L"],
                [None,"R","S",None,"L",None,None,None,"G"],
                [None,None,None,None,None,None,None,None,"W"],
                [None,"T","F","R",None,None,None,None,None],
                [None,None,"G",None,"F",None,"S",None,None],
                [None,None,None,None,None,"W","R","F",None],
                ["T",None,None,None,None,None,None,None,None],
                ["N",None,None,None,"W",None,"G","P",None],
                ["G","S",None,None,None,"N","L",None,None]]

        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        is_valid = solver.valid_letter(puzzle, "W", 0, 1)
        self.assertTrue(is_valid)
        is_valid = solver.valid_letter(puzzle, "R", 6, 8)
        self.assertTrue(is_valid)
