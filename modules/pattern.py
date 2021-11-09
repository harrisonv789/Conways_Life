def get_pattern (pattern: str):
    pattern = pattern.lower()
    if pattern == "glider":
        return glider()
    if pattern == "block":
        return block()
    if pattern == "beehive":
        return beehive()
    if pattern == "beacon":
        return beacon()
    if pattern == "blinker":
        return blinker()


def glider ():
    width = 3
    height = 3
    cells = [
        (0, 0),
        (2, 0),
        (1, 1),
        (2, 1),
        (1, 2)
    ]
    return (width, height, cells)


def block ():
    width = 2
    height = 2
    cells = [
        (0, 0),
        (0, 1),
        (1, 1),
        (1, 0)
    ]
    return (width, height, cells)

def beehive ():
    width = 4
    height = 3
    cells = [
        (1, 0),
        (2, 0),
        (0, 1),
        (3, 1),
        (1, 2),
        (2, 2)
    ]
    return (width, height, cells)

def beacon ():
    width = 4
    height = 4
    cells = [
        (0, 0),
        (1, 0),
        (0, 1),
        (2, 3),
        (3, 2),
        (3, 3)
    ]
    return (width, height, cells)

def blinker ():
    width = 3
    height = 1
    cells = [
        (0, 0),
        (1, 0),
        (2, 0),
    ]
    return (width, height, cells)