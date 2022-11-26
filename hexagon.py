import pygame
from pygame import *
from time import sleep
from math import sin, radians



class HexagonFactory(sprite.Sprite):

    def __init__(self, screen, radius):
        self.screen = screen
        self.radius = radius
        self.already_drawn_hexes = list()
    
    def hightlight_hexagon(self, x_click, y_click, path_to_image=None):
        for dot in self.already_drawn_hexes:
            x_dot, y_dot = dot
            if abs(x_dot - x_click) < self.radius and abs(y_dot - y_click) < self.radius:
                self.__draw_hexagon(x_dot, y_dot, (255, 0, 0), False)
                if path_to_image != None:
                    self.screen.blit(image.load (path_to_image), dot)
                pygame.display.flip()
                return

        

    def draw_hexagon(self, x_center, y_center):
        return self.__draw_hexagon(x_center, y_center) 

    def __draw_hexagon(self, x_center, y_center, line_color = (171, 32, 253), add_to_roster=True):
        hxgn = Hexagon(self.radius, x_center, y_center)
        if add_to_roster == True:
            self.already_drawn_hexes.append((x_center, y_center))
        
        vertex_index = 1
        while vertex_index < 7:
            if vertex_index == 6:
                pygame.draw.line(self.screen, line_color, hxgn.dots[vertex_index], hxgn.dots[vertex_index - 5], width=3)
            else:    
                pygame.draw.line(self.screen, line_color, hxgn.dots[vertex_index], hxgn.dots[vertex_index + 1], width=3)

            vertex_index += 1

        return hxgn

    def is_dot_inlist(self, dot):
        x_center, y_center = dot
        for dot_element in self.already_drawn_hexes:
            dot_x_element, dot_y_element = dot_element
            if abs(dot_x_element - x_center) < 10 and abs(dot_y_element - y_center) < 10:
                return True
        return False

class Hexagon:
    radius = 0
    dots = [ (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.dots[0] = (x_center, y_center)
        self.get_dots() 
    
    def get_dots(self):
        self.dots[1] = (self.dots[0][0] + self.radius, self.dots[0][1]) #3 hours
        self.dots[2] = (self.dots[1][0] - self.radius*sin(radians(30)), self.dots[1][1] + self.radius*sin(radians(60))) #5
        self.dots[3] = (self.dots[2][0] - self.radius, self.dots[2][1]) #7
        self.dots[4] = (self.dots[3][0] - self.radius*sin(radians(30)), self.dots[3][1] - self.radius*sin(radians(60))) #9
        self.dots[5] = (self.dots[4][0] + self.radius*sin(radians(30)), self.dots[4][1] - self.radius*sin(radians(60))) #11
        self.dots[6] = (self.dots[5][0] + self.radius, self.dots[5][1]) #1







