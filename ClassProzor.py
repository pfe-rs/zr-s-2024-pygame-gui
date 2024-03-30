from ClassLajsna import *
import pygame
class Prozor:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.lajsna=Lajsna(self.x,self.y,self.width,30)
    def draw(self,screen):
        pygame.draw.rect(screen,(153, 153, 102),pygame.Rect(self.x,self.y,self.width,self.height))
        self.lajsna.draw(screen)
    def click(self,x,y):
        if(x>=self.lajsna.x and x<=self.lajsna.x+self.lajsna.width) and (y>self.lajsna.y and y<self.lajsna.y+self.lajsna.height):
            self.lajsna.click(x,y,self)
    def drag(self,x,y,prevx,prevy):
        self.x+=x
        self.y+=y
        self.lajsna.drag(x,y,prevx,prevy)

