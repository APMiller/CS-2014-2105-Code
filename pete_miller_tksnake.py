# Pete Miller
# 5/11/2015
# Snake

from Tkinter import *
import random

def close():
	root.destory()

def keyPressed(event):
	#if(canvas.data.color == "green"):
		#print event.keysym, event.char
	if(event.keysym == "Up" and canvas.data.color == "green"):#0
		canvas.data.direction = 'up'
	elif(event.keysym == "Down" and canvas.data.color == "green"):#310
		canvas.data.direction = 'down'
	elif(event.keysym == "Right" and canvas.data.color == "green"):#210
		canvas.data.direction = 'right'
	elif(event.keysym == "Left" and canvas.data.color == "green"):#10
		canvas.data.direction = 'left'
	elif(event.keysym == "p" and canvas.data.color == "green"):
		canvas.data.direction = 'none'
	else:
		pass
	'''if(canvas.data.color == "orange"):
		if(canvas.data.initial_count < 3):
			if(event.keysym == "A"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "B"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "C"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "D"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "E"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "F"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "G"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "H"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "I"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "J"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "K"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "L"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "M"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "N"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "O"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "P"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "Q"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "R"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "S"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "T"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "U"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "V"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "W"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "X"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "Y"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
			elif(event.keysym == "Z"):
				canvas.data.initials = canvas.data.initials + event.keysym
				canvas.data.initial_count += 1
	if(canvas.data.initial_count == 3):
		print canvas.data.initials
		print canvas.data.score_name'''

def redrawAll():
	canvas.delete(ALL)
	canvas.create_rectangle(0, 0, canvas.data.death_width, canvas.data.death_height, fill = "red")
	canvas.create_rectangle(20, 20, canvas.data.width, canvas.data.height, fill = "black")
	#canvas.create_rectangle(0, 0, canvas.data.point_display_width, canvas.data.point_display_height, fill = "white")
	canvas.create_text(250, 10, text = "Score : %s" % (canvas.data.points))
	canvas.create_rectangle(canvas.data.x1, canvas.data.y1, canvas.data.x1 + 20, canvas.data.y1 + 20, fill = canvas.data.color)
	#canvas.create_image(canvas.data.x1 + 10, canvas.data.y1 + 1, image = canvas.photo)
	canvas.create_rectangle(canvas.data.food1_x1, canvas.data.food1_y1, canvas.data.food1_x1 + 20, canvas.data.food1_y1 + 20, fill = "yellow")
	canvas.create_rectangle(canvas.data.food2_x1, canvas.data.food2_y1, canvas.data.food2_x1 + 20, canvas.data.food2_y1 + 20, fill = "yellow")
	canvas.create_rectangle(canvas.data.food3_x1, canvas.data.food3_y1, canvas.data.food3_x1 + 20, canvas.data.food3_y1 + 20, fill = "yellow")
	canvas.create_rectangle(canvas.data.food4_x1, canvas.data.food4_y1, canvas.data.food4_x1 + 20, canvas.data.food4_y1 + 20, fill = "yellow")
	canvas.create_rectangle(canvas.data.food5_x1, canvas.data.food5_y1, canvas.data.food5_x1 + 20, canvas.data.food5_y1 + 20, fill = "yellow")
	canvas.create_rectangle(canvas.data.food6_x1, canvas.data.food6_y1, canvas.data.food6_x1 + 20, canvas.data.food6_y1 + 20, fill = "blue")
	#canvas.create_rectangle(canvas.data.food7_x1, canvas.data.food7_y1, canvas.data.food7_x1 + 20, canvas.data.food7_y1 + 20, fill = "purple")

def timerFired():
	redrawAll()
	if(canvas.data.direction == 'up' and canvas.data.y1 > 00):
		canvas.data.y1 -= 20
		canvas.data.y2 -= 20
	elif(canvas.data.direction == 'down' and canvas.data.y2 < 520):
		canvas.data.y1 += 20
		canvas.data.y2 += 20
	elif(canvas.data.direction == 'left' and canvas.data.x1 > 10):
		canvas.data.x1 -= 20
		canvas.data.x2 -= 20
	elif(canvas.data.direction == 'right' and canvas.data.x1 < 500):
		canvas.data.x1 += 20
		canvas.data.x2 += 20
	elif(canvas.data.direction == 'none'):
		pass
	#Death
	if(canvas.data.x1 < 20 or canvas.data.y1 < 20 or canvas.data.x2 > 500 or canvas.data.y2 > 500): #Death
		canvas.data.x1 += 0
		canvas.data.y1 += 0
		canvas.data.x2 += 0
		canvas.data.y2 += 0
		canvas.data.color = "orange"
		'''canvas.data.food6_x1 = random.randrange(20, 500, 20)
		canvas.data.food6_y1 = random.randrange(20, 500, 20)
		canvas.data.food6_x2 = canvas.data.food6_x1 + 20
		canvas.data.food6_y2 = canvas.data.food6_y1 + 20'''
	if(canvas.data.color == "orange" and canvas.data.go_count == 1):
		print "Game over"
		print "You got %s points" % (canvas.data.points)
		#Display High Scores
		print ""
		print "High Scores:"
		print "APM - 124"
		print "APM - 122"
		print "MLH - 110"
		print "NAG - 103"
		print "APM - 97"
		'''print ""
		print "Your initials: "'''
		#print canvas.data.initials
		#canvas.data.scores_out.write(canvas.data.initials + " - " + canvas.data.points + "\n")
		canvas.data.go_count += 1
	canvas.after(canvas.data.delay, timerFired)
	if(canvas.data.x1 == canvas.data.food1_x1 and canvas.data.y1 == canvas.data.food1_y1 and canvas.data.x2 == canvas.data.food1_x2 and canvas.data.y2 == canvas.data.food1_y2):
		canvas.data.points += 1
		canvas.data.food1_x1 = random.randrange(20, 500, 20)
		canvas.data.food1_y1 = random.randrange(20, 500, 20)
		canvas.data.food1_x2 = canvas.data.food1_x1 + 20
		canvas.data.food1_y2 = canvas.data.food1_y1 + 20
	elif(canvas.data.x1 == canvas.data.food2_x1 and canvas.data.y1 == canvas.data.food2_y1 and canvas.data.x2 == canvas.data.food2_x2 and canvas.data.y2 == canvas.data.food2_y2):
		canvas.data.points += 1
		canvas.data.food2_x1 = random.randrange(20, 500, 20)
		canvas.data.food2_y1 = random.randrange(20, 500, 20)
		canvas.data.food2_x2 = canvas.data.food2_x1 + 20
		canvas.data.food2_y2 = canvas.data.food2_y1 + 20
	elif(canvas.data.x1 == canvas.data.food3_x1 and canvas.data.y1 == canvas.data.food3_y1 and canvas.data.x2 == canvas.data.food3_x2 and canvas.data.y2 == canvas.data.food3_y2):
		canvas.data.points += 1
		canvas.data.food3_x1 = random.randrange(20, 500, 20)
		canvas.data.food3_y1 = random.randrange(20, 500, 20)
		canvas.data.food3_x2 = canvas.data.food3_x1 + 20
		canvas.data.food3_y2 = canvas.data.food3_y1 + 20
	elif(canvas.data.x1 == canvas.data.food4_x1 and canvas.data.y1 == canvas.data.food4_y1 and canvas.data.x2 == canvas.data.food4_x2 and canvas.data.y2 == canvas.data.food4_y2):
		canvas.data.points += 1
		canvas.data.food4_x1 = random.randrange(20, 500, 20)
		canvas.data.food4_y1 = random.randrange(20, 500, 20)
		canvas.data.food4_x2 = canvas.data.food4_x1 + 20
		canvas.data.food4_y2 = canvas.data.food4_y1 + 20
	elif(canvas.data.x1 == canvas.data.food5_x1 and canvas.data.y1 == canvas.data.food5_y1 and canvas.data.x2 == canvas.data.food5_x2 and canvas.data.y2 == canvas.data.food5_y2):
		canvas.data.points += 1
		canvas.data.food5_x1 = random.randrange(20, 500, 20)
		canvas.data.food5_y1 = random.randrange(20, 500, 20)
		canvas.data.food5_x2 = canvas.data.food5_x1 + 20
		canvas.data.food5_y2 = canvas.data.food5_y1 + 20
	canvas.data.food_time += 1
	if(canvas.data.food_time == 50):
		canvas.data.food_time = 0
		canvas.data.food6_x1 = random.randrange(20, 500, 20)
		canvas.data.food6_y1 = random.randrange(20, 500, 20)
		canvas.data.food6_x2 = canvas.data.food6_x1 + 20
		canvas.data.food6_y2 = canvas.data.food6_y1 + 20
	elif(canvas.data.x1 == canvas.data.food6_x1 and canvas.data.y1 == canvas.data.food6_y1 and canvas.data.x2 == canvas.data.food6_x2 and canvas.data.y2 == canvas.data.food6_y2):
		canvas.data.food_time = 0
		canvas.data.points += 5
		canvas.data.food6_x1 = random.randrange(20, 500, 20)
		canvas.data.food6_y1 = random.randrange(20, 500, 20)
		canvas.data.food6_x2 = canvas.data.food6_x1 + 20
		canvas.data.food6_y2 = canvas.data.food6_y1 + 20
	'''canvas.data.purple_food_time += 1
	canvas.data.purple_food_delay += 1
	if(canvas.data.purple_food_time == 30):
		canvas.data.purple_food_time = 0
		canvas.data.purple_food_delay = 0
		canvas.data.food7_x1 = 700
		canvas.data.food7_y1 = 700
		canvas.data.food7_x2 = 720
		canvas.data.food7_y2 = 720
		canvas.data.purple_food_flag = True
	elif(canvas.data.purple_food_delay == 30 and canvas.data.purple_food_flag == True):
		canvas.data.food7_x1 = random.randrange(20, 520, 20)
		canvas.data.food7_y1 = random.randrange(20, 520, 20)
		canvas.data.food7_x2 = canvas.data.food7_x1 + 20
		canvas.data.food7_y2 = canvas.data.food7_y1 + 20
		canvas.data.purple_food_flag = False
		canvas.data.purple_food_time = 0
		canvas.data.purple_food_delay = 0
	elif(canvas.data.x1 == canvas.data.food7_x1 and canvas.data.y1 == canvas.data.food7_y1 and canvas.data.x2 == canvas.data.food7_x2 and canvas.data.y2 == canvas.data.food7_y2):
		canvas.data.points += 10
		canvas.data.food7_x1 = random.randrange(20, 520, 20)
		canvas.data.food7_y1 = random.randrange(20, 520, 20)
		canvas.data.food7_x2 = canvas.data.food7_x1 + 20
		canvas.data.food7_y2 = canvas.data.food7_y1 + 20'''

def init():
	canvas.data.delay = 35 #<--- How to change speed
	#Block
	canvas.data.x1 = 240 #Top left X 140
	canvas.data.y1 = 240 #Top left Y 90
	canvas.data.x2 = 260 #Bottom right X 160 
	canvas.data.y2 = 260 #Bottom right Y 110
	canvas.data.color = "green"
	#photo = PhotoImage(file = "ufo.gif")
	#canvas.photo = photo
	#Death Canvas
	canvas.data.death_width = 520
	canvas.data.death_height = 520
	#Canvas
	canvas.data.width = 500
	canvas.data.height = 500
	#Food 1
	canvas.data.food1_x1 = random.randrange(20, 500, 20)
	canvas.data.food1_y1 = random.randrange(20, 500, 20)
	canvas.data.food1_x2 = canvas.data.food1_x1 + 20
	canvas.data.food1_y2 = canvas.data.food1_y1 + 20
	#Food 2
	canvas.data.food2_x1 = random.randrange(20, 500, 20)
	canvas.data.food2_y1 = random.randrange(20, 500, 20)
	canvas.data.food2_x2 = canvas.data.food2_x1 + 20
	canvas.data.food2_y2 = canvas.data.food2_y1 + 20
	#Food 3
	canvas.data.food3_x1 = random.randrange(20, 500, 20)
	canvas.data.food3_y1 = random.randrange(20, 500, 20)
	canvas.data.food3_x2 = canvas.data.food3_x1 + 20
	canvas.data.food3_y2 = canvas.data.food3_y1 + 20
	#Food 4
	canvas.data.food4_x1 = random.randrange(20, 500, 20)
	canvas.data.food4_y1 = random.randrange(20, 500, 20)
	canvas.data.food4_x2 = canvas.data.food4_x1 + 20
	canvas.data.food4_y2 = canvas.data.food4_y1 + 20
	#Food 5
	canvas.data.food5_x1 = random.randrange(20, 500, 20)
	canvas.data.food5_y1 = random.randrange(20, 500, 20)
	canvas.data.food5_x2 = canvas.data.food5_x1 + 20
	canvas.data.food5_y2 = canvas.data.food5_y1 + 20
	#Food 6 disapeares and reapears, worth 5
	canvas.data.food6_x1 = random.randrange(20, 500, 20)
	canvas.data.food6_y1 = random.randrange(20, 500, 20)
	canvas.data.food6_x2 = canvas.data.food6_x1 + 20
	canvas.data.food6_y2 = canvas.data.food6_y1 + 20
	'''#Food 7 disapears, waits, reapears, worth 10
	canvas.data.food7_x1 = random.randrange(20, 520, 20)
	canvas.data.food7_y1 = random.randrange(20, 520, 20)
	canvas.data.food7_x2 = canvas.data.food7_x1 + 20
	canvas.data.food7_y2 = canvas.data.food7_y1 + 20'''
	#Other
	canvas.data.direction = ""
	canvas.data.points = 0
	canvas.data.food_time = 0
	canvas.data.purple_food_time = 0
	canvas.data.purple_food_delay = 0
	canvas.data.purple_food_flag = False
	canvas.data.go_count = 1
	#canvas.data.scores = open(".\pytk_snake_scores.py", "r")
	#canvas.data.scores_out = open(".\pytk_snake_scores.py", "wb")
	#canvas.data.initials = ""
	#canvas.data.initial_count = 0
	#canvas.data.score_name = "%s : %s" % (canvas.data.initials, canvas.data.points)
	#canvas.data.initials = raw_input("Your initials: ")

def main():
	root = Tk()
	global canvas
	canvas = Canvas(root, width = 520, height = 520)
	canvas.pack()
	class Struct(): pass
	canvas.data = Struct()
	init()
	timerFired()
	root.protocol("WM_DELET_WINDOW", close)
	root.bind("<Key>", keyPressed)
	root.mainloop()

main()
