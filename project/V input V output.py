import speech_recognition as sr
import pyttsx3

Initialize recognizer & TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙 Say something...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
             speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Connection error.")
        return ""

while True:
    command = listen()
    if "stop" in command:
        speak("Goodbye!")
        break
    elif command:
        speak("You said " + command)
