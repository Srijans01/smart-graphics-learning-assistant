import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import tkinter
import os



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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def giveMe():
    
    query = takeCommand().lower()
    if "first" in query or "1st" in query or "one" in query:
        speak("You searched for 2D computer graphics")
        speak("Here is some basic information about 2D graphics")
        speak("2D computer graphics is the computer-based generation of digital images—mostly from two-dimensional models (such as 2D geometric models, text, and digital images) and by techniques specific to them.The word may stand for the branch of computer science that comprises such techniques or for the models themselves.")
        print("2D computer graphics is the computer-based generation of digital images—mostly from two-dimensional models (such as 2D geometric models, text, and digital images) and by techniques specific to them.The word may stand for the branch of computer science that comprises such techniques or for the models themselves.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\2d.png')
            #msg.showinfo('1','2D computer graphics is the computer-based generation of digital images—mostly from two-dimensional models (such as 2D geometric models, text, and digital images) and by techniques specific to them.The word may stand for the branch of computer science that comprises such techniques or for the models themselves.')
            #fourth_win()
    elif "second" in query or "2nd" in query or "two" in query:
        speak("3D computer graphics")
        speak("Here is the basic information about 3D graphics")
        speak("3D computer graphics or three-dimensional computer graphics (in contrast to 2D computer graphics), are graphics that use a three-dimensional representation of geometric data (often Cartesian) that is stored in the computer for the purposes of performing calculations and rendering 2D images. Such images may be stored for viewing later or displayed in real-time.")
        print("3D computer graphics or three-dimensional computer graphics (in contrast to 2D computer graphics), are graphics that use a three-dimensional representation of geometric data (often Cartesian) that is stored in the computer for the purposes of performing calculations and rendering 2D images. Such images may be stored for viewing later or displayed in real-time.")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\3dimg.png')
    elif "third"in query or "3rd" in query or "three" in query:
        speak("Here the the basic information about 3D projections")
        speak("3D projection is any method of mapping three-dimensional points to a two-dimensional plane. As most current methods for displaying graphical data are based on planar (pixel information from several bitplanes) two-dimensional media, the use of this type of projection is widespread, especially in computer graphics, engineering and drafting.")
        print("3D projection is any method of mapping three-dimensional points to a two-dimensional plane. As most current methods for displaying graphical data are based on planar (pixel information from several bitplanes) two-dimensional media, the use of this type of projection is widespread, especially in computer graphics, engineering and drafting.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\3dproj.png')
    elif "fourth" in query or "4th" in query or "fourth" in query:
        speak("Here the the basic information about Alpha compositing")
        speak("In computer graphics, alpha compositing is the process of combining an image with a background to create the appearance of partial or full transparency. It is often useful to render image elements in separate passes, and then combine the resulting multiple 2D images into a single, final image called the composite. For example, compositing is used extensively when combining computer-rendered image elements with live footage.")
        print("n computer graphics, alpha compositing is the process of combining an image with a background to create the appearance of partial or full transparency. It is often useful to render image elements in separate passes, and then combine the resulting multiple 2D images into a single, final image called the composite. For example, compositing is used extensively when combining computer-rendered image elements with live footage.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\alphac.png')
    elif "fifth" in query or "5th" in query or "five" in query:
        speak("Here the the basic information about Anti-aliasing")
        speak("Anti-aliasing may refer to any of a number of techniques to combat the problems of aliasing in a sampled signal such as a digital image or digital audio recording.")
        print("Anti-aliasing may refer to any of a number of techniques to combat the problems of aliasing in a sampled signal such as a digital image or digital audio recording.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\alias.png')
    elif "sixth" in query or "6th" in query or "six" in query:
        speak("Here the the basic information about Bézier curve")
        speak("A Bézier curve (pronounced [bezje] in French) is a parametric curve used in computer graphics and related fields.")
        print("A Bézier curve (pronounced [bezje] in French) is a parametric curve used in computer graphics and related fields.[1] The curve, which is related to the Bernstein polynomial, is named after Pierre Bézier, who used it in the 1960s for designing curves for the bodywork of Renault cars.[2] Other uses include the design of computer fonts and animation.[2] Bézier curves can be combined to form a Bézier spline, or generalized to higher dimensions to form Bézier surfaces.[2] The Bézier triangle is a special case of the latter.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\bzcr.png')
    elif "seventh" in query or "7th" in query or "seven" in query:
        speak("Here the the basic information about Bézier surface")
        speak("Bézier surfaces are a species of mathematical spline used in computer graphics, computer-aided design, and finite element modeling. As with the Bézier curve, a Bézier surface is defined by a set of control points")
        print("Bézier surfaces are a species of mathematical spline used in computer graphics, computer-aided design, and finite element modeling. As with the Bézier curve, a Bézier surface is defined by a set of control points")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\bzs.png')
    elif "eighth" in query or "8th" in query or "eight" in query:
        speak("Here the the basic information about Bilinear interpolation")
        speak("In mathematics, bilinear interpolation is an extension of linear interpolation for interpolating functions of two variables (e.g., x and y) on a rectilinear 2D grid.")
        print("In mathematics, bilinear interpolation is an extension of linear interpolation for interpolating functions of two variables (e.g., x and y) on a rectilinear 2D grid.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\bin.png')
    elif "ninth" in query or "9th" in query or "nine" in query:
        speak("Here the the basic information about Bresenham's line algorithm")
        speak("Bresenham's line algorithm is a line drawing algorithm that determines the points of an n-dimensional raster that should be selected in order to form a close approximation to a straight line between two points.")
        print("Bresenham's line algorithm is a line drawing algorithm that determines the points of an n-dimensional raster that should be selected in order to form a close approximation to a straight line between two points.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\bin.png')
    elif "tenth" in query or "10th" in query or "ten" in query:
        speak("Here the the basic information about Line drawing algorithm")
        speak("A line drawing algorithm is a graphical algorithm for approximating a line segment on discrete graphical media. On discrete media, such as pixel-based displays and printers, line drawing requires such an approximation (in nontrivial cases).")
        print("A line drawing algorithm is a graphical algorithm for approximating a line segment on discrete graphical media. On discrete media, such as pixel-based displays and printers, line drawing requires such an approximation (in nontrivial cases).")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\lal.png')
    elif "eleventh" in query or "11th" in query or "eleven" in query:
        speak("Here the the basic information about Graphical projection")
        speak("Graphical projection is a protocol, used in technical drawing, by which an image of a three-dimensional object is projected onto a planar surface without the aid of numerical calculation.")
        print("Graphical projection is a protocol, used in technical drawing, by which an image of a three-dimensional object is projected onto a planar surface without the aid of numerical calculation.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\gp.png')
    elif "twelfth" in query or "12th" in query or "twelve" in query:
        speak("Here the the basic information about Isometric projection")
        speak("Isometric projection is a method for visually representing three-dimensional objects in two dimensions in technical and engineering drawings. It is an axonometric projection in which the three coordinate axes appear equally foreshortened and the angle between any two of them is 120 degrees.")
        print("Isometric projection is a method for visually representing three-dimensional objects in two dimensions in technical and engineering drawings. It is an axonometric projection in which the three coordinate axes appear equally foreshortened and the angle between any two of them is 120 degrees.")
        speak("Now the rendered image will be displayed in windows photo viewer")
        os.startfile(r'C:\Users\hp\Downloads\tkinter_proj\ip.png')
    elif "ok bye" in query:
        speak("bye sir")
        exit(0)

def wikisearch():
    query = takeCommand().lower()
    speak('Searching ')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)   
def third_win():
    #takeCommand()
    giveMe()
def fourth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top1 = tkinter.Tk()
    top1.title("2D computer graphics")
    top1.geometry('500x200')
    l20=tkinter.Label(top1,text="2D computer graphics is the computer-based generation\n of digital images—mostly from two-dimensional models\n (such as 2D geometric models, text, and digital images)\n and by techniques specific to them.The word may stand for the branch of computer science\n that comprises such techniques or for the models themselves.")
    l20.pack()
def fifth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top2 = tkinter.Tk()
    top2.title("3D computer graphics")
    top2.geometry('500x200')
    l21=tkinter.Label(top2,text="3D computer graphics or three-dimensional computer graphics\n (in contrast to 2D computer graphics), are graphics\n that use a three-dimensional representation of\n geometric data (often Cartesian) that is stored in the computer for the\n purposes of performing calculations and rendering 2D images.\n Such images may be stored for viewing later or displayed in real-time.")
    l21.pack()
def sixth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top3 = tkinter.Tk()
    top3.title("3D projections")
    top3.geometry('500x200')
    l22=tkinter.Label(top3,text="3D projection is any method of mapping three-dimensional points to a \ntwo-dimensional plane. As most current methods for displaying graphical\n data are based on planar (pixel information from several bitplanes) two-dimensional media,\n the use of this type of projection is widespread,\n especially in computer graphics, engineering and drafting.")
    l22.pack()
def seventh_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top4 = tkinter.Tk()
    top4.title("Alpha compositing")
    top4.geometry('500x200')
    l23=tkinter.Label(top4,text="In computer graphics, alpha compositing is the process of combining an image with\n a background to create the appearance of partial or full transparency. It is often\n useful to render image elements in separate passes, and then combine the resulting multiple\n 2D images into a single,final image called the composite.\n For example, compositing is used extensively when combining computer-rendered\n image elements with live footage.")
    l23.pack()
def eighth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top5 = tkinter.Tk()
    top5.title("Anti-aliasing")
    top5.geometry('500x200')
    l24=tkinter.Label(top5,text="Anti-aliasing may refer to any of a number of techniques to combat\n the problems of aliasing in a sampled signal such as\n a digital image or digital audio recording.")
    l24.pack()
def ninth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top6 = tkinter.Tk()
    top6.title("Bézier curve")
    top6.geometry('500x200')
    l25=tkinter.Label(top6,text="A Bézier curve (pronounced [bezje] in French) is a parametric curve used in\n computer graphics and related fields.\nThe curve, which is related to the Bernstein polynomial, is named after Pierre Bézier, who used it \nin the 1960s for designing curves for the bodywork of Renault cars.\nOther uses include the design of computer fonts and animation.\n Bézier curves can be combined to form a Bézier spline, or generalized to higher dimensions\n to form Bézier surfaces.The Bézier triangle is a special case of the latter.")
    l25.pack()
def tenth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top7 = tkinter.Tk()
    top7.title("Bézier surface")
    top7.geometry('500x200')
    l26=tkinter.Label(top7,text="Bézier surfaces are a species of mathematical spline used in computer graphics,\n computer-aided design, and finite element modeling. As with the Bézier curve,\n a Bézier surface is defined by a set of control points")
    l26.pack()
def eleventh_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top8 = tkinter.Tk()
    top8.title("Bilinear interpolation")
    top8.geometry('500x200')
    l27=tkinter.Label(top8,text="In mathematics, bilinear interpolation is an extension of linear interpolation\n for interpolating functions of two variables (e.g., x and y)\n on a rectilinear 2D grid.")
    l27.pack()
def twelfth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top9 = tkinter.Tk()
    top9.title("Bresenham's line algorithm")
    top9.geometry('500x200')
    l28=tkinter.Label(top9,text="Bresenham's line algorithm is a line drawing algorithm that determines the points\n of an n-dimensional raster that should be selected in order to form a\n close approximation to a straight line between two points.")
    l28.pack()
def thirteenth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top10 = tkinter.Tk()
    top10.title("Line drawing algorithm")
    top10.geometry('500x300')
    l29=tkinter.Label(top10,text="A line drawing algorithm is a graphical algorithm for approximating\n a line segment on discrete graphical media. On discrete media, \nsuch as pixel-based displays and printers, line drawing requires such an \napproximation (in nontrivial cases).")
    l29.pack()
def fourteenth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top11 = tkinter.Tk()
    top11.title("Graphical projection")
    top11.geometry('500x300')
    l30=tkinter.Label(top11,text="Graphical projection is a protocol, used in technical drawing,\n by which an image of a three-dimensional object is projected onto a planar surface\n without the aid of numerical calculation.")
    l30.pack()
def fifteenth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    top12 = tkinter.Tk()
    top12.title("Isometric projection")
    top12.geometry('500x300')
    l31=tkinter.Label(top12,text="Isometric projection is a method for visually representing three-dimensional\n objects in two dimensions in technical and engineering drawings. It is an axonometric\n projection in which the three coordinate axes appear equally foreshortened\n and the angle between any two of them is 120 degrees.")
    l31.pack()
def sixteenth_win():
    #img1 = tkinter.PhotoImage(file="bzc.png")
    wikisearch()

window=tkinter.Tk()
window.title("Welcome to second window")
window.geometry('2000x2000')
    
    #takeCommand()
sb = tkinter.Scrollbar(window)  
sb.pack(side ="right", fill ="y")
    #l_02=tkinter.Label(window,text='Program Starts...',relief="solid",font=('arial',20,'bold'),command=open_win).place(x=30,y=70)
b_01=tkinter.Button(window,text="Enable speak",width=12,bg="brown",fg="grey",command=third_win).pack(side="bottom")
b_02=tkinter.Button(window,text="Search other topics",width=20,bg="brown",fg="grey",command=wikisearch).pack(side="bottom")
    #b_02=tkinter.Button(window,text="Search for more topics",width=12,bg="brown",fg="grey",command=fourth_win).pack(side="bottom",padx=500)
l4=tkinter.Label(window,text="WELCOME,THIS IS A SMART GRAPHICS LEARNING ASSISTANT",relief="solid",bg="violet",fg="white",font=("arial",19,"bold")).pack(pady=12)
l5=tkinter.Label(window,text="Which of the following do you want to select-->",relief="solid",bg="MistyRose2",font=("arial",14,"bold")).pack(pady=12.25)
l6=tkinter.Radiobutton(window,text="1.2D computer graphics",font=("arial",10,"underline"),command=fourth_win).pack(pady=12.5)
l7=tkinter.Radiobutton(window,text="2.3D computer graphics",font=("arial",10,"underline"),command=fifth_win).pack(pady=12.75)
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
window.mainloop()
