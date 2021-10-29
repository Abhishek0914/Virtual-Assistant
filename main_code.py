import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import youtubesearchpython as ysp
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

def takecommand():
    global r
    r=sr.Recognizer()
    query="Default"
    with sr.Microphone() as source:
        print('Listening....')
        #r.pause_threshold=1
        #r.energy_threshold=300
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)
    try:
        print('Recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print("User said: ",query)
    except Exception as e:
        print('Say that again....')
        print(e)
    return query

    


if __name__=="__main__":
    speak("Hello there!. I am your virtual assistant ")
wishme()

while True:
    query=takecommand().lower()
    if 'wikipedia' in query:
        speak('Searching wikipedia....')
        query=query.replace('wikipedia','')
        result=wikipedia.summary(query,sentences=2)
        speak('According to wikipedia....')
        print(result)
        speak(result)
    elif 'open youtube' in query:
        speak('Searching for Youtube and opening it')
        webbrowser.open('youtube.com')
    elif 'search video' in query:
        url='https://www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            speak('What do you want to search?')
            audio=r.listen(source)
            try:
                get=r.recognize_google(audio)
                print(get)
                webbrowser.get().open_new(url+get)
            except sr.UnknownValueError:
                print("Couldn't search for it")
        
    elif 'open google' in query:
        speak('Opening Google.com')
        webbrowser.open('Google.com')
    
    elif 'search google' in query:
        url='https://www.google.com/search?q='
        with sr.Microphone() as source:
            speak('What do you want to search?')
            audio=r.listen(source)
            try:
                get=r.recognize_google(audio)
                print(get)
                webbrowser.get().open_new(url+get)
            except sr.UnknownValueError:
                print("Couldn't search for it")

    elif 'play music' in query:
        music_dir="C:\\Users\\Lenovo\\Music"
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'open epic games' in query:
            file_dir="D:\Games_Data\Epic Games\Launcher\Portal\Binaries\Win32"
            file=os.listdir(file_dir)
            speak('Opening Epic Games')
            os.startfile(os.path.join(file_dir,file[42]))

    elif 'bye' in query:
        speak('Bye sir!')
        break
    
