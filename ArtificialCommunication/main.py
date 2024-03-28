import speech_recognition as sr

# Create a recognizer object using PocketSphinx
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

try:
    # Recognize speech using PocketSphinx
    text = recognizer.recognize_sphinx(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError as e:
    print(f"Recognition request failed; {e}")


import os

if __name__ == '__main__':
    print("Welcome to ArtificialCommunication 1.1. Created by LORRISHA")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            break
    command = f"say {x}"
    os.system(command)
