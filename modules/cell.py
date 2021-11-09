# Specifies a cell class for storing data about a cell
class Cell:

    # The position of the cell
    x: int = 0
    y: int = 0

    # Whether the cell is active or not
    active: bool = False

    # Constructor sets up the cell
    def __init__(self, x: int, y: int, active: bool = False) -> None:
        self.x = x
        self.y = y
        self.active = active

    # Returns the position of the cell
    @property
    def position (self) -> tuple:
        return (self.x, self.y)

    # Toggles the cell and returns the current state
    def toggle (self) -> bool:
        self.active = not self.active
        return self.active

    # Sets the active state of the cell and returns the current state
    def set_active (self, active) -> bool:
        self.active = active
        return self.active

