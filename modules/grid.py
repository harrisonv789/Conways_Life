# Include relevant imports
from .cell import Cell

# Define the Grid class for storing cells
class Grid:

    # Stores the width and height of a grid
    width: int = 10
    height: int = 10

    # Stores a 2D array of cells
    grid: list = []

    # Default constructor specifies a size
    def __init__(self, width: int = 10, height: int = 10) -> None:
        self.width = width
        self.height = height
        self.construct()

    # Constructs the array of cells and returns a success
    def construct (self) -> bool:

        # Reset the grid
        grid = []

        # Loop through each row
        for y in range(self.height):
            row = []

            for x in range(self.width):
                row.append(Cell(x, y))
            
            self.grid.append(row)

    # Activates a specific set of cells with a list of tuples
    #   e.g [(0, 0), (0, 1), (x, y)]
    def activate (self, cells: list) -> bool:
        if type(cells) is tuple and len(cells) == 2:
            self.grid[cells[1]][cells[0]].set_active(True)
            return True
        
        # If a list of tuples
        if type(cells) is list and len(cells) > 0:
            for cell in cells:
                if type(cell) is tuple and len(cell) == 2:
                    self.grid[cell[1]][cell[0]].set_active(True)
            return True
        
        # Invalid
        return False


    # Simulates a step in the grid
    def simulate (self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]

                # Counts number of live neighbours
                live = self.neighbours(x, y)

                # If the cell is currently active
                if cell():
                    if live < 2 or live > 3:
                        cell.set_next(False)

                # If the cell is dead
                else:
                    if live == 3:
                        cell.set_next(True)

        # Update all cells
        self.update()

    # Counts the number of live neighbours around a cell
    def neighbours (self, x, y):
        count = 0
        
        if x > 0:
            if self.grid[y][x-1](): count += 1
            if y > 0 and self.grid[y-1][x-1](): count += 1
            if y < self.height - 1 and self.grid[y+1][x-1](): count += 1
        if x < self.width - 1:
            if self.grid[y][x+1](): count += 1
            if y > 0 and self.grid[y-1][x+1](): count += 1
            if y < self.height - 1 and self.grid[y+1][x+1](): count += 1
        if y > 0 and self.grid[y-1][x](): count += 1
        if y < self.height - 1 and self.grid[y+1][x](): count += 1

        return count


    # Updates all cells
    def update (self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x].update()


    # Show the grid in the terminal
    def __str__(self) -> str:
        output = "+" + "-" * (self.width) + "+\n"

        for y in range(self.height):
            output += "|"
            for x in range(self.width):
                output += "*" if self.grid[y][x]() else " "
            output += "|\n"

        output += "+" + ("-" * (self.width)) + "+"

        return output