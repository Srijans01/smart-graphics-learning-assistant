import tkinter
import datetime
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


root = tkinter.Tk()
root.geometry("1500x1000")
root.minsize(100,500)
#root.iconbitmap(r'voice_command.ico')
root.title("Smart Graphics Learning Assistant")

#img = tkinter.PhotoImage(file="bzc.png")
#backimg=tkinter.PhotoImage(file="eqi.png")
#im_01=tkinter.PhotoImage(file="2d.png")
#U=tkinter.Label(root,image=backimg)
#U.place(x=0,y=0,relwidth=1,relheight=1)
#w=tkinter.Entry(root,bg="red").pack(anchor="nw",padx=90,side="left")
"""
cv_img = cv2.imread("bg2.png")
#height, width, no_channels = cv_img.shape
canvas = tkinter.Canvas(root, width = 1000, height = 500)
canvas.pack()
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
canvas.create_image(0, 0, image=backimg, anchor=tkinter.NW)
"""
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant Sir. Please tell me how may I help you")
def second_win():
    wishMe()
def exitt():
    exit(0)
def speakhow():
    speak("To start the program click on START")
    speak("The list of topics will be displayed on clicking START and then the user has to speak the option, for example foe first option say first and so on")
    speak("To see the information click on the topic and the information will be displayed")           
f1= tkinter.Frame(root,bg="yellow",borderwidth=7,relief="sunken").pack(side="left",fill="y")
#l1=tkinter.Label(f1,text="SMART GRPHIC LEARNING ASSISTANT",bg="blue").pack(side="left")
C=tkinter.Canvas(root,bg="blue",height=250,width=300)
fn=tkinter.PhotoImage(file="orange.png")
background_label=tkinter.Label(root,image=fn)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
C.pack()
b2=tkinter.Button(f1,text="QUIT",command=exitt).pack(side="bottom")
b1=tkinter.Button(f1,text="START",command=second_win).pack(side="bottom")
b3=tkinter.Button(f1,text="HOW TO USE",command=speakhow).pack(side="bottom")
#x1=tkinter.Label(image=backimg).pack()
l = tkinter.Label(root,text="WELCOME TO SMART GRAPHICS LEARNING ASSISTANT",bg="red",fg="white",padx=50,pady=50,font=("comicsansms",19,"bold"),borderwidth=10,relief="groove").pack(side="top",pady=100)
sri = tkinter.Label(root,text="Created by Ayush Rawat,Piyush Yadav,Srijan Sachdeva",bg="blue",fg="white",padx=50,pady=50,font=("comicsansms",19,"bold"),borderwidth=10,relief="groove").pack(side="bottom",padx=110)
#m = tkinter.Label(root,image=img).pack(side="right",fill="x")
root.configure(bg="MistyRose2")
root.mainloop()