import pyttsx3
import speech_recognition as sr
import pyjokes
import datetime

def speechtext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("not listening")


def speechspeake(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',200)
    engine.say(x)
    engine.runAndWait()
    
    
    
    
    
speechspeake("hello")