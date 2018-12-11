#沈正豪的个人库
#感谢processing
import pygame
import math
bg_size = width, height = 800, 600
screen  = pygame.display.set_mode(bg_size)
def ellipse(location, size, color, strokeWeight):
    x, y = location[0], location[1]
    width, height = size[0], size[1]
    if strokeWeight > min(width, height)//2:
        strokeWeight = min(width, height)//2
    pygame.draw.ellipse(screen, color,(x-width//2,\
        y-height//2, width, height),strokeWeight)

def dist(point1,point2):
    return ((point1[0]-point2[0])**2+\
            (point1[1]-point2[1])**2)**(0.5)

class PVector:
    def __init__(self,x,y):
        self.x, self.y = x, y
    def it(self):
        return (self.x, self.y)
    def it_x(self):
        return self.x
    def it_y(self):
        return self.y
    def add(self, q):
        self.x +=q[0]
        self.y +=q[1]
        return (self.x,self.y)
    def mag(self):
        return (self.x**2 + self.y**2)**0.5
    def magset(self,newlength):
        oldlength = (self.x**2 + self.y**2)**0.5
        self.x *= newlength/oldlength
        self.y *= newlength/oldlength
        return (self.x,self.y)
    def direction(self):
        if self.y>=0:
            if self.x>=0:
                return math.atan(self.y/self.x)
            else:
                return math.atan(self.y/self.x)+math.pi
        else:
            if self.x<=0:
                return math.atan(self.y/self.x)+math.pi
            else:
                return math.atan(self.y/self.x)
    def dirset(self,direction):
        length = (self.x**2 + self.y**2)**0.5
        self.x = length*math.cos(direction)
        self.y = length*math.sin(direction)
        return (self.x,self.y)
        
    

