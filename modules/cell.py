# Specifies a cell class for storing data about a cell
class Cell:

    # The position of the cell
    x: int = 0
    y: int = 0

    # Whether the cell is active or not
    active: bool = False

    # Store the next state
    next_state = None

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

    # Sets the next state of the cell
    def set_next (self, next) -> bool:
        self.next_state = next
        return self.next_state

    # If the object is called, return the active sate
    def __call__(self) -> bool:
        return self.active

    # Updates the state of the cell
    def update (self) -> bool:
        if self.next_state != None:
            self.active = self.next_state
            self.next_state = None

