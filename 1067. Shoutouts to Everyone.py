import pyttsx3


def text_to_speech(everyone):
    for someone in everyone:
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # Convert the text to speech
        engine.say(f"Shoutout to {someone}")
        engine.runAndWait()


# Example usage
everyone = ["Subhranil1", "Subhranil2", "Subhranil3"]
text_to_speech(everyone)
