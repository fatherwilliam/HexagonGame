# importing required library
import pygame
from pygame.locals import *
import os
from hexagon import HexagonFactory
from panel_tools import VerticalTools 

def is_dot_valid(dot, WIDTH, HEIGHT, radius):
    x, y = dot 
    if x < 0 or x > WIDTH:
        return False

    if y < 0 or y > HEIGHT:
        return False

    #no crossing the upper line 
    if y < radius/4:
        return False

    #no crossing the right border
    if WIDTH - x < radius:
        return False

    #no crossing the bottom border 
    if y + radius > HEIGHT:
        return False 

    #no crossing the left border
    if x < WIDTH/12: #TODO
        return False

    return True 

def get_neighbors_centers(seed_hex, screen_width, screen_height):
    returned = []
    upper_right = (seed_hex.dots[6][0] + seed_hex.radius, seed_hex.dots[6][1])
    if is_dot_valid(upper_right, screen_width, screen_height, seed_hex.radius):
        returned.append(upper_right)
    
    lower_right = (seed_hex.dots[2][0] + seed_hex.radius, seed_hex.dots[2][1])
    if is_dot_valid(lower_right, screen_width, screen_height, seed_hex.radius):
        returned.append(lower_right)
    
    upper_left = (seed_hex.dots[5][0] - seed_hex.radius, seed_hex.dots[5][1])
    if is_dot_valid(upper_left, screen_width, screen_height, seed_hex.radius):
        returned.append(upper_left) 

    bottom_left = (seed_hex.dots[3][0] - seed_hex.radius, seed_hex.dots[3][1])
    if is_dot_valid(bottom_left, screen_width, screen_height, seed_hex.radius):
        returned.append(bottom_left)
    
    return returned


def draw_hexagons(screen, list_to_draw_dots, radius, WIDTH, HEIGHT, hexFactory: HexagonFactory):
    if len(list_to_draw_dots) == 0:
        return
    for dot in list_to_draw_dots:
        if hexFactory.is_dot_inlist(dot):
            continue
        x_center, y_center = dot
        hxgn = hexFactory.draw_hexagon(x_center, y_center)
        neighbor_dots = get_neighbors_centers(hxgn, WIDTH, HEIGHT)
        draw_hexagons(screen, neighbor_dots, radius, WIDTH, HEIGHT, hexFactory)

def draw_screen(screen, radius, WIDTH, HEIGHT):
    hexFactory = HexagonFactory(screen, radius)
    x_center = (WIDTH - WIDTH/11) / 2
    y_center = HEIGHT/2
    
    seed_hex = hexFactory.draw_hexagon(x_center, y_center)
    list_to_draw_dots = get_neighbors_centers(seed_hex, WIDTH, HEIGHT)
    draw_hexagons(screen, list_to_draw_dots, radius, WIDTH, HEIGHT, hexFactory)

    tools = VerticalTools(screen, WIDTH, HEIGHT)
    tools.draw_panel()
    pygame.display.flip()
    return (hexFactory, tools)

# activate the pygame library .
pygame.init()
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h
RADIUS = 70

scrn = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE) 

pygame.display.set_caption('Panzer General 2022')
 
bg_image_alpha = pygame.image.load(os.path.join("images", "westerneurope.jpg")).convert_alpha()
bg_image = pygame.transform.scale(bg_image_alpha, (WIDTH, HEIGHT))
scrn.blit(bg_image, (0, 0))

# Using blit to copy content from one surface to other
hexFactory, toolPanel = draw_screen(scrn, RADIUS, WIDTH, HEIGHT)

status = True
while (status):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x_hover, y_hover = event.pos
            toolPanel.highlight_button(x_hover, y_hover, hightlight_text = False)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_hover, y_hover = event.pos
            toolPanel.highlight_button(x_hover, y_hover, hightlight_text = True)
            if toolPanel.path_to_image != None:                
                hexFactory.hightlight_hexagon(x_hover, y_hover, toolPanel.path_to_image)  
            else:
                hexFactory.hightlight_hexagon(x_hover, y_hover)

        if event.type == pygame.MOUSEMOTION:
            x_hover, y_hover = event.pos
            toolPanel.highlight_button(x_hover, y_hover)    
        
        if event.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.quit()