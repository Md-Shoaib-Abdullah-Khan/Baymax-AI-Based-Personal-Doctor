import streamlit as st
import numpy as np
import scipy.io.wavfile as wav
from PIL import Image
from patient_voice import record_audio, convert_spech_to_text
from doctor import doc
from doctor_voice import tts_with_gtts
import pygame
import io
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


st.header("Tell me your problem:")


if st.button("Start Recording 🎙️"):
    
    record_audio('patient_voice.wav', timeout=5)
    query = convert_spech_to_text('patient_voice.wav')
    doc_response = doc(image_path=image_path, patient_statement=query)
    tts_with_gtts(doc_response)
    

