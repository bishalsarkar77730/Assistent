import tkinter as tk
from tkinter import scrolledtext
from .speak import speak

def create_note_taker():
    def save_notes():
        notes = text_area.get("1.0", tk.END)
        with open("notes.txt", "w") as file:
            file.write(notes)
        root.destroy()
        speak("आपके नोट्स सुरक्षित कर लिए गए हैं")

    root = tk.Tk()
    root.title("Kavya Notes")
    text_area = scrolledtext.ScrolledText(
        root, wrap=tk.WORD, width=40, height=10, font=("Arial", 12)
    )
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    save_button = tk.Button(root, text="Save Notes", command=save_notes)
    save_button.pack(pady=10)
    root.mainloop()
