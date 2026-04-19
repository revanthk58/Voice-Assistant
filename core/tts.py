
import pyttsx3

def speak(text):
    engine = pyttsx3.init()   # 👈 create fresh instance each time
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()
    engine.stop() 

