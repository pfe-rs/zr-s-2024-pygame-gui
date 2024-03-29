from ClassProzor import *
from ClassLajsna import *
import pygame
prozori=[]
class WindowMenager:
    def add_prozor(self):
        global prozori
        prozori.append(Prozor(100,50,1500,750))
    def remove_prozor(prozor):
        global prozori
        prozori.remove(prozor)
    def draw(self,screen):
        global prozori
        for prozor in prozori:
            prozor.draw(screen)
    def check_click(self,x,y):
        global prozori
        for i in range(len(prozori)-1,-1,-1):
            pamti=len(prozori)-1
            if(x>=prozori[i].x and x<=prozori[i].x+prozori[i].width) and (y>prozori[i].y and y<prozori[i].y+prozori[i].height):
                prozori[i].click(x,y)
                if(len(prozori)-1<pamti):
                    break
                pom=prozori[i]
                for j in range(i+1,len(prozori)):
                    prozori[j-1]=prozori[j]
                prozori[len(prozori)-1]=pom
                break
    def mouseup(self):
        global prozori
        for prozor in prozori:
                prozor.lajsna.press=2
    def drag(self,x,y):
        global prozori
        for prozor in prozori:
            if prozor.lajsna.press==1:
                prozor.drag(x-prozor.lajsna.prevpress[0],y-prozor.lajsna.prevpress[1],x,y)