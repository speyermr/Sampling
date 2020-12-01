Black = (0x00, 0x00, 0x00)
White = (0xff, 0xff, 0xff)


def blank_canvas(size):
    row = lambda: [(0, 0, 0) for _ in range(size)]
    return [row() for _ in range(size)]


def dot(canvas, x, y, size, color):
    deltas = [v - size // 2 for v in range(size)]
    for dy in deltas:
        for dx in deltas:
            cy = y + dy
            cx = x + dx
            if cy < 0 or cy >= len(canvas):
                continue
            row = canvas[cy]
            if cx < 0 or cx >= len(row):
                continue
            row[cx] = color


def marker(canvas, x, y):
    dot(canvas, x, y, 9, White)
    dot(canvas, x, y, 5, (0xa0, 0x20, 0x30))
