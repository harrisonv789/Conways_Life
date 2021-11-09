# Conway's Game of Life :feet:

A small fun project to simulate Conway's Game of Life, created in Python 3. Conway's Game of Life simulates a grid of cells, where the state of each cell consists of whether the cell is alive or dead. Between each simulation frame, the state of each cell is dependent on the 8 neighbouring cells. The rules of the game are simple, and are calculated during each simulation time-step:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The main program can specify the grid size, the initial conditions (able to add specific patterns at positions) and the simulation settings.

---

To run the program:

```
./main.py
```
