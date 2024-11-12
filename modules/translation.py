import speech_recognition as sr
from googletrans import Translator
from .speak import speak

def hindi_to_english():
    recognizer = sr.Recognizer()
    translator = Translator()
    with sr.Microphone() as source:
        speak("मैं सुन रही हूं सर...")
        audio = recognizer.listen(source)

    try:
        speak("पहचान हो रही है...")
        text = recognizer.recognize_google(audio, language="hi-IN")
    except Exception:
        speak("कृपया इसे फिर से कहें, आपने जो कहा वह मुझे समझ नहीं आया ")
        return "none", "none"

    translation = translator.translate(text, src="hi", dest="en").text
    back_translation = translator.translate(translation, src="en", dest="hi").text
    return translation, back_translation
