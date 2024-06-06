#imports
import pyttsx3
import time
import os
import sys
import wikipedia
import webbrowser
from plyer import notification
import speech_recognition as sr
from pathlib import Path


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


def OpenWebsite(sitename:str):
    engine.say(f'opening {sitename} Sir...')
    webbrowser.open_new_tab(f'{sitename.lower()}.com')
    time.sleep(5)


def FileCreationAndDeletion(CREATE:bool, filepath):
    if CREATE:
        with open(filepath, 'w') as f:
            f.write(" ")

        engine.say("File created Sir")
        print("File created sir...")


    else:
        if os.path.exists(filepath):
            os.remove(filepath)

            engine.say("File Deleted sir.")
            print("File deleted.")

        else:
            engine.say("File does not exists sir.")
            print("File does not exists sir.")


def DirectoryCreationAndDeletion(CREATE:bool, dir_path:str):
    directory_path = Path(dir_path)
    if CREATE:
        if directory_path.is_dir():
            engine.say("Directory already exists sir.")
            print("Directory already exists sir.")

        else:
            os.makedirs(directory_path, exist_ok=True)
            engine.say("Directory created sir.")
            print("Directory created sir.")

    else:
        if directory_path.is_dir():
            engine.say("Directory does not exists sir.")
            print("Directory does not exists sir.")

        else:
            os.rmdir(directory_path)
            engine.say("Directory removed sir.")
            print("Directory removed sir.")


def move_file(filepath:str, new_dir:str):
    if os.path.exists(filepath):
        newpath = os.path.join(new_dir, os.path.basename(filepath))
        os.replace(filepath, newpath)
        engine.say("files replaced sir....")
        print("files replaced sir....")


    else:
        engine.say("file does not exists sir....")
        print("file does not exists sir....")


if __name__ == "__main__":
    notification.notify(
            title = 'Desktop Assistant',
            message = 'Desktop Assistant started.'
        )

    # introduction about the desktop assistant.
    Intro()

    while True:

        queries = take_command() # taking commands from user.
        queries = queries.lower()

        # getting wikipedia info
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

        # opening some of the websites
        elif 'youtube' in queries:
            OpenWebsite(sitename='youtube')


        elif 'google' in queries:
            OpenWebsite(sitename='google')


        elif 'stackoverflow' in queries:
            OpenWebsite(sitename='stackoverflow')

        elif 'codechef' in queries:
            OpenWebsite(sitename='codechef')


        elif 'github' in queries:
            OpenWebsite(sitename='github')


        elif 'leetcode' in queries:
            OpenWebsite(sitename='leetcode')

        # getting current time.
        elif 'time' in queries:
            cuur_time = time.strftime("%H:%M", time.localtime())
            engine.say(cuur_time)
            print(cuur_time)

        # opening VS code.
        elif 'open code' in queries:
            try:
                codepath = "C:\\Users\\sunil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                engine.say('Opening VS code sir..')
                os.startfile(codepath)
            except Exception as e:
                engine.say("Sorry I am unable to start Visual Studio Code sir.")
                continue

        # creating files
        elif "create file" in queries:
            engine.say("Sir please enter the filepath along the with filename.")
            filepath = input("\n Enter the filepath along the with filename :- \n ")
            CREATE = True
            FileCreationAndDeletion(CREATE, filepath)

        # deleting files
        elif "delete file" in queries:
            engine.say("Sir please enter the filepath along the with filename.")
            filepath = input("\n Enter the filepath along the with filename :- \n ")
            CREATE = False
            FileCreationAndDeletion(CREATE, filepath)

        # creating directory
        elif "create directory" in queries:
            engine.say("Sir please enter the directory path along the with filename.")
            dirpath = input("Sir please enter the directory path along the with filename.")
            CREATE = True
            DirectoryCreationAndDeletion(CREATE, dirpath)

        # Deleting directory
        elif 'delete directory' in queries:
            engine.say("Sir please enter the directory path along the with filename.")
            dirpath = input("Sir please enter the directory path along the with filename.")
            CREATE = False
            DirectoryCreationAndDeletion(CREATE, dirpath)

        # Moving files.
        elif 'move file' in queries:
            engine.say("Enter the base file filepath")
            filepath = input("Enter the base file filepath")

            engine.say("Enter the destination file path")
            despath = input("Enter the destination file path")

            move_file(filepath, despath)

        # closing the assistant.
        elif 'exit' in queries or 'quit' in queries:
            outro()
            sys.exit()

        engine.runAndWait()
