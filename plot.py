import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename

spikesTime = []
spikesData = []

Tk().withdraw() 
spikesCsv = askopenfilename()

with open(spikesCsv, 'rb') as spikes:
	reader = csv.reader(spikes, delimiter=',')
	for row in reader:
		spikesTime.append(row[0])
		spikesData.append(row[cellNumber])

