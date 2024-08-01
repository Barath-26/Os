import keyboard
import pygetwindow as gw
import joblib
import re

# Load the trained model
model = joblib.load('distraction_classifier.pkl')

common_words = {"the", "also", "and", "that", "if", "is", "it", "in", "on", "at", "to", "with", "for","make","give","me","more","data","set"}
typed_characters = []

def minimize_current_window():
    try:
        window = gw.getActiveWindow()
        if window:
            window.minimize()
    except Exception as e:
        print(f"Error minimizing window: {e}")

def check_input(event):
    global typed_characters

    if event.name == 'space':
        input_text = ''.join(typed_characters).strip()
        typed_characters = []

        # Remove common words from the input
        words = re.findall(r'\b\w+\b', input_text.lower())
        filtered_words = [word for word in words if word not in common_words]

        if not filtered_words:
            return

        # Use the trained model to predict if the input text is distracting
        prediction = model.predict([input_text])[0]

        if prediction == 0:
            print(f"Educational input detected: {input_text}")
        else:
            print(f"Distracting input detected: {input_text}. Minimizing current window.")
            minimize_current_window()
    elif event.name == 'backspace':
        if typed_characters:
            typed_characters.pop()
    else:
        typed_characters.append(event.name)

keyboard.on_press(check_input)

print("Keyboard monitoring started. Press ESC to stop.")
keyboard.wait('esc')
