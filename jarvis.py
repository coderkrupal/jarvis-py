import pyttsx3
import speech_recognition as sr
import pyjokes
import datetime
import webbrowser
import requests
from geopy.geocoders import Nominatim


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
            return data
        except sr.UnknownValueError:
            print("not listening")


def speechspeake(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 140)
    engine.say(x)
    engine.runAndWait()


if __name__ == "__main__":

    print("1.jarvis basic")
    print("2.wheather update using jarvis")
    jarvis_input = int(input("enter comman >"))

    if jarvis_input == 1:
        if speechtext().lower() == "jarvis":
            speechspeake("welcome sir how can i help you")
            data1 = speechtext()
            if "your name" in data1:
                name = "my name is jarvis"
                speechspeake(name)
            elif "old are you" in data1:
                old = "My history of artificial intelligence (AI) began in antiquity, with myths, stories, and rumors of artificial beings endowed with intelligence or consciousness by master craftsmen"
                speechspeake(old)
            elif "time" in data1:
                current_time = datetime.datetime.now().strftime("%I%M%p")
                speechspeake(current_time)
            elif "YouTube" in data1:
                webbrowser.open_new("https://www.youtube.com/")

            elif "chat GPT" in data1:
                print(f"Received input: {data1}")
                webbrowser.open_new("https://chatgpt.com/")

            elif "ghibli art" in data1:
                webbrowser.open_new("https://ghibliai.io/")

            elif "jokes" in data1:
                joke = pyjokes.get_joke()
                speechspeake(joke)
            elif "deactivate" in data1:
                speechspeake("deacticate")
    elif jarvis_input == 2:
        print("weather update...")
        geolocator = Nominatim(user_agent="weather_app")
        CITY = input("enter a city name")
        location = geolocator.geocode("{CITY}, India")
        if location:
            lat = location.latitude
            lon = location.longitude
        else:
            print("locatino not found")
        API_KEY = "f8136e2bab5b48d17abf806cbba601e9"
        URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(URL)
        data = response.json()
        # print(data)
        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            speakdata = f"Current temperature in {CITY}: {temp}°C"
            print("speaking......")
            speechspeake(speakdata)
        else:
            speechspeake("Failed to get weather data")

    else:
        print("not recognize")
