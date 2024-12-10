import pyttsx3
import speech_recognition 
ear = speech_recognition.Recognizer()

def speak(text:str):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


# DEMO

def listen()->str:
    with speech_recognition.Microphone(0) as mics:
        print("successfully init microphone")
        user_input = ear.listen(mic,timeout=2,phrase_time_limit=2)
        print("got sound")
        text = ear.recognize_google(user_input)
        text = text.lower()
        speak(text)
        return text
test = listen()
exit()