# Imports
import PySimpleGUI as sg
import time
import re

THEMES = ["DarkAmber", "Black", "DarkTeal12", "LightBlue"]
THEME = 0
sg.theme(THEMES[THEME]) # Choosing theme

# Layout for input window
layout1 = [ [sg.Image("chaplin.gif", key="-CHAPLIN GIF-")],
	   [sg.Text("Enter some text", key="-PROMPT 1-")],
	   [sg.InputText(key="-TEXT-")],
	   [sg.Text("Reader WPM"), sg.Slider(range=(100, 600), default_value=200, orientation="horizontal", key="-SLIDER-")],
	   [sg.Button("Begin", key="-ENTER-"), sg.Button("Cancel", key="-CANCEL-")] ]

# Create the input window
window = sg.Window("Charlie Chaplin's Assembly Line Reader", layout1)

# Event loop
while True:
	event, values = window.read()
	if event in (sg.WIN_CLOSED, "-CANCEL-", "-ENTER-"):
		if event == "-ENTER-":
			print("You entered ", values["-TEXT-"])
		break

window.close()

# Preparing for the next window - by words version
words = re.split(r"\n| ", values["-TEXT-"])
delay = 60000 / values["-SLIDER-"]

print(words)
TEXT_WIDTH = 40
layout2 = [ [sg.Text(size=(TEXT_WIDTH, 1), key="-TEXT-")] ]
window2 = sg.Window("Charlie Chaplin's Assembly Line Reader", layout2) 
for i in range(len(words)):
	window2.read(timeout=delay)
	window2["-TEXT-"].update(" ".join(words[i:]))

window2.close()
