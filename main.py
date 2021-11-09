#!/usr/bin/python3

# Include all relevant modules
import time, os
from modules.grid import Grid

# Sleep time
sleep_time = 0.02

# Create the grid
grid = Grid(80, 40)
grid.add(0, 0, "glider")
grid.add(5, 0, "glider")
grid.add(10, 0, "glider")
grid.add(40, 10, "block")
grid.add(15, 15, "beacon")
grid.add(32, 25, "blinker")

grid.add(30, 25)
grid.add(31, 25)
grid.add(31, 23)
grid.add(34, 25)
grid.add(35, 25)
grid.add(36, 25)
grid.add(33, 24)


# Simulate the gird
for i in range(2000):
    os.system("clear")
    print(grid)
    time.sleep(sleep_time)
    grid.simulate()
