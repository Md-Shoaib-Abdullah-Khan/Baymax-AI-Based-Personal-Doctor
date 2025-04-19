import os
from gtts import gTTS
from playsound import playsound
import subprocess
import platform

def tts_with_gtts(input_text, output_filepath="doctor_voice.mp3"):
    language = 'bn'

    speech = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )

    speech.save(output_filepath) 

    playsound(output_filepath)

        
text_to_speak = "প্রতিটি বাঙালির জীবনে একটা বিশেষ জায়গা জুড়ে আছে। ছোটবেলায় স্কুল থেকে ফিরে বা ছুটির দিনে বাংলা গল্পের বই নিয়ে সময় কাটায়নি এমন বাঙালি নেই বললেই চলে। প্রচুর মানুষ আছেন যারা বড় হওয়ার পরেও, হাজারো ব্যস্ততার মধ্যেও রোজ গল্প পড়তে ভীষণ ভালোবাসেন। Bangla golper সাথে বাঙালিদের অনেক স্মৃতি জড়িয়ে আছে। বাংলা গল্প একদিকে যেমন সারাদিনের ধকল, চিন্তা এক নিমেষে দূর করে দিতে পারে"
#tts_with_gtts(text_to_speak, "doctor_voice.mp3")


from langchain_community.tools import ElevenLabsText2SpeechTool
from dotenv import load_dotenv
load_dotenv()

text_to_speak = "Hello world! I am the real slim shady"

def tts_with_elevenlabs(text):
    tts = ElevenLabsText2SpeechTool()
    speech_file = tts.run(text)
    tts.play(speech_file)

#tts_with_elevenlabs(text_to_speak)



