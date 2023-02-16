from PIL import Image, ImageDraw
import math
import random

size = 600
im = Image.new("RGB", (size, size), (255, 255, 255))
draw = ImageDraw.Draw(im)

def draw_polygon(draw, center, size, n, fill_color, outline_color):

    angles = [2 * math.pi * i / n for i in range(n)]
    radius = size / 2

    vertices = [
        (center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle))
        for angle in angles
    ]

    draw.polygon(vertices, fill=fill_color, outline=outline_color)

num_shapes = 20
colors = [(27, 96, 158), (208, 51, 71), (225, 169, 27), (41, 128, 185), (183, 28, 28)]

for i in range(num_shapes):

    size = random.randint(50, 200)
    n = random.choice([4, 6, 8])

    center = (
        random.randint(size, im.size[0] - size),
        random.randint(size, im.size[1] - size),
    )

    fill_color = random.choice(colors)
    outline_color = (0, 0, 0)

    draw_polygon(draw, center, size, n, fill_color, outline_color)

    if n == 4:

        diamond_size = size / 2
        diamond_center = (center[0], center[1])
        draw_polygon(draw, diamond_center, diamond_size, 4, fill_color, outline_color)

    elif n == 6:

        hex_size = size / 2
        hex_center = (center[0], center[1])
        draw_polygon(draw, hex_center, hex_size, 6, fill_color, outline_color)

    elif n == 8:

        square_size = size / 2
        square_center1 = (center[0] - square_size / 2, center[1] - square_size / 2)
        draw_polygon(draw, square_center1, square_size, 4, fill_color, outline_color)
        square_center2 = (center[0] + square_size / 2, center[1] + square_size / 2)
        draw_polygon(draw, square_center2, square_size, 4, fill_color, outline_color)

im.save("pattern.png")
