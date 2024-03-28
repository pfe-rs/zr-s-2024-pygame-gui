import pygame
class Lajsna:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        # self.xx=self.x+self.width*14/15-self.width/30
        # self.xy=self.y+self.height/10
        # self.xwidth=self.width/15
        # self.xheight=self.height*8/10
        self.press=2
        self.prevpress=[-1,-1]
    def draw(self,screen):
        pygame.draw.rect(screen,(0, 102, 255),pygame.Rect(self.x,self.y,self.width,self.height))
        pygame.draw.line(screen,(200, 20, 0),(self.x+self.width*14/15-self.width/30,self.y+self.height/10),(self.x+self.width*14/15-self.width/30+self.width/15,self.y+self.height/10+self.height*8/10),3)
        pygame.draw.line(screen,(200, 20, 0),(self.x+self.width*14/15-self.width/30,self.y+self.height/10+self.height*8/10),(self.x+self.width*14/15-self.width/30+self.width/15,self.y+self.height/10),3)
   
    def click(self,x,y):
        if x>self.x+self.width*14/15-self.width/30 and x<self.x+self.width*14/15-self.width/30+self.width/15:
            self.press=0
        else:
            self.press=1
            self.prevpress=[x,y]
    def drag(self,x,y,prevx,prevy):
        self.x+=x
        self.y+=y
        #self.prevpress=[self.x,self.y]
        self.prevpress=[prevx,prevy]