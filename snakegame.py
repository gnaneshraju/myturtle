'''import turtle
s=turtle.getscreen()
t=turtle.Turtle()
t.right(90)
t.forward(200)
t.left(90)
t.backward(100)
t.right(90)
t.backward(200)
t.left(90)
t.forward(100)
t.goto(100,100)
t.home()
t.dot(30)
t.goto(-200,100)
turtle.bgcolor("#FFFF00")
turtle.title("gnanesh's snake game")
i=1
t.shape("square")
t.shapesize(0.5,10,1)
t.fillcolor("red")
t.home()
t.speed(1)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
while(i<30):
    t.forward(i*1)
    i+=1
t=turtle.Turtle()
t.pencolor("yellow")
t.goto(-200,-200)
t.pencolor("black")
t.dot(20)
turtle.bgcolor("#E0FFFF")
t.forward(100)
t.right(90)
t.penup()
t.forward(100)
t.pendown()
t.right(90)
t.forward(300)
c=t.clone()
t.color("yellow")
c.color("magenta")
t.circle(100)
c.circle(50)'''

import turtle
import random
s=turtle.getscreen()
t=turtle.Turtle()
t.penup()
t.goto(-200,100)
t.shape("turtle")
t.shapesize(1,1,1)
t.color("green")
c=t.clone()
c.penup()
c.goto(-200,-100)
c.shape("turtle")
c.shapesize(1,1,1)
c.color("red")
t.penup()
t.goto(300,60)
t.pendown()
t.color("green")
t.circle(40)
t.penup()
t.goto(300,-120)
t.pendown()
t.color("red")
t.circle(40)
t.penup()
t.goto(-200,100)
t.color("green")
die1=[1,2,3,4,5,6]
die2=[1,2,3,4,5,6]
for i in range(20):
    if t.pos()>=(300,60):
        print("green wins")
        break
    if c.pos()>=(300,-120):
        print("red wins")
        break
    else:
        input("press enter to move the red turtle")
        z=random.choice(die1)
        print(z)
        t.forward(z*10)
        if t.pos()>=(300,60):
            print("green wins")
            break
        else:
            input("press enter to move the green turtle")
            w=random.choice(die2)
            print(w)
            c.forward(w*10)
            if c.pos()>=(300,-120):
                print("red wins")
                break
    
