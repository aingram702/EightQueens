from tkinter import *  # Import all of tkinter

SIZE = 8  # Size of the chessboard global variable

class EightQueens:
    def __init__(self):
        self.queens = SIZE * [-1]  # Positions for queens
        self.search(0)  # start search for solution from row 0
        
        # Display soltions in queens
        window = Tk()  # create window
        window.title("Eight Queens")  # set title
        
        image = PhotoImage(file = "B:/Projects/images/queen.GIF")
        for i in range(SIZE):
            for j in range(SIZE):
                if self.queens[i] == j:
                    Label(window, image = image).grid(row = i, column = j)
                else:
                    Label(window, width = 5, height = 2, bg = "red").grid(row = i, column = j)
        window.mainloop() # creates event loop
        
     # search for a solution starting from specific row
    def search(self, row):
        if row == SIZE:  # stopping condition
            return True  # solution found to place 8 queens
            
        for column in range(SIZE):
            self.queens[row] = column  # place it at (row, column)
            if self.isValid(row, column) and self.search(row + 1):
                return True  # found and exit loop
        
        # no solution for a queen placed at any column of this row
        return False
    
    # check if queen can be placed at row i and column j
    def isValid(self, row, column):
        for i in range(1, row + 1):
            if (self.queens[row - i] == column  # check column
                or self.queens[row - i] == column - i or self.queens[row - i] == column + i):
                return False  # there is a conflict
        return True  # no conflict
    
EightQueens()  # create GUI
        
