from Speech_to_text import hindi_to_english
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Master िशाल")

    elif 12 <= hour < 18:
        speak("Good Afternoon, Master िशाल")

    else:
        speak("Good Evening, Master िशाल")

    speak("काव्या ऑनलाइन है. मैं आपकी कैसे मदद कर शक्ति हूं")


# wishme()

# trigger_words = ["काव्या", "कव्या", "काव्य", "सुनो", "काव्या सुनो", "क्या सुनो"]
while True:
    translation, back_translation = hindi_to_english()
    speak(translation)
    speak(back_translation)