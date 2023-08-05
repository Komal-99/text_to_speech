import streamlit as st
from gtts import gTTS
from io import BytesIO

def text_to_speech_app():
    # Get user input text through a text area
    text_to_speech = st.text_area("Enter the text you want to convert to speech:")

    # Convert the text to speech when the user clicks the "Generate Audio" button
    if st.button("Generate Audio"):
        # Check if the input text is not empty
        if text_to_speech.strip() != "":
            audio_data = get_audio_data(text_to_speech)
            st.audio(audio_data, format='audio/mpeg')

def get_audio_data(text_to_speech):
    # Generate audio using gTTS
    tts = gTTS(text=text_to_speech, lang='en')
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)
    return audio_stream

if __name__ == '__main__':
    text_to_speech_app()
