import pygame
import tkinter
import tkinter.filedialog
from time import sleep

def get_picture():
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name

def text_out(screen, text, color, x_center, y_center, font_size = 32):
    font = pygame.font.SysFont("comicsansms", font_size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x_center, y_center)
    screen.blit(text, textRect) 

class VerticalTools:
    def __init__(self, screen, WIDTH, HEIGHT) -> None:
        self.path_to_image = None
        self.screen = screen
        self.window_width = WIDTH
        self.window_height = HEIGHT
        self.width = WIDTH/12
        self.button_text_color = (0, 0, 255)
        self.button_bg_color = (0, 0, 120)
        self.button_fore_color = (230, 230, 230)
        self.button_highlight_color = (171, 32, 253)
        self.y_shift = 100
        self.buttons = list()
        
    def draw_button(self, text):
        button = Button(text, self)
        button.draw(self, highlight=False)
        return button

    def draw_panel(self):
        pygame.draw.rect(self.screen, (0, 0, 120), pygame.Rect(0, 0, self.width + 3, self.window_height))
        pygame.draw.rect(self.screen, (210, 210, 210), pygame.Rect(3, 0, self.width - 3, self.window_height - 5))
        self.buttons.append(self.draw_button("Add unit"))        
        pygame.display.flip()

    def highlight_button(self, x_click, y_click, hightlight_text=False):
        for button in self.buttons:
            if button.top_rect.collidepoint((x_click, y_click)):
                button.draw(self, True, hightlight_text)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if hightlight_text:
                    pygame.display.flip()
                    sleep(0.1)
                    self.path_to_image = get_picture()
            else:
                button.draw(self, False)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.display.flip() 
                               

class Button:
    def __init__(self, text:str, panel: VerticalTools) -> None:
        self.text = text 
        self.font_size = 30 #TODO: make it as a function from 'button_height'
        x_border = panel.width/5  
        button_height = x_border * 1.5
        self.bottom_rect = pygame.Rect(x_border/2, panel.y_shift, x_border*4, button_height)
        self.top_rect = pygame.Rect(x_border/2 + 2, panel.y_shift + 2, x_border*4 - 4, button_height - 4)
    
    def draw(self, panel: VerticalTools, highlight: bool, hightlight_text = False):
        bg_color = panel.button_bg_color
        text_color = panel.button_text_color
        if highlight:
            bg_color = panel.button_highlight_color
        
        if hightlight_text:
            text_color = panel.button_highlight_color

        pygame.draw.rect(panel.screen,  bg_color, self.bottom_rect)
        pygame.draw.rect(panel.screen, panel.button_fore_color, self.top_rect)
        text_out(panel.screen, self.text, text_color, self.top_rect.centerx, self.top_rect.centery, 30)
