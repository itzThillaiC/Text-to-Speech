
# Importing Libraries
from logging import root
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initializing Window metrics
root = Tk()
root.geometry("400*350")
root.configure(bg='white')
root.title("TC's Text-to-Speech")

Label(root, text="TEXT_TO_SPEECH", font="arial 30 bold", bg='white smoke').pack()
Label(text="DataFlair", font='arial 20 bold',
      bg='white smoke', width='20').pack(side='bottom')

Txt = StringVar()
Label(root, text="Enter Text", font='arial 20 bold',
      bg='white smoke').place(x=20, y=60)

entry_field = Entry(root, textvariable=Txt, width='50')
entry_field.place(x=20, y=100)


# TTS function
def Text_to_Speech():
    Msg = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('Text-audio.mp3')
    playsound('Text-audio.mp3')


# Exit
def Exit():
    root.destroy()


# Reset
def reset():
    Txt.set("")
