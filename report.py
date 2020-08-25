import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import os
import tkinter

#-------Sets the engine to sapi5-------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#--------Function to enable the program to speak-----
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#----------Function to wish the user-----------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant Sir. Please tell me how may I help you")
#-------Function to listen and recognize--------
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak(f"User said: {query}")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

#------------Function to speak about the chosen topic------
def giveMe():
    
    query = takeCommand().lower()
    if "first" in query or "1st" in query or "one" in query:
        speak("You searched for 2D computer graphics")
        speak("Here is some basic information about 2D graphics")
        speak("2D computer graphics is the computer-based generation of digital images—mostly from two-dimensional models (such as 2D geometric models, text, and digital images) and by techniques specific to them.The word may stand for the branch of computer science that comprises such techniques or for the models themselves.")
        print("2D computer graphics is the computer-based generation of digital images—mostly from two-dimensional models (such as 2D geometric models, text, and digital images) and by techniques specific to them.The word may stand for the branch of computer science that comprises such techniques or for the models themselves.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\2d.png')
elif "second" in query or "2nd" in query or "two" in query:
        speak("3D computer graphics")
        speak("Here is the basic information about 3D graphics")
        speak("3D computer graphics or three-dimensional computer graphics (in contrast to 2D computer graphics), are graphics that use a three-dimensional representation of geometric data (often Cartesian) that is stored in the computer for the purposes of performing calculations and rendering 2D images. Such images may be stored for viewing later or displayed in real-time.")
        print("3D computer graphics or three-dimensional computer graphics (in contrast to 2D computer graphics), are graphics that use a three-dimensional representation of geometric data (often Cartesian) that is stored in the computer for the purposes of performing calculations and rendering 2D images. Such images may be stored for viewing later or displayed in real-time.")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\3dimg.png')
#-------Function to speak how to use-------
def speakhow():
    speak("To start the program click on START")
    speak("The list of topics will be displayed on clicking START and then the user has to speak the option, for example foe first option say first and so on")
    speak("To see the information click on the topic and the information will be displayed")           
#--------Function to search wikipedia-----
def wikisearch():
    query = takeCommand().lower()
    speak('Searching ')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)  
#------Function to exit-----
def exitt():
    exit(0)
#-----Main window in tkinter-------
root = tkinter.Tk()
root.geometry("1500x1000")
root.minsize(100,500)
root.title("Smart Graphics Learning Assistant") 
f1= tkinter.Frame(root,bg="yellow",borderwidth=7,relief="sunken").pack(side="left",fill="y")
C=tkinter.Canvas(root,bg="blue",height=250,width=300)
fn=tkinter.PhotoImage(file="backg.png")
background_label=tkinter.Label(root,image=fn)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
C.pack()
b2=tkinter.Button(f1,text="QUIT              ",command=exitt,activebackground="red",font="1000",borderwidth="1",relief="solid",justify="center").place(x=100,y=700)
b1=tkinter.Button(f1,text="START          ",command=second_win,activebackground="green",font="1000",borderwidth="1",justify="center",relief="solid").place(x=100,y=500)
b3=tkinter.Button(f1,text="HOW TO USE",command=speakhow,activebackground="orange",font="1000",borderwidth="1",justify="center",relief="solid").place(x=100,y=600)
l = tkinter.Label(root,text="WELCOME TO SMART GRAPHICS LEARNING ASSISTANT",bg="lavender",fg="black",padx=50,pady=50,font=("comicsansms",19,"bold"),borderwidth=10,relief="groove").place(x=360,y=100)
sri = tkinter.Label(root,text="Developed by Ayush Rawat,Srijan Sachdeva,Piyush Yadav",bg="black",fg="white",padx=40,pady=30,font=("comicsansms",10,"bold"),borderwidth=10,relief="groove").place(x=1000,y=700)
root.configure(bg="MistyRose2")
root.mainloop()
#-----Second window-----------
def second_win():
    window=tkinter.Tk()
    window.title("Welcome to second window")
    window.geometry('2000x2000')
    wishMe()
    #takeCommand()
    sb = tkinter.Scrollbar(window)  
    sb.pack(side ="right", fill ="y")
    #l_02=tkinter.Label(window,text='Program Starts...',relief="solid",font=('arial',20,'bold'),command=open_win).place(x=30,y=70)
    b_01=tkinter.Button(window,text="Enable speak",width=12,bg="brown",fg="grey",command=third_win).pack(side="bottom")
    b_02=tkinter.Button(window,text="Search other topics",width=20,bg="brown",fg="grey",command=wikisearch).pack(side="bottom")
    #b_02=tkinter.Button(window,text="Search for more topics",width=12,bg="brown",fg="grey",command=fourth_win).pack(side="bottom",padx=500)
    l4=tkinter.Label(window,text="WELCOME,THIS IS A SMART GRAPHICS LEARNING ASSISTANT",relief="solid",bg="violet",fg="white",font=("arial",19,"bold")).pack(pady=12)
    l5=tkinter.Label(window,text="Which of the following do you want to select-->",relief="solid",bg="MistyRose2",font=("arial",14,"bold")).pack(pady=12.25)
    l6=tkinter.Radiobutton(window,text="1.2D computer graphics",font=("arial",10,"underline"),command=fourth_win).pack(padx=1,pady=12.5,anchor="nw")
    l7=tkinter.Radiobutton(window,text="2.3D computer graphics",font=("arial",10,"underline"),command=fifth_win).pack(padx=1,pady=12.75,anchor="nw")
    l8=tkinter.Radiobutton(window,text="3.3D projection",font=("arial",10,"underline"),command=sixth_win).pack(pady=13)
    l9=tkinter.Radiobutton(window,text="4.Alpha compositing",font=("arial",10,"underline"),command=seventh_win).pack(pady=13.25)
    l10=tkinter.Radiobutton(window,text="5.Anti-aliasing",font=("arial",10,"underline"),command=eighth_win).pack(pady=13.5)
    l11=tkinter.Radiobutton(window,text="6.Bézier curve",font=("arial",10,"underline"),command=ninth_win).pack(pady=13.75)
    l12=tkinter.Radiobutton(window,text="7.Bézier surface",font=("arial",10,"underline"),command=tenth_win).pack(pady=14)
    l13=tkinter.Radiobutton(window,text="8.Bilinear interpolation",font=("arial",10,"underline"),command=eleventh_win).pack(pady=14.25)
    l14=tkinter.Radiobutton(window,text="9.Bresenham's line algorithm",font=("arial",10,"underline"),command=twelfth_win).pack(pady=14.5)
    l15=tkinter.Radiobutton(window,text="10.Line drawing algorithm",font=("arial",10,"underline"),command=thirteenth_win).pack(pady=14.75)
    l16=tkinter.Radiobutton(window,text="11.Graphical projection",font=("arial",10,"underline"),command=fourteenth_win).pack(pady=15)
    l17=tkinter.Radiobutton(window,text="12.Isometric projection",font=("arial",10,"underline"),command=fifteenth_win).pack(pady=15.25)
#--------------Text pop up window-------
def fourth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top1 = tkinter.Tk()
    top1.title("2D computer graphics")
    top1.geometry('500x200')
    l20=tkinter.Label(top1,text="2D computer graphics is the computer-based generation\n of digital images—mostly from two-dimensional models\n (such as 2D geometric models, text, and digital images)\n and by techniques specific to them.The word may stand for the branch of computer science\n that comprises such techniques or for the models themselves.")
    l20.pack()