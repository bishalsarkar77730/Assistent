from googlesearch import search
from .speak import speak


def perform_search(query):
    speak("मैं आपके प्रश्न का उत्तर खोज रही हूं...")
    results = []
    try:
        for result in search(query, num_results=3):
            results.append(result)
        if results:
            speak("यह रहे कुछ परिणाम:")
            for i, result in enumerate(results, start=1):
                speak(f"परिणाम {i}")
                print(result)
                speak(result)
    except Exception:
        speak("मुझे अभी इंटरनेट से जोड़ने में समस्या हो रही है। कृपया बाद में प्रयास करें।")
