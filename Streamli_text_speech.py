import streamlit as st
import pyttsx3

def text_to_speech_app():
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties for the TTS engine (optional)
    engine.setProperty('volume', 0.9)
    engine.setProperty('rate', 150)  # Adjust the speech rate as needed

    # Get user input text through a text area
    text_to_speech = st.text_area("Enter the text you want to convert to speech:")

    # Convert the text to speech when the user clicks the "Generate Audio" button
    if st.button("Generate Audio"):
        # Check if the input text is not empty
        if text_to_speech.strip() != "":
            engine.say(text_to_speech)
            engine.runAndWait()
            st.audio(get_audio_file(text_to_speech), format='audio/wav')

def get_audio_file(text_to_speech):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # You can customize the filename and path for saving the audio file
    filename = 'text_to_speech_output.wav'

    # Save the TTS audio file
    engine.save_to_file(text_to_speech, filename)
    engine.runAndWait()
    return filename

if __name__ == '__main__':
    text_to_speech_app()
