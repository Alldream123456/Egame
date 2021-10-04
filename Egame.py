import pygame
import sys
whether = False
print("\nWelcome the Egame.\n---Made by Pygame,Python")

'''<简单功能>'''

class eg():
    def setup(size_wideth,size_hight):
        global whether
        if whether == False:
            pygame.init()
        whether = True
        screen = pygame.display.set_mode((size_wideth,size_hight))

    def title(title):
        global whether
        if whether == False:
            pygame.init()
        whether = True
        pygame.display.set_caption(title)

    def flip():
        pygame.display.flip()

    def picture(pc,a):
        pygame.image.load(pc)
        
'''</简单功能>'''
eg=eg()
eg.picture('11.png')
