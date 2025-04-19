import sounddevice as sd
import soundfile as sf
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

file_path = 'output.wav'

def record_audio(file_path, timeout=5, phrase_time_limit=None):
    fs = 44100  # Sample rate
    seconds = timeout  # Duration of recording

    print("Recording...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording finished.")

    sf.write(file_path, myrecording, fs)


def convert_spech_to_text(file_path):
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    client = Groq(api_key=GROQ_API_KEY)
    stt_model = 'whisper-large-v3-turbo'
    audio_file = open(file_path,'rb')
    transcription = client.audio.transcriptions.create(
        model = stt_model,
        file=audio_file,
        language='bn'
    )
    print(transcription)
    return transcription.text


record_audio(file_path)
convert_spech_to_text(file_path)

