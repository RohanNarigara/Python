from email.mime import audio
import speech_recognition as sr
import webbrowser
import pyttsx3


r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)
    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    #Listen for word "Jarvis" to wake up
    #Obtain audio from the microphone
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #Listen for the Command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    
        except Exception as e:
            print("Error; {0}".format(e))