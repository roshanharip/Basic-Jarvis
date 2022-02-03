# pyttsx3 is Python Text To Speech Library
import pyttsx3
# speechRecognition is Recognise Speak 
import speech_recognition as sr
#  importing wikipedia
import wikipedia
import webbrowser
import os
import datetime
# installing driver
engine = pyttsx3.init("sapi5")
# getting voices of modules
voices = engine.getProperty("voices")
# setting voice
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!!")
    elif hour <= 12 and hour< 18:
        speak("Good Afternoon!!!")
    else:
        speak("Good Evening !!!")
    speak("Roshan, How can I help you? ") 
def takeCommand():
    '''This Function takes Command and output the string as voice'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Listening........
        # Checking ___ Microphone
        print("Listening")
        # Pausing Time initial Voice and Before final voice 
        # Threshold
        r.pause_threshold = 1
        # Source is the Audio Which we speak
        # listen func listening source 
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        # recognizing audio through google engine thier are too many engine you will try another also
        query = r.recognize_google(audio,language='en-in')
        query = ["wikipedia","shahrukh khan"]
        # print what user said
        print(f"User said : {query} ")
    except Exception as e:
        print(e)
        print("Say again please....")
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query :
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences= 2 )
            speak('According to Wikipedia')
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'open amazon' in query:
            webbrowser.open('amazon.in')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(strTime)
        elif 'open code' in query:
            codepath = "C:\\Users\\91944\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'exit' in query:
            exit()