from Tkinter import *
from tkFileDialog import askopenfilename

spikesCsv = "..."

#spikesCsv = askopenfilename()

root = Tk()
#TkFileDialogExample(root).pack()
root.geometry('150x200+300+200')

a = []

def getSpkiesCsv(event):
	#spikesCsv = askopenfilename()
	spikesCsv = askopenfilename(**self.file_opt)

def getCellNumber(event):
	a.append(text1.get('1.0', END))
	root.quit()

label1 = Label(root, text = "Cell number:")
label1.pack()

text1 = Text(root,height=1,width=15,wrap=WORD)
text1.pack()

buttonSpikesCsv = Button(root, text="File...")
buttonSpikesCsv.bind("<Button-2>", getSpkiesCsv)
buttonSpikesCsv.pack()

label1 = Label(root, text = spikesCsv)
label1.pack()

btn = Button(root, text="OK", width=15,height=3)
btn.bind("<Button-1>", getCellNumber)
btn.pack()

root.mainloop()

print a[0]
#print a[1]
#print a[2]
"""
from Tkinter import *
root=Tk()
text1=Text(root,height=7,width=7,font='Arial 14',wrap=WORD)
text1.pack()
root.mainloop()

print text
"""