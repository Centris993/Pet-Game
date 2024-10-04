#Evan Mogford 3rd period

#import and the important bits
import random
import time
import tkinter as tk
from tkinter import ttk

#makes tmp fuctions for buttons
def test():
    pass

#the class to hold all part of the pet
class pet:
    #pet stats
	fullness = 50
	weight = 80
	energy = 100
	money = 100
	name = ""
	#pets own window
	root = tk.Tk()
	root.geometry("720x600")
	frame = ttk.Frame(root, width=500, height=500, padding = 10)
	frame.grid(column=1, row=1)

	def __init__(self):
		self.name_set()
		self.root.mainloop()

	#quit option
	quit_frame = ttk.Frame(root,width=50)
	quit_frame.grid(column=1, row=2)
	close = tk.Button(quit_frame, text = "quit", width = 31, height = 5, command = root.destroy).grid(column=1,row=1)
	
	#top text
	big_label = tk.Label(root, text = 'Welcome to my simulator').grid(column=1,row=0)
	
	#make it easy to change the top text
	def main_label(self, str):
		self.big_label = tk.Label(self.root, text = str, width= 30).grid(column=1,row=0)
	
	#shows all the stats on the side
	status = ttk.Frame(root, width= 100, padding = 10)
	status.grid(column=0, row=1)
	
	#set the name
	def name_set(self):
		#make the frame
		name_frame = ttk.Frame(self.root, padding = 10)
		name_frame.grid(column=1, row=1)

		#to close the window and open the normal one, also assigns the name var
		def submit_name():
			self.name = name_var.get()
			name_frame.destroy()
			self.main_menu()
			title.destroy()
			name_get.destroy()
			submit_it.destroy()
			self.update_stats()

		#label, entry box, and submit button
		title = tk.Label(self.frame, text = "pet name:")
		title.grid(column= 0, row= 0)
		name_var = tk.StringVar()
		name_get = tk.Entry(self.frame, textvariable= name_var)
		name_get.grid(column=1,row=0)
		submit_it = tk.Button(self.frame, text = "submit", command = submit_name)
		submit_it.grid(column=1,row=1)

	#make the main menu
	def main_menu(self):
		C1 = tk.Button(self.frame, text = "feed", width=15, height=10, command=self.feed).grid(column = 0, row = 0) 
		C2 = tk.Button(self.frame, text = "sleep", width=15, height=10, command =self.sleep).grid(column=1, row=0)
		C3 = tk.Button(self.frame, text = "play", width = 15, height=10, command = self.play).grid(column=1,row=1)
		C4 = tk.Button(self.frame, text = "gamble", width = 15, height=10, command = self.gamble).grid(column=0,row=1)
		

	#updates all the stats in the stat window
	def update_stats(self):
		status_fullness = tk.Message(self.status, text = ("fullness:" , self.fullness, "%"), width= 90).grid(column=0,row=0)
		status_energy = tk.Message(self.status, text = ("energy:", self.energy, "%"), width= 90).grid(column=0, row=1)
		status_weight = tk.Message(self.status, text = ("weight:", self.weight, "lb"), width= 90).grid(column=0, row=2)
		status_money = tk.Message(self.status, text = ("money: %", self.money), width= 90).grid(column=0, row=3)

	#check if any stat gets too low and causes the pet to leave
	def death(self):
		if self.fullness <= 0 or self.weight <= 0 or self.weight > 200 or self.energy <= 0 or self.money <= 0:
			death_frame = ttk.Frame(self.root, width=500, height = 500, padding = 10)
			death_frame.grid(column=1, row=1)
			self.big_label = tk.Label(self.root, text = (self.name + "left you for someone who treats them better"), width = 70).grid(column = 1, row = 0)
			close = tk.Button(death_frame, text = "quit", width = 30, height = 20, command = self.root.destroy).grid(column=1, row = 1)
		else:
			pass

	#main function to act as the "loop" to lower the stats when anything happens, then cheaks if it dies
	def game_tick(self):
		self.fullness -= 10
		self.weight -= 2
		self.energy -=10
		self.money += 10
		self.update_stats()

	#for the functions that dont open a new frame, its easier to have this that removes the base frame and stuff
	def regular_death(self):
		self.game_tick()
		if self.fullness <= 0 or self.weight <= 0 or self.weight > 200 or self.energy <= 0 or self.money <= 0:
			self.frame.destroy()
			death_frame = ttk.Frame(self.root, width=500, height = 500, padding = 10)
			death_frame.grid(column=1, row=1)
			self.big_label = tk.Label(self.root, text = (self.name + " left you for someone who treats them better"), width = 70).grid(column = 1, row = 0)
			close = tk.Button(death_frame, text = "quit", width = 30, height = 20, command = self.root.destroy).grid(column=1, row = 1)

		
	
		
	#main fuction when feeding the pet
	def feed(self):
		#make the food menu
		food_frame = ttk.Frame(self.root, width=500, height= 500, padding = 10)
		food_frame.grid(column=1, row=1)

		#death while in the food menu b/c it's a different frame
		def death():
			self.game_tick()
			if self.fullness <= 0 or self.weight <= 0 or self.weight > 200 or self.energy <= 0 or self.money <= 0:
				food_frame.destroy()
				death_frame = ttk.Frame(self.root, width=500, height = 500, padding = 10)
				death_frame.grid(column=1, row=1)
				self.big_label = tk.Label(self.root, text = (self.name + " left you for someone who treats them better"), width = 70).grid(column = 1, row = 0)
				close = tk.Button(death_frame, text = "quit", width = 30, height = 20, command = self.root.destroy).grid(column=1, row = 1)
			else:
				pass

		#one tick
		death()
		

		#close the frame
		def remove():
			food_frame.destroy()

		#different foods, different vaule adjustments
		def premium_feed():
			if self.fullness < 100:
				self.fullness = 100
				self.money -= 20
				self.weight += 2
				status_fullness = tk.Message(self.status, text = ("fullness:" , self.fullness, "%"), width= 100).grid(column=0,row=0)
				remove()
			else:
				self.main_label(self.name + " is too full to eat")
				time.sleep(22)
				remove()
		def regular_feed():
			if self.fullness <= 60:
				self.fullness +=40
				self.money -= 10
				status_fullness = tk.Message(self.status, text = ("fullness:" , self.fullness, "%"), width= 100).grid(column=0,row=0)
				remove()
			else:
				self.main_label(self.name + " is too full to eat")
				time.sleep(22)
				remove()
		def cheap_feed():
			if self.fullness <= 80:
				self.fullness += 20
				self.money -=5
				status_fullness = tk.Message(self.status, text = ("fullness:" , self.fullness, "%"), width= 100).grid(column=0,row=0)
				remove()
			else:
				self.main_label(self.name + " is too full to eat")
				time.sleep(.2)
				remove()
		
		#the main buttons to feed
		premium = tk.Button(food_frame, text = "Premium Food \n -$20", width=15, height=10, command = premium_feed).grid(column=0, row=0)
		regular = tk.Button(food_frame, text = "Regular Food \n -$10", width=15, height=10, command = regular_feed).grid(column=1, row=0)
		cheap = tk.Button(food_frame, text = "cheap Food \n -$5", width=15, height=10, command = cheap_feed).grid(column=0, row=1)

	#sleep action, raises energy	
	def sleep(self):
		self.regular_death()
		ran = random.randrange(0,10)
		if ran == 1:
			self.main_label(self.name + " could not fall asleep")
		elif self.energy <= 70:
			self.main_label(self.name +" had a good nap")
			self.energy += 30
		else:
			self.main_label(self.name + " was too energized to sleep")

	#play, lowers weight at the cost of energy and fullness
	def play(self):
		self.regular_death()
		ran = random.randrange(0,10)
		if ran == 1:
			self.main_label(self.name +" Had to be cleaned")
			self.money -=50
		elif ran != 1:
			self.main_label(self.name +" had fun playing")
		self.energy -= 30
		self.weight -=10
		self.fullness -=10

	#gamble, all gamblers quit right before their big win.....
	def gamble(self):
		self.game_tick()
		ran = random.randrange(0,500)
		if ran == 1:
			self.main_label("you win $50,000!")
			self.money += 50000
		else:
			self.main_label("you didn't win...")
			self.money -= 10	


#valids any numerical inputs
#do i even need this?
#just keep it here
def valid(strInput):
	output = input(strInput)
	#Use the .isnumeric() command on string
	while output.isnumeric() is False:
		output = input("try again:")
	return(output)