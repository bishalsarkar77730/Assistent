from Speech_to_text import hindi_to_english
import speech_recognition as sr
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
        speak("Good Morning, बिशाल जी")

    elif 12 <= hour < 18:
        speak("Good Afternoon, बिशाल जी")

    else:
        speak("Good Evening, बिशाल जी")

    speak("काव्या ऑनलाइन है! मैं आपकी कैसे मदद कर शक्ति हूं")


# wishme()

trigger_words = ["काव्या", "कव्या", "काव्य",
                 "सुनो", "काव्या सुनो", "क्या सुनो", "काव्य हेलो", "काव्य सुनो"]
# while True:
#     translation, back_translation = hindi_to_english()
#     speak(translation)
#     speak(back_translation)

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        speak("मैं सुन रही हूं सर...")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio, language="hi-IN")
        print("You said: " + recognized_text)

        if any(word in recognized_text for word in trigger_words):
            translation, back_translation = hindi_to_english()
            speak(translation)
            speak(back_translation)

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        speak("आपने जो कहा वह मुझे समझ नहीं आया !")
