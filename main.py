#imports
import pyttsx3
import time
import os
import sys
import webbrowser
import plyer
import speech_recognition as sr

class Main:
    pass

engine = pyttsx3.init('sapi5')

def Intro():
    curr_time = int(time.strftime("%H", time.localtime()))
    if curr_time>=0 and curr_time<12:
        engine.say('Good Morning, Sir!')
        engine.say('I am Your Desktop assistant. How may I help you sir ?')

    elif curr_time >= 12 and curr_time<18:
        engine.say('Good Afternoon, Sir !')
        engine.say('I am Your Desktop assistant. How may I help you sir ?')

    elif curr_time > 18 :
        engine.say("Good Evening, Sir !")
        engine.say('I am Your Desktop assistant. How may I help you sir ?')

    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print('User said :', query)
        return query

    except Exception as e:
        print("Please say that again....")
        engine.say("Please say that again....")
        engine.runAndWait()
        return "None"


if __name__ == "__main__":
    Intro()

    while True:
        queries = take_command()

        if 'exit' in queries or 'quit' in queries:
            sys.exit()

