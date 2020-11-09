import turtle
import random

pencere = turtle.Screen()
pencere.screensize(600, 600)
pencere.title("Örümcek Yakalama Oyunu")
pencere.bgcolor("green")
pencere.tracer(2)

oyuncu = turtle.Turtle()
oyuncu.color("black")
oyuncu.shape("square")
oyuncu.shapesize(3)
oyuncu.penup()

score = 0
yaziPuan = turtle.Turtle()
yaziPuan.speed(0)
yaziPuan.shape("square")
yaziPuan.color("white")
yaziPuan.penup()
yaziPuan.hideturtle()
yaziPuan.goto(-200, 200)
yaziPuan.write("Puan :{}".format(score), align="center",font=("Courier",24,"normal"))

speed = 1

hizPuan = turtle.Turtle()
hizPuan.speed(0)
hizPuan.shape("square")
hizPuan.color("white")
hizPuan.penup()
hizPuan.hideturtle()
hizPuan.goto(200, 200)
hizPuan.write("Hız :{}".format(speed), align="center",font=("Courier",24,"normal"))

def solaDon():
    oyuncu.left(30)

def sagaDon():
    oyuncu.right(30)

def hiziArtir():
    global speed
    speed = speed + 1
    hizPuan.clear()
    hizPuan.write("Hız :{}".format(speed), align="center", font=("Courier", 24, "normal"))

def hiziAzalt():
    global speed
    speed = speed - 1
    hizPuan.clear()
    hizPuan.write("Hız :{}".format(speed), align="center", font=("Courier", 24, "normal"))


pencere.listen()
pencere.onkey(solaDon,"Left")
pencere.onkey(sagaDon,"Right")
pencere.onkey(hiziArtir,"Up")
pencere.onkey(hiziAzalt,"Down")

maxHedef = 5
orumcekler = []
for i in range(maxHedef):
    orumcekler.append(turtle.Turtle())
    orumcekler[i].penup()
    orumcekler[i].color("red")
    orumcekler[i].shape("turtle")
    orumcekler[i].speed(1)
    orumcekler[i].setposition(random.randint(-300, 300), random.randint(-300, 300))



while True:
    oyuncu.forward(speed)

    if oyuncu.xcor() > 300 or oyuncu.xcor() < -300:
        oyuncu.right(180)

    if oyuncu.ycor() > 300 or oyuncu.ycor() < -300:
        oyuncu.right(180)

    for i in range(maxHedef):
        orumcekler[i].forward(1)
        if orumcekler[i].xcor() > 500 or orumcekler[i].xcor() < -500:
            orumcekler[i].right(random.randint(150,250))
        if orumcekler[i].ycor() > 500 or orumcekler[i].ycor() < -500:
            orumcekler[i].right(random.randint(150,250))
        if oyuncu.distance(orumcekler[i]) < 40:
            orumcekler[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
            orumcekler[i].right(random.randint(0, 360))
            score = score + 10
            yaziPuan.clear()
            yaziPuan.write("Puan :{}".format(score), align="center", font=("Courier", 24, "normal"))