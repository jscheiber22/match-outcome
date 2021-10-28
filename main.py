'''
	A script to take the possible match ups of a week of football and output all possible winners of each game.
'''

import tkinter as tk
from tkinter import ttk
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

		self.OFTextFields = []
		self.checkButtons = []

		# Creates right side of panel for teams out of favor
		tk.Label(master=self.window, text="Out of Favor:").grid(row=0, column=0)
		for x in range(1,9):
			text = tk.Entry(master=self.window, width=20)
			text.grid(row=x, column=0, sticky='ne')
			text.bind("<Return>", self.outputSheet)
			button = ttk.Checkbutton(master=self.window)
			button.grid(row=x, column=2, sticky='e')
			self.OFTextFields.append(text)
			self.checkButtons.append(button)

		# Submit button
		tk.Button(self.window, text = 'SUBMIT', command=self.outputSheet).grid(row=9, column=1, sticky='n')

		self.window.mainloop()


	def outputSheet(self, event = None):
		vsTeams = []
		# adds all checked boxes to list
		for x in range(0, 8):
			if self.checkButtons[x].instate(['selected']):
				vsTeams.append(self.OFTextFields[x].get())


		# this is for 2 teams winning, add for x in range(0, current team winning count) before for team in vsteams so it will append other teams too
		finalteams = []
		columnFiller = []
		columnFiller += vsTeams
		for x in range(0, 75):
			columnFiller += ['']
		df = pd.DataFrame(pd.Series(columnFiller))

		# works for any combo of 2 teams winning \/\/\/

		if len(vsTeams) >= 2:
			for x in range(0, len(vsTeams)):
				tempTeams = []
				for team in vsTeams:
					tempPair = sorted([vsTeams[x], team])
					if len(set(tempPair)) == len(tempPair) and tempPair not in finalteams and tempPair not in tempTeams:
						tempTeams.append(tempPair)
				finalteams += tempTeams

			df['Two Winners'] = pd.Series(finalteams)
			df['Two Winners']
			


		if len(vsTeams) >= 3:
			finalteams = []
			# working for combo of 3
			for x in range(0, len(vsTeams)):
				tempTeams = []
				for team3 in vsTeams:
					for team in vsTeams:
						tempPair = sorted([vsTeams[x], team, team3])
						if len(set(tempPair)) == len(tempPair) and tempPair not in finalteams and tempPair not in tempTeams:
							tempTeams.append(tempPair)
				finalteams += tempTeams

			df['Three Winners'] = pd.Series(finalteams)
			


		if len(vsTeams) >= 4:
			finalteams = []
			# working for combo of 4
			for x in range(0, len(vsTeams)):
				tempTeams = []
				for team3 in vsTeams:
					for team4 in vsTeams:
						for team in vsTeams:
							tempPair = sorted([vsTeams[x], team, team3, team4])
							if len(set(tempPair)) == len(tempPair) and tempPair not in finalteams and tempPair not in tempTeams:
								tempTeams.append(tempPair)
				finalteams += tempTeams

			df['Four Winners'] = pd.Series(finalteams)
			

		if len(vsTeams) >= 5:
			finalteams = []
			# working for combo of 4
			for x in range(0, len(vsTeams)):
				tempTeams = []
				for team3 in vsTeams:
					for team4 in vsTeams:
						for team5 in vsTeams:
							for team in vsTeams:
								tempPair = sorted([vsTeams[x], team, team3, team4, team5])
								if len(set(tempPair)) == len(tempPair) and tempPair not in finalteams and tempPair not in tempTeams:
									tempTeams.append(tempPair)
				finalteams += tempTeams

			df['Five Winners'] = pd.Series(finalteams)
			

		if len(vsTeams) >= 6:
			finalteams = []
			# working for combo of 4
			for x in range(0, len(vsTeams)):
				tempTeams = []
				for team3 in vsTeams:
					for team4 in vsTeams:
						for team5 in vsTeams:
							for team6 in vsTeams:
								for team in vsTeams:
									tempPair = sorted([vsTeams[x], team, team3, team4, team5, team6])
									if len(set(tempPair)) == len(tempPair) and tempPair not in finalteams and tempPair not in tempTeams:
										tempTeams.append(tempPair)
				finalteams += tempTeams

			df['Six Winners'] = pd.Series(finalteams)
			

		if len(vsTeams) >= 7:
			finalteams = []
			# working for combo of 4
			for x in range(0, len(vsTeams)):
				tempTeams = []
				for team3 in vsTeams:
					for team4 in vsTeams:
						for team5 in vsTeams:
							for team6 in vsTeams:
								for team7 in vsTeams:
									for team in vsTeams:
										tempPair = sorted([vsTeams[x], team, team3, team4, team5, team6, team7])
										if len(set(tempPair)) == len(tempPair) and tempPair not in finalteams and tempPair not in tempTeams:
											tempTeams.append(tempPair)
				finalteams += tempTeams

			df['Seven Winners'] = pd.Series(finalteams)
			

		if len(vsTeams) >= 8:
			finalteams = []
			# working for combo of 4
			for x in range(0, len(vsTeams)):
				tempTeams = []
				for team3 in vsTeams:
					for team4 in vsTeams:
						for team5 in vsTeams:
							for team6 in vsTeams:
								for team7 in vsTeams:
									for team8 in vsTeams:
										for team in vsTeams:
											tempPair = sorted([vsTeams[x], team, team3, team4, team5, team6, team7, team8])
											if len(set(tempPair)) == len(tempPair) and tempPair not in finalteams and tempPair not in tempTeams:
												tempTeams.append(tempPair)
				finalteams += tempTeams

			df['Eight Winners'] = pd.Series(finalteams)
			



		# combinations = product(*vsTeams)

		# df = pd.DataFrame(list(combinations))
		print('Outputting combinations to file: combinations' + str(len(os.listdir('.'))) + '.csv\n')
		df.to_csv('combinations' + str(len(os.listdir('.'))) + '.csv')





if __name__ == '__main__':
	MatchOutcome()