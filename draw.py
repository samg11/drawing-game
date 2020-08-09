import turtle # imports the turtle graphics module
import time # imports the time module

running = True # the main game loop depends on running being equal to true
xSpeed = 0 # sets the speed to 0
ySpeed = 0 # sets the speed to 0
u = True # sets penup to true
d = False # sets pendown to false
w = 600 # variable which I use for the width
h = 400 # variable which I use for the height
hw = w/2 # variable which is equal to half of the width and comes in handy when making the box stop at the wall
hh = h/2 # same thing as hw but for the height
time_elapsed = 0 # shows the time elapsed which helps with the timer
ps = 10 # variable for pensize

game = turtle.Screen() # creates the screen and assignes it to the variable, "game"
game.setup(width=w, height=h) # makes the screen (width variable) x (height variable)
game.tracer(0) # makes animation more smooth

box = turtle.Turtle() # assign an object to the varaible, "box"
box.shape("square") # sets the shape of the object to a box
box.penup() # keeps the pen up until the user is ready to put it down
box.speed(0) # makes the box move as fast as the computer can run(the speed is controlled via a delay in the main game loop)
box.direction = "stop" # lets the box get assigned a direction later


pen = turtle.Turtle() # creates the pen which writes
pen.speed(0) # writes things immeadiatly
pen.shape("circle") # sets the pen to be a circle but become irrelevant with .hideturtle
pen.color("black") # setting the font color to black
pen.penup() # move the pen up unless it
pen.hideturtle() # stops the user from seeing the pen itself
pen.goto(w-450,h-250) # puts everything the pen writes at coordinates with an x-axis of the width minus 450 and a y-axis of the height minus 250


def move():
	''' sets directions and moves the box '''
	global ySpeed, xSpeed # due to the variables ySpeed and xSpeed 
	if box.direction == "up" and box.ycor() < hh - ySpeed:
		''' moves the box up if the direction is up '''
		xSpeed = 0 # stops the box from moving along the x-axis
		ySpeed = 10 # makes the box start moving on the y-axis
		y = box.ycor() # sets the variable, "y" equal to the y-coordinate of the box
		box.sety(y + ySpeed) # adds the ySpeed value to the y-coordinate

	elif box.direction == "down" and box.ycor() > -hh + ySpeed*2:
		''' moves the box down if the direction is down '''
		xSpeed = 0 # stops the box from moving along the x-axis
		ySpeed = 10 # makes the box start moving on the y-axis
		y = box.ycor() # sets the variable, "y" equal to the y-coordinate of the box
		box.sety(y - ySpeed) # subtracts the ySpeed value from the y-coordinate

	elif box.direction == "left" and box.xcor() > -hw + xSpeed:
		''' moves the box left if the direction is left '''
		xSpeed = 10 # makes the box start moving on the x-axis
		ySpeed = 0 # stops the box from moving along the y-axis
		x = box.xcor() # sets the variable, "x" equal to the x-coordinate of the box
		box.setx(x - xSpeed) # subtracts the xSpeed value from the y-coordinate

	elif box.direction == "right" and box.xcor() < hw - xSpeed*2:
		''' moves the box right if the direction is right '''
		xSpeed = 10 # makes the box start moving on the x-axis
		ySpeed = 0 # stops the box from moving along the y-axis
		x = box.xcor() # sets the variable, "x" equal to the x-coordinate of the box
		box.setx(x + xSpeed) # adds the xSpeed value to the y-coordinate

def penChange():
	''' moves the pen up and down when you press the space bar '''
	global u,d # gets the variable, "u" and "d" which were assigned before the functions was defined
	if u:
		box.pendown() # starts writing

	elif d:
		box.penup() # stops writing

	u,d=d,u # makes d = u and u = d

def up():
	''' sets the direction of the box to up '''
	box.direction = "up"

def down():
	''' sets the direction of the box to down '''
	box.direction = "down"

def left():
	''' sets the direction of the box to left '''
	box.direction = "left"

def right():
	''' sets the direction of the box to right '''
	box.direction = "right"

def rb():
	''' sets the color of the box to red '''
	box.color("red")

def gb():
	''' sets the color of the box to green '''
	box.color("green")

def bb():
	''' sets the color of the box to blue '''
	box.color("blue")

def db():
	''' sets the color of the box to black '''
	box.color("black")

def stop():
	''' stops running the program '''
	running = False

def ips():
	''' increases the pensize '''
	global ps
	ps += 0.5

def dps():
	''' decreases the pen size '''
	global ps
	ps -= 0.5

game.onkeypress(up, "Up") # calls the "up" function when the up-arrow is pressed
game.onkeypress(down, "Down") # calls the "down" function when the down-arrow is pressed
game.onkeypress(left, "Left") # calls the "left" function when the left-arrow is pressed
game.onkeypress(right, "Right") # calls the "right" function when the right-arrow is pressed

game.onkeypress(penChange, "space") # calls the "penChange" function when the space-bar is pressed

game.onkeypress(rb, "r") # calls the "rb" function when the r-key is pressed
game.onkeypress(gb, "g") # calls the "gb" function when the g-key is pressed
game.onkeypress(bb, "b") # calls the "bb" function when the b-key is pressed
game.onkeypress(db, "d") # calls the "db" function when the d-key is pressed

game.onkeypress(ips, 'w') # calls the "ips" function when the w-key is pressed
game.onkeypress(dps, 's') # calls the "dps" function when the s-key is pressed

game.onkeypress(stop, "Escape") # calls the "up" function when the up-arrow is pressed

while running:
	''' main game loop '''
	time.sleep(0.1) # created a delay of 0.1 seconds
	game.update() # updates the game
	game.listen() # checks for key presses

	time_elapsed += 0.1 # adds 0.1 to the time_elapsed variable
	pen.clear() # clears what the pen has done
	pen.write(f"Time elapsed:\n{round(time_elapsed)}", font=("arial", 14, "normal")) # writes how much time has elapsed

	box.pensize(ps) # sets the pensize the "ps" variable

	move() # moves by calling the move function
	

#game.mainloop()