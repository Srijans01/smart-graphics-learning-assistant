#-------------Gives information about the topics-------
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def wishMe():
    speak("I am your assistant Sir. Please tell me how may I help you")
    speak("WELCOME,THIS IS A SMART GRAPHICS LEARNING ASSISTANT")      
    print("Which of the following do you want to select-->")
    speak("Which of the following do you want to select-->")
    print("\n1.2D computer graphics")
    print("\n2.3D computer graphics")
    print("\n3.3D projection")
    print("\n4.Alpha compositing")
    print("\n5.Anti-aliasing")
    print("\n6.Bézier curve")
    print("\n7.Bézier surface")
    print("\n8.Bilinear interpolation")
    print("\n9.Bresenham's line algorithm")
    print("\n10.Line drawing algorithm")
    print("\n11.Graphical projection")
    print("\n12.Isometric projection")        #print("WELCOME,WHAT DO YOU WANT TO LEARN")
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

if __name__ == "__main__":
    wishMe()
    giveMe()
