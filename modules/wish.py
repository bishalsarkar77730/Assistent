from datetime import datetime
from .speak import speak

def wishme():
    hour = int(datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, बिशाल जी")
    elif 12 <= hour < 18:
        speak("Good Afternoon, बिशाल जी")
    else:
        speak("Good Evening, बिशाल जी")
    speak("काव्या ऑनलाइन है! मैं आपकी कैसे मदद कर शक्ति हूं")
