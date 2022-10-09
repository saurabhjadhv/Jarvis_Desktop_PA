from http import server
from winreg import QueryValue
import pyttsx3
import webbrowser
import speech_recognition as sr
import os
import datetime
import webbrowser
import wikipedia
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)  # engine will speak
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        print("Good morning")

    elif (hour >= 12) and (hour <= 18):
        print("Good Afternoon")

    else:
        print("Good evening")

    speak("I am Jarvis, Boss How may I help You")


def takeCommand():
    # It takes microphone input from the user and return string output.
    r = sr.Recognizer()    # Recognizer class will help to recognize the audio.
    with sr.Microphone() as source:
        print("Listening...")
        # seconds of non speaking audio considered complete. (gap of 1s)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...!")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saurabhjadhav150@gmail.com', 'lmdheyjztsswqfwb')
    server.sendmail('saurabhjadhav150@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    WishMe()

    while 1:
        # converting takecommand into lower case.
        # to convert it into lowercase and match the query.
        query = takeCommand().lower()

    # logic to executing task based on query.
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.Youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            code_path = "C:\\Users\\ANKITA JADHAV\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)


        elif 'mail to saurabh' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "saurabhjadhav150@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent !")

            except Exception as e:
                print(e)
                print("sorry my friend saurabh bhai, I am not able to sent email")
