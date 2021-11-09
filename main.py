#!/usr/bin/python3

# Include all relevant modules
from modules.simulation import Simulation
from modules.grid import Grid

# Create the grid
grid = Grid(80, 40)

# Add initial elements
grid.add(30, 0, "glider")
grid.add(54, 20, "block")

# Create the simulation
simulation = Simulation(grid)

# Run the simulation
simulation.run(
    steps=1000,
    sleep=0.1,
)