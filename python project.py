import speech_recognition as sr
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import pyautogui
import webbrowser

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")

    # Option 1: Use macOS built-in afplay
    os.system("afplay response.mp3")

    # Option 2: Use pydub for cross-platform support
    # sound = AudioSegment.from_mp3("response.mp3")
    # play(sound)

tasks = []
listeningToTask = False

def main():
    global tasks
    global listeningToTask

    while True:
        command = listen_for_command()

        triggerKeyword = "bologna"
        
        if command and triggerKeyword in command:
            if listeningToTask:
                tasks.append(command)
                listeningToTask = False
                respond(f"Adding {command} to your task list. You have {len(tasks)} tasks currently in your list.")
            elif "add a task" in command:
                listeningToTask = True
                respond("Sure, what is the task?")
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "take a screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("I took a screenshot for you.")
            elif "open chrome" in command:
                respond("Opening Chrome.")
                webbrowser.open("http://www.youtube.com/@JakeEh")
            elif "exit" in command:
                respond("Goodbye!")
                break
            else:
                respond("Sorry, I'm not sure how to handle that command.")

if __name__ == "__main__":
    respond("This has been building a virtual assistant with Python")