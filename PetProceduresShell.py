import random
import time
import tkinter as tk
from tkinter import ttk
# Remember:
	# trigger some special events randomly
	# we can ONLY affect the primary stat in the procedure
		#since that is the only one represented by a parameter
	# at least 1 procedure should have more options for the user

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
		name_frame = ttk.Frame(self.root, padding = 10).grid(column=1, row=1)

		#to close the window and open the normal one
		def submit_name():
			name_frame.destroy()
			self.main_menu()

		#all the buttons and stuff
		title = tk.Label(self.frame, text = "pet name:").grid(column= 0, row= 0)
		name_var = tk.StringVar()
		name_get = tk.Entry(self.frame, textvariable= name_var).grid(column=1,row=0)
		self.name = name_var.get()
		submit_it = tk.Button(self.frame, text = "submit", command = submit_name).grid(column=1,row=1)
	def main_menu(self):
		C1 = tk.Button(self.frame, text = "feed", width=15, height=10, command=self.feed).grid(column = 0, row = 0) 
		C2 = tk.Button(self.frame, text = "sleep", width=15, height=10, command =self.sleep).grid(column=1, row=0)
		close = tk.Button(self.frame, text = "quit", width = 15, height = 10, command = self.root.destroy).grid(column=1,row=1)

	def update_stats(self):
		status_fullness = tk.Message(self.status, text = ("fullness:" , self.fullness, "%"), width= 100).grid(column=0,row=0)
		status_energy = tk.Message(self.status, text = ("energy:", self.energy, "%"), width= 100).grid(column=0, row=1)
		status_weight = tk.Message(self.status, text = ("weight:", self.weight, "lb"), width= 100).grid(column=0, row=2)
		status_money = tk.Message(self.status, text = ("money: $", self.money), width= 100).grid(column=0, row=3)

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
		
	
		
	#main fuction when feeding the pet
	def feed(self):
		#make the food menu
		food_frame = ttk.Frame(self.root, width=500, height= 500, padding = 10)
		food_frame.grid(column=1, row=1)

		#death while in the food menu
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

		#different foods
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

		
	def sleep(self):
		self.game_tick()
		ran = random.randrange(0,10)
		if ran == 1:
			self.main_label(self.name + " could not fall asleep")
		elif self.energy <= 70:
			self.main_label(self.name +" had a good nap")
			self.energy += 30
		else:
			self.main_label(self.name + " was too energized to sleep")




'''(4) CREATE at least 2 more actions/procedures'''

#valids any numerical inputs
#do i even need this?
#just keep it here
def valid(strInput):
	output = input(strInput)
	#Use the .isnumeric() command on string
	while output.isnumeric() is False:
		output = input("try again:")
	return(output)