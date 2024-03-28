import pygame
class Lajsna:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.xx=self.x+self.w*14/15-self.w/30
        self.xy=self.y+self.h/10
        self.xw=self.w/15
        self.xh=self.h*8/10
    def draw(self,screen):
        pygame.draw.rect(screen,(0, 102, 255),pygame.Rect(self.x,self.y,self.w,self.h))
        pygame.draw.line(screen,(200, 20, 0),(self.xx,self.xy),(self.xx+self.xw,self.xy+self.xh),3)
        pygame.draw.line(screen,(200, 20, 0),(self.xx,self.xy+self.xh),(self.xx+self.xw,self.xy),3)
    def click(self,x,y):
        if(x>=self.x and x<=self.x+self.w) and (y>self.y and y<self.y+self.h):
            if (x>self.xx and x<self.xx+self.xw):
                print('na x')
            else: print('na lajsni')
    #def pressed(self,screen):
     #   if 