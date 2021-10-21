'''
	A script to take the possible match ups of a week of football and output all possible winners of each game.
'''

import tkinter as tk
from itertools import product
import pandas as pd
from itertools import product
import os


class MatchOutcome:

	def __init__(self):

		# Tkinter window setup for inputting teams:
		self.window = tk.Tk()

		self.window.rowconfigure(list(range(0,10)), minsize = 50, weight = 1)
		self.window.columnconfigure(list(range(0,2)), minsize = 50, weight = 1)

		self.IFTextFields = []

		# Creates left side of panel for teams in favor
		tk.Label(master=self.window, text="In Favor:").grid(row=0, column=0)
		for x in range(1,9):
			text = tk.Entry(master=self.window, width=30)
			text.grid(row=x, column=0, sticky='nw')
			text.bind("<Return>", self.outputSheet)
			self.IFTextFields.append(text)

		self.OFTextFields = []

		# Creates right side of panel for teams out of favor
		tk.Label(master=self.window, text="Out of Favor:").grid(row=0, column=2)
		for x in range(1,9):
			text = tk.Entry(master=self.window, width=30)
			text.grid(row=x, column=2, sticky='ne')
			text.bind("<Return>", self.outputSheet)
			self.OFTextFields.append(text)

		# Submit button
		tk.Button(self.window, text = 'SUBMIT', command=self.outputSheet).grid(row=9, column=1, sticky='n')

		self.window.mainloop()


	def outputSheet(self, event = None):
		vsTeams = []
		for x in range(0, 8):
			vsTeams.append([self.IFTextFields[x].get(), self.OFTextFields[x].get()]) # creates a list that looks like [(team1, team2), (team3, team4)] for future processing
		combinations = product(*vsTeams)

		df = pd.DataFrame(list(combinations))
		df.to_csv('combinations' + str(len(os.listdir('.'))) + '.csv')





if __name__ == '__main__':
	MatchOutcome()