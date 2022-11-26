from pygame import *

class Unit(sprite.Sprite):
    def __init__(self, x, y, path_to_image):
        sprite.Sprite.__init__(self)
        self.up_pressed_once = False
        self.image = image.load (path_to_image) 
        print(type(self.image))
        self.rect = Rect(x, y, self.image.get_rect().width, self.image.get_rect().height) # rectangular object for now 
    
    def draw(self, screen): # Draw itself on the screen
        screen.blit(self.image, (self.rect.x,self.rect.y))