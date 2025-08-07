import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyBnny6AbjR52NGDnbN7qVSCBVBbX7Xe9Fg")
model = genai.GenerativeModel("models/gemini-pro")
  # fixed typo (moldel -> model)

# Initialize voice engine
engine = pyttsx3.init()

# Recognizer
r = sr.Recognizer()

print("Spartan Assistant ready.")

while True:
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio)
        print(f"You said: {user_input}")

        # Stop condition
        if "stop" in user_input.lower():
            engine.say("Goodbye, Spartan out!")
            engine.runAndWait()
            break

        # Get AI response and speak it
        ai_response = model.generate_content(user_input).text
        engine.say(ai_response)
        engine.runAndWait()

    except Exception as e:
        print(f"Error: {str(e)}")
        engine.say("Sorry, I didn't catch that.")
        engine.runAndWait()
