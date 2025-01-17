import pygame
import random
import quicksort
import mergesort
import insertionsort
import bubblesort

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
heights = [(i + 1) * 10 for i in range(SCREEN_WIDTH // 10)]

data = []
pos = 0
for i in range(SCREEN_WIDTH // 10):
    player = pygame.Rect(pos, 0, 10, heights[i])
    data.append(player)
    pos += 10

def convert_to_data(arr):
    data_arr = []
    pos = 0
    for i in range(SCREEN_WIDTH // 10):
        player = pygame.Rect(pos, 0, 10, arr[i])
        data_arr.append(player)
        pos += 10
    return data_arr

def randomize_data():
    random.shuffle(heights)
    pos = 0
    for i in range(SCREEN_WIDTH // 10):
        player = pygame.Rect(pos, 0, 10, heights[i])
        data[i] = player
        pos += 10

animate = []
len_animate = 0
frame = -1
last_update = pygame.time.get_ticks()
animation_cooldown = 100

# app loop
run = True
while run:

    screen.fill((0, 0, 0))

    # keypress events
    key = pygame.key.get_pressed()

    if key[pygame.K_r]:
        randomize_data()
        frame = -1
        len_animate = 0
        animate = []

    if key[pygame.K_b]:
        bubblesort.bubblesort(heights)
        animate = []
        for ani in bubblesort.bubblesort_animate:
            animate.append(convert_to_data(ani))
        len_animate = len(animate)
        frame = 0

    if key[pygame.K_i]:
        insertionsort.insertionsort(heights)
        animate = []
        for ani in insertionsort.insertionsort_animate:
            animate.append(convert_to_data(ani))
        len_animate = len(animate)
        frame = 0

    if key[pygame.K_q]:
        quicksort.quicksort(heights, 0, len(heights) - 1)
        animate = []
        for ani in quicksort.quicksort_animate:
            animate.append(convert_to_data(ani))
        len_animate = len(animate)
        frame = 0

    if key[pygame.K_m]:
        mergesort.mergesort(heights, 0, len(heights) - 1)
        animate = []
        for ani in mergesort.mergesort_animate:
            animate.append(convert_to_data(ani))
        len_animate = len(animate)
        frame = 0
    
    # ui updates
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown and frame < len_animate and len_animate != 0:
        frame += 1
        last_update = current_time

    if len_animate != 0 and frame < len_animate:
        for d in animate[frame]:
            pygame.draw.rect(screen, (20, 148, 20), d)   

    if not animate:
        for d in data:
            pygame.draw.rect(screen, (20, 148, 20), d)

    if frame == len_animate and animate:
        for d in animate[-1]:
            pygame.draw.rect(screen, (20, 148, 20), d)   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()

pygame.quit()