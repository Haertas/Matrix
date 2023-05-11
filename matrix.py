import pygame
import random

pygame.init()

width = 1920
height = 1080

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matrix")

black = (0, 0, 0)
green = (0, 255, 0)

font = pygame.font.Font("matrix code nfi.ttf", 11)

def generate_symbol():
    return chr(random.randint(33, 126))

def generate_start_position():
    x = random.randint(0, width)
    y = random.randint(-height, 0)
    return x, y

symbols = []
density = 17
for y in range(0, height, density):
    for x in range(0, width, density):
        symbol = generate_symbol()
        speed = random.randint(5, 15)  
        symbols.append({"symbol": symbol, "x": x, "y": y, "speed": speed})

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for symbol in symbols:
        symbol["y"] += symbol["speed"]
        if symbol["y"] > height:
            symbol["y"] = random.randint(-height, 0)
            symbol["symbol"] = generate_symbol()
            symbol["speed"] = random.randint(5, 15)

    window.fill(black)

    for symbol in symbols:
        text = font.render(symbol["symbol"], True, green)
        window.blit(text, (symbol["x"], symbol["y"]))

    pygame.display.flip()
    clock.tick(144)
pygame.quit()
