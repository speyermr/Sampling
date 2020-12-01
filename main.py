import math
import png
from drawing import blank_canvas, marker

size = 500
cycles = lambda n: n * 2 * math.pi

def plot(canvas, sample_rate):
    for x in range(size):
        v = x * cycles(2) / size
        w = math.sin(v)
        y = size//2 + int(size//2 * 0.9 * w)
        if x % sample_rate == 0:
            marker(canvas, x, y)

for r in [2, 5, 13, 23, 47, 57, 73, 97]:
    path = f'out.{r:02d}.png'
    canvas = blank_canvas(size)
    plot(canvas, r)
    png.write(canvas, path)