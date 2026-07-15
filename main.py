import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import pyjokes

engine=pyttsx3.init()
engine.setProperty("rate",170)

def speak(t):
    print("Jarvis:",t)
    engine.say(t)
    engine.runAndWait()

def wish():
    h=datetime.datetime.now().hour
    if h<12:speak("Good Morning")
    elif h<18:speak("Good Afternoon")
    else:speak("Good Evening")
    speak("I am Jarvis. How can I help you?")

def take():
    r=sr.Recognizer()
    with sr.Microphone() as s:
        audio=r.listen(s)
    try:
        return r.recognize_google(audio,language="en-in").lower()
    except:
        return "none"

if __name__=="__main__":
    wish()
    while True:
        q=take()
        if q=="none":
            continue
        elif "wikipedia" in q:
            speak(wikipedia.summary(q.replace("wikipedia",""),sentences=2))
        elif "open google" in q:
            webbrowser.open("https://google.com")
        elif "open youtube" in q:
            webbrowser.open("https://youtube.com")
        elif "open chatgpt" in q:
            webbrowser.open("https://chatgpt.com")
        elif "time" in q:
            speak(datetime.datetime.now().strftime("%I:%M %p"))
        elif "date" in q:
            speak(datetime.datetime.now().strftime("%d %B %Y"))
        elif "calculator" in q:
            os.system("calc")
        elif "notepad" in q:
            os.system("notepad")
        elif "command prompt" in q:
            os.system("start cmd")
        elif "joke" in q:
            speak(pyjokes.get_joke())
        elif "search google" in q:
            webbrowser.open("https://www.google.com/search?q="+q.replace("search google",""))
        elif "weather" in q:
            speak("Add your OpenWeather API key to enable weather.")
        elif "news" in q:
            speak("Add your NewsAPI key to enable news.")
        elif "ai chat" in q:
            speak("Add your OpenAI API key to enable AI chat.")
        elif q in ["exit","quit","goodbye","stop"]:
            speak("Goodbye")
            break
        else:
            speak("Command not understood.")

