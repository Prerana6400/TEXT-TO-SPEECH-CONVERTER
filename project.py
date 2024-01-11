from tkinter import *
from gtts import gTTS
import os

root = Tk()
canvas= Canvas(root,width=300,height=400)
canvas.pack(side="bottom")


title=Label(root,text=" USER INPUT TO SPEECH CONVERTER" ,fg="white",bg="black" , font=("Arial",20))
title.pack(side="top")
    
def texttospeech() :
    text= entry.get()
    language='en'
    output=gTTS(text=text,lang=language,slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")
entry = Entry(root,font=("Arial",30))
canvas.create_window(200,200,window=entry)

button =Button(text="START",font=("Arial",30),command=texttospeech)

canvas.create_window(200,300,window=button)

root.mainloop()