from ClassProzor import *
from ClassLajsna import *
import pygame
class WindowMenager:
    def __init__(self):
        self.prozori=[]
    def add_prozor(self):
        self.prozori.append(Prozor(100,50,1500,750,'a'))
    def remove_prozor(self,prozor):
        self.prozori.remove(prozor)
    def draw(self,screen):
        for prozor in self.prozori:
            prozor.draw(screen)
    def check_click(self,x,y):
        for i in range(len(self.prozori)-1,-1,-1):
            if(x>=self.prozori[i].x and x<=self.prozori[i].x+self.prozori[i].width) and (y>self.prozori[i].y and y<self.prozori[i].y+self.prozori[i].height):
                self.prozori[i].click(x,y)
                if self.prozori[i].lajsna.press==0:
                    self.remove_prozor(self.prozori[i])
                pom=self.prozori[i]
                for j in range(i+1,len(self.prozori)):
                    self.prozori[j-1]=self.prozori[j]
                self.prozori[len(self.prozori)-1]=pom
                break
    def mouseup(self):
        for prozor in self.prozori:
                prozor.lajsna.press=2
    def drag(self,x,y):
        for prozor in self.prozori:
            if prozor.lajsna.press==1:
                prozor.drag(x-prozor.lajsna.prevpress[0],y-prozor.lajsna.prevpress[1],x,y)