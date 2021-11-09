#!/usr/bin/python3

# Include all relevant modules
import time
from modules.grid import Grid

# Sleep time
sleep_time = 0.1

# Create the grid
grid = Grid(80, 30)
grid.activate(
    [
        (3, 3),
        (5, 3),
        (4, 4),
        (5, 4),
        (4, 5),

    ]
)


print(grid)
time.sleep(sleep_time)

for i in range(100):
    grid.simulate()
    print(grid)
    time.sleep(sleep_time)
