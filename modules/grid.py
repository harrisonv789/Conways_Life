# Include relevant imports
from .cell import Cell
from .pattern import *

# Define the Grid class for storing cells
class Grid:

    # Stores the width and height of a grid
    width: int = 10
    height: int = 10

    # Stores a 2D array of cells
    grid: list = []

    # Stores the generation
    generation: int = 0

    # Stores the population
    population: int = 0
    population_min: int = 0
    population_max: int = 0

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
            self.population += 1
        
        # If a list of tuples
        elif type(cells) is list and len(cells) > 0:
            for cell in cells:
                if type(cell) is tuple and len(cell) == 2:
                    self.grid[cell[1]][cell[0]].set_active(True)
                    self.population += 1

        # Updates the min and max
        self.population_min = self.population
        self.population_max = self.population

        # Return success
        return True

    
    # Adds a particular type of cell at some location
    def add (self, x: int, y: int, type: str = None):

        # If not type entered
        if type == None:
            self.activate([(x, y)])
            return

        pattern = get_pattern(type)
        
        # If the pattern exists
        if pattern != None:
            if x >= 0 and x < self.width - 1 - pattern[0] and y >= 0 and y < self.height - 1 - pattern[1]:
                self.activate(
                    [(x + xi, y + yi) for xi, yi in pattern[2]]
                )


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
        self.population = 0

        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x].update()
                self.population += self.grid[y][x]()

        self.generation += 1

        # Update the population min and max
        if self.population < self.population_min: self.population_min = self.population
        if self.population > self.population_max: self.population_max = self.population


    # Show the grid in the terminal
    def __str__(self) -> str:
        output =  "\tGeneration: %d\n" % self.generation
        output += "\tPopulation: \n\t\tNow: %d\n\t\tMin: %d\n\t\tMax: %d\n" % \
            (self.population, self.population_min, self.population_max)

        output += "+" + "-" * (self.width) + "+\n"

        for y in range(self.height):
            output += "|"
            for x in range(self.width):
                output += "*" if self.grid[y][x]() else " "
            output += "|\n"

        output += "+" + ("-" * (self.width)) + "+\n"

        return output