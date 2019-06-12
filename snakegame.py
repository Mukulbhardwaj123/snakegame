import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# setting up the screen
wn = turtle.Screen()
wn.title("SNAKE GAME BY MUKULBHARDWAJ")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns of the screen updates

# SNAKE HEAD
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()  # it does not draw anything(turtle module)
head.goto(0, 0)  # remain in the centre of the screen at the start of game
head.direction = "stop"

# SNAKE FOOD
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()  # it does not draw anything(turtle module)
food.goto(0, 100)  # remain in the centre of the screen at the start of game

segments = []

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("navyblue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# FUNCTIONS
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
wn.listen()  # our created window
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# MAIN GAME LOOP
while True:
    wn.update();

    # CHECK FOR THE COLLISIONS WITH BORDER
    w = head.xcor()
    h = head.ycor()
    if w > 290 or w < -290 or h > 290 or h < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide the segments
        for segment in segments:
            segment.goto(1234, 1234)

        # Clear the segments list
        segments.clear()
        # reset the delay
        delay = 0.1
        # reset the score
        score = 0

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # check for a collision with the food
    if (head.distance(food) < 20):

        # move the food to random part

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # ADD A SEGMENT
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order:

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # Move segment ) to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(100000, 100000)

            # Clear the segments list
            segments.clear()
            # reset the delay
            delay = 0.1
            # reset the score
            score = 0

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()