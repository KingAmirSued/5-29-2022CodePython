from tkinter import W
from turtle import *
from time import *

class Sprite(Turtle):
    def __init__(self,x,y,step,color,shape):
        super().__init__()
        self.penup() 
        self.speed(0)
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = step

    def move_Up(self):    
        self.goto(self.xcor(), self.ycor() + self.step)
    def moveleft(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def moveright(self):
        self.goto(self.xcor() + self.step, self.ycor())   
    def move_Down(self):    
        self.goto(self.xcor(), self.ycor() - self.step) 


    def is_collide(self,Sprite):
        dist = self.distance(Sprite.xcor(), Sprite.ycor())
        if dist < 20:
            return True  
        else:
            return False 
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start,y_start)
        self.setheading(self.towards(x_end,y_end))
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end,self.y_end)<self.step:
            self.set_move(self.x_end,self.y_end,self.x_start,self.y_start)





player = Sprite(0,-150,10,'yellow','circle')
enemy = Sprite(-100,50,5,'red','square')
enemy.set_move(-100,30, 100,-30)

enemy2 = Sprite(100,-50,5,'red','square')
enemy2.set_move(100,-30,-100,-30)

enemy3 = Sprite(0,0,5,'red','square')
enemy3.set_move(200,10,-200,10)
princess = Sprite(0,150,0,'green','triangle')

scr = player.getscreen()
scr.listen()

scr.onkey(player.move_Up,'w')
scr.onkey(player.moveleft,'a')
scr.onkey(player.moveright,'d')
scr.onkey(player.move_Down,'s')

score = 0


while score < 3:
    enemy.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(princess):
        score += 1
        player.goto(0,-100)

    elif player.is_collide(enemy) or player.is_collide(enemy2) or player.is_collide(enemy3):
        princess.hideturtle()
        player.hideturtle()
        break


enemy.hideturtle()
enemy2.hideturtle()



