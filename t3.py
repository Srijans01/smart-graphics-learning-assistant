#----------Identifies what the user says and how our program works-----
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
def speakhow():
    speak("To start the program click on START")
    speak("The list of topics will be displayed on clicking START and then the user has to speak the option, for example foe first option say first and so on")
    speak("To see the information click on the topic and the information will be displayed")
if __name__ == "__main__":
    takeCommand()
    speakhow()