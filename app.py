import streamlit as st
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from PIL import Image
from patient_voice import record_audio, convert_spech_to_text
from doctor import doc
from doctor_voice import tts_with_gtts

st.set_page_config(page_title="Image + Voice Recorder App")
st.title("AI Doctor")

fs = 44100  # Sample rate

# Upload Image Section
st.header("Upload your medical condition:")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
image_path='sample.png'
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    image.save(image_path)


# Buttons
st.header("Tell me your problem in voice:")


if st.button("Start Recording 🎙️"):
    file_path = 'output.wav'
    record_audio(file_path=file_path, timeout=5)
    query = convert_spech_to_text(file_path=file_path)
    doc_response = doc(image_path=image_path, patient_statement=query)
    tts_with_gtts(doc_response, "doctor_voice.mp3")

