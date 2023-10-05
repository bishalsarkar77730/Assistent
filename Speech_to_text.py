import pyttsx3
import speech_recognition as sr
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def hindi_to_english():
    r = sr.Recognizer()
    translator = Translator()
    with sr.Microphone() as source:
        speak("मैं सुन रही हूं सर...")
        audio = r.listen(source)

    try:
        speak("पहचान हो रही है...")
        text = r.recognize_google(audio, language='hi-IN')
    except Exception as e:
        speak("कृपया इसे फिर से कहें, आपने जो कहा वह मुझे समझ नहीं आया ")
        return "none"
    translation = translator.translate(text, src='hi', dest='en').text
    back_translation = translator.translate(
        translation, src='en', dest='hi').text

    return translation, back_translation
