# Imports
import PySimpleGUI as sg
import time
import re


def Prompt():
    # Setting up themes
    THEMES = ["DarkAmber", "Black", "DarkTeal12", "LightBlue"]
    THEME = 0
    sg.theme(THEMES[THEME])  # Choosing theme

    # Layout for input window
    layout1 = [[sg.Image("chaplin.gif", key="-CHAPLIN GIF-")],
               [sg.Button("Toggle Gif", key="-TOGGLE CHAPLIN-")],
               [sg.Text("Enter some text", key="-PROMPT 1-")],
               [sg.InputText(key="-TEXT-")],
               [sg.Text("Reader WPM"), sg.Slider(range=(100, 600),
                                                 default_value=200, orientation="horizontal", key="-SLIDER-")],
               [sg.Radio("Assembly Line", "-RADIO-", key="-ASSEMBLY LINE-", default=True), sg.Radio("Single Word",
                                                                                                    "-RADIO-", key="-SINGLE WORD-"), sg.Radio("Highlight Word", "-RADIO-", key="HIGHLIGHT WORD-")],
               [sg.Button("Begin", key="-ENTER-"), sg.Button("Exit", key="-EXIT-")]]

    # Create the input window
    window = sg.Window(
        "Charlie Chaplin's Assembly Line: Speed Reader", layout1, margins=(40, 40))

    # Event loop
    run_gif = True
    while True:
        event, values = window.read(timeout=100)

        # Go to the next frame of the gif if run_gif is True
        if run_gif:
            window.FindElement(
                "-CHAPLIN GIF-").UpdateAnimation("chaplin.gif", time_between_frames=100)

        # Toggles whether or not the gif is run
        if event == "-TOGGLE CHAPLIN-":
            if run_gif:
                run_gif = False
            else:
                run_gif = True

        # Checks if the user exited the application
        if event in (sg.WIN_CLOSED, "-EXIT-"):
            quit()
            break

        # Checks if the user is continuing
        if event in ("-ENTER-"):
            if values["-TEXT-"] == "":
                sg.popup("You need to enter something first!")
            else:
                break

    window.close()
    return values


def Prep(values):
    # Preparing for the next window - by words version
    try:
        words = re.split(r"\n| ", values["-TEXT-"])
    except TypeError:
        sg.popup("Invalid Input")
        words = ""

    delay = 60000 / values["-SLIDER-"]

    print(words)
    return words, delay

def AssemblyLine(words, delay):
    TEXT_WIDTH = 40
    
    layout = [[sg.Text(size=(TEXT_WIDTH, 1), key="-TEXT-")]]
    window = sg.Window("Charlie Chaplin's Assembly Line Reader", layout, margins=(100, 100))
    for i in range(len(words)):
        window.read(timeout=delay)
        window["-TEXT-"].update(" ".join(words[i:]))

    window.close()

def SingleWord(words, delay):
    TEXT_WIDTH = 20
    layout = [[sg.Text(size=(TEXT_WIDTH, 1), key="-TEXT-", justification="center")]]
    window = sg.Window("Charlie Chaplin's Assembly Line Reader", layout, margins=(100, 100))
    for i in range(len(words)):
        window.read(timeout=delay)
        window["-TEXT-"].update(" ".join(words[i])) 

values = Prompt()
words, delay = Prep(values)
if values["-ASSEMBLY LINE-"]:
    AssemblyLine(words, delay)
if values["-SINGLE WORD-"]:
    SingleWord(words, delay)
