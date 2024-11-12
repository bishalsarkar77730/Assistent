import speech_recognition as sr
from modules.speak import speak
from modules.wish import wishme
from modules.translation import hindi_to_english
from modules.note_taker import create_note_taker
from modules.search import perform_search

wishme()

trigger_words = [
    "काव्या",
    "कव्या",
    "काव्य",
    "सुनो",
    "काव्या सुनो",
    "क्या सुनो",
    "काव्य हेलो",
    "काव्य सुनो",
]
note_taking_trigger = "काव्या नोट्स लो"

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
            if translation != "none":
                speak(translation)
                speak(back_translation)

        elif note_taking_trigger in recognized_text:
            create_note_taker()
        else:
            perform_search(recognized_text)

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        speak("आपने जो कहा वह मुझे समझ नहीं आया !")
