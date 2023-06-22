#imports
import pyttsx3
import time
import os
import sys
import wikipedia
import webbrowser
from plyer import notification
import speech_recognition as sr


engine = pyttsx3.init('sapi5')


def Intro():
    curr_time = int(time.strftime("%H", time.localtime()))
    if curr_time>=0 and curr_time<12:
        engine.say('Good Morning, Sir!')
        engine.say('I am Your Desktop Assistant. How may I help you sir ?')

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


def outro():
    engine.say('Thanks for Using me.')
    engine.say('This is me your desktop assistant signing off sir.')
    engine.runAndWait()


if __name__ == "__main__":
    notification.notify(
            title = 'Desktop Assistant',
            message = 'Desktop Assistant started.'
        )

    Intro()

    while True:

        queries = take_command()
        queries = queries.lower()

        if 'wikipedia' in queries:
            try:
                queries = queries.replace("wikipedia", "")
                summary = wikipedia.summary(queries, sentences=2)
                print(summary)
                engine.say(summary)
            except Exception as e:
                print("Sorry Sir I couldn't recognized that. Please Say that again... ")
                engine.say("Sorry Sir I couldn't recognized that. Please Say that again... ")
                continue


        elif 'youtube' in queries:
            engine.say('opening Youtube Sir...')
            webbrowser.open_new_tab('youtube.com')
            time.sleep(5)


        elif 'google' in queries:
            engine.say('opening Google Sir...')
            webbrowser.open_new_tab('google.com')


        elif 'stackoverflow' in queries:
            engine.say('opening Stackoverflow Sir...')
            webbrowser.open_new_tab('stackoverflow.com')


        elif 'codechef' in queries:
            engine.say('opening codechef Sir...')
            webbrowser.open_new_tab('codechef.com')


        elif 'github' in queries:
            engine.say('opening github Sir...')
            webbrowser.open_new_tab('github.com')


        elif 'leetcode' in queries:
            engine.say('opening leetcode Sir...')
            webbrowser.open_new_tab('leetcode.com')


        elif 'music' in queries:
            pass

        elif 'the time' in queries:
            cuur_time = time.strftime("%H:%M", time.localtime())
            engine.say(cuur_time)
            print(cuur_time)


        elif 'open code' in queries:
            try:
                codepath = "C:\\Users\\sunil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                engine.say('Opening VS code sir..')
                os.startfile(codepath)
            except Exception as e:
                engine.say("Sorry I am unable to start Visual Studio Code sir.")
                continue


        elif 'exit' in queries or 'quit' in queries:
            outro()
            sys.exit()

        engine.runAndWait()
