# Import all classes
import time, os, sys
from .grid import Grid
from .color import Color

# Simulation class
class Simulation:

    # The grid of the simulation
    grid: Grid = None

    # Default constructor
    def __init__(self, grid: Grid) -> None:
        self.grid = grid

    # Run the simulation
    def run (self, steps = 100, screen = True, sleep = 0.1, progress = True) -> None:
        # Check for valid grid
        if self.grid == None:
            print("No Grid Found.")
            return

        # Simulate the grid
        for step in range(steps):   
            if screen:             
                time.sleep(sleep)  
                os.system("clear")
                print(self.grid)
            
            # Run simulation
            self.grid.simulate()

            # If showing the progress
            if progress:
                cur_progress = float(step) / float(steps - 1)
                print("\t%2.1f%%  |  %s%s%s" % ((cur_progress * 100.0), Color.YELLOW_B, \
                    ("=" * int(cur_progress * 50)), Color.END), end=("\r" if not screen else "\n"))
                if not screen: sys.stdout.flush()

        # Finish the simulation
        print("\nSimulation Complete.")