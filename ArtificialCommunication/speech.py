
'''import os

if __name__=='__main__':
    print("welcome to RoboSpeaker 1.1.Created by Harry")
    x=input("Enter what you want me to speak: ")
    command= f"say {x}"
    os.system(command)
import os

if __name__ == '__main__':
    print("Welcome to ArtificialCommunication 1.1. Created by LORRISHA")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            break
        command = f'/usr/bin/say {x}'  # Specify full path to say command
        os.system(command)
'''
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

print("Welcome to ArtificialCommunication 1.1. Created by LORRISHA")
while True:
    x = input("Enter what you want me to speak (q to quit): ")
    if x == "q":
        break

    # Speak the input text using the text-to-speech engine
    engine.say(x)
    engine.runAndWait()

# Clean up the text-to-speech engine
engine.stop()
