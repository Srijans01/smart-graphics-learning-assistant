#------wishes the user and and searches any query in wikipedia-----
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

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
    print("\n12.Isometric projection")
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

def wikisearch():
    query = takeCommand().lower()
    speak('Searching ')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)  
if __name__ == "__main__":
    wishMe()
    print("Search in wikipedia")
    wikisearch()