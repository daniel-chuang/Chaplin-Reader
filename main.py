# In order to build with pyinstaller use this command:
# pyinstaller -F -w --onefile --windowed --add-data "chaplin.gif:." main.py

# Imports
import PySimpleGUI as sg
import time
import re
import os


def Prompt():
    # Setting up themes
    THEMES = ["DarkAmber", "Black", "DarkTeal12", "LightBlue"]
    THEME = 0
    sg.theme(THEMES[THEME])  # Choosing theme

    # Setting up image
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    chaplin = resource_path("./chaplin.gif")

    # Layout for input window
    layout1 = [[sg.Image(chaplin, key="-CHAPLIN GIF-")],
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
                "-CHAPLIN GIF-").UpdateAnimation(chaplin, time_between_frames=100)

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
