import SZH
import pygame
import sys
import math
import traceback
from pygame.locals import *
from random import *
import serial
ser=serial.Serial('com3',9600)
pygame.init()
pygame.mixer.init()
bg_size = width, height = 800, 600

screen  = pygame.display.set_mode(bg_size)
pygame.display.set_caption("贪吃蛇")

clock = pygame.time.Clock()
eat_sound = pygame.mixer.Sound("enemy1_down.wav")
eat_sound.set_volume(0.5)
def main():
    running = True
    score_font = pygame.font.Font("font.ttf", 36)
    food = [ ]
    stone = [ ]
    q = [ ]
    q.append(SZH.PVector(50, 50))
    q.append(SZH.PVector(45, 50))
    ell_size = (30, 30)
    snake_color = (0, 255, 0)
    food_color = (255, 0, 0)
    stone_color = (0, 0, 0)
    direction = SZH.PVector(30, 0)
    mspeed = 5
    delay = 100
    speed = [ ]
    speed.append(SZH.PVector(5,0))
    speed.append(SZH.PVector(0.08,0))
    for i in range(15):
        food.append((randint(0,width),randint(0,height)))
        stone.append((randint(100,width),randint(100,height)))
        
    while running:
        screen.fill((204,204,204))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ser.write(bytes('s','utf-8'))
        xtmpstring=''
        ytmpstring=''
        while(1):
            t=str(ser.read())
            if(t!="b'x'"):
                xtmpstring+=str(int(t[2]))
            else:
                break
        while(1):
            t=str(ser.read())
            if(t!="b'y'"):
                ytmpstring+=str(int(t[2]))
            else:
                break
        speed[0].x=(float(xtmpstring)-511)/100
        speed[0].y=(float(ytmpstring)-511)/100
        # 绘制得分
        score_text = score_font.render("Score : %s" % str(len(q)),\
                    True, (0, 0,255))
        screen.blit(score_text, (width-200, 5))
        # 绘制速度
        speed_text = score_font.render("V : %s" % str(speed[0].mag()),\
                    True, (0, 0,255))
        screen.blit(speed_text, (width-200, 35))
        #控制蛇的方向及速度
        '''key_pressed = pygame.key.get_pressed()

        if key_pressed[K_a] or key_pressed[K_LEFT]:
            direction.dirset(direction.direction()+0.3)
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            direction.dirset(direction.direction()-0.3)
        if key_pressed[K_d] or key_pressed[K_DOWN]:
            if speed[0].mag()>mspeed:
                speed[0].magset(speed[0].mag()-0.5)
        if key_pressed[K_w] or key_pressed[K_UP]:
            speed[0].magset(speed[0].mag()+0.5)
        speed[0].dirset(direction.direction())'''
        #绘制方向盘
        SZH.ellipse((width//2, height-30),(60, 60),(0, 0, 0),2)
        pygame.draw.line(screen,(0, 0, 0),(width//2, height-30),\
        (30*math.cos(speed[0].direction())+width//2,30*math.sin(speed[0].direction())+height-30), 2)
        for i in range(len(q)-1,0,-1):
            q[i] = SZH.PVector(q[i-1].it_x(),q[i-1].it_y())
        q[0].add(speed[0].it())
                     
        for i in range(len(q)-1,-1,-1):
            SZH.ellipse(q[i].it(),ell_size,snake_color,5)
            SZH.ellipse(q[i].it(),(20, 20),(100,100,100),10)
        for i in range(len(food)):
            SZH.ellipse(food[i],ell_size,food_color,30)
            SZH.ellipse(stone[i],ell_size,stone_color,30)
            if SZH.dist(q[0].it(),food[i])<25:
                food[i] = (randint(0, width),randint(0, height))
                q.append(q[len(q)-1])
                eat_sound.play()
            '''if(not(width>q[0].it_x()>0)):
                q[0].x=width-q[0].x
            if(not(height>q[0].it_y()>0)):
                q[0].y=height-q[0].y'''
            if SZH.dist(q[0].it(),stone[i])<25 or not(width>q[0].it_x()>0 and height>q[0].it_y()>0):
                speed[0].magset(0.000000001)
                screen.fill((204,204,204))
                
                # 读取历史最高得分
                with open("best.txt", "r") as f:
                    record_score = int(f.read())

                # 如果玩家得分高于历史最高得分，则存档
                if len(q) > record_score:
                    with open("best.txt", "w") as f:
                        f.write(str(len(q)))
                # 绘制结束得分
                score_text = score_font.render("Score : %s" % str(len(q)),\
                    True, (0, 0,255))
                screen.blit(score_text, (width/2-80, height/2))
                
                best_text = score_font.render("bestScore : %s" % str(record_score),\
                    True, (0, 0,255))
                screen.blit(best_text, (width/2-80, height/2+50))
                # 绘制游戏结束
                over_text = score_font.render("game over" ,\
                    True, (0, 0,255))
                screen.blit(over_text, (width/2-80, height/2-50))
        pygame.display.flip()
        pygame.time.delay(delay)
        clock.tick(600)
        

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
