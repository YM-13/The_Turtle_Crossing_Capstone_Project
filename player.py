from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.shapesize(stretch_wid=1, stretch_len=1)
		self.left(90)
		self.penup()
		self.go_to_start()

	def go_to_start(self):
		self.goto(STARTING_POSITION)

	# Player drives turtle
	def go_up(self):
		new_y = self.ycor() + MOVE_DISTANCE
		self.goto(self.xcor(), new_y)

	def is_at_finish_line(self):
		if self.ycor() == FINISH_LINE_Y:
			return True
