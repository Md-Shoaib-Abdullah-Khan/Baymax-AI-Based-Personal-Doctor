from gtts import gTTS
import pygame
import io
def tts_with_gtts(input_text):
    language = 'en'

    speech = gTTS(text=input_text, lang=language, slow=False)
    mp3_fp = io.BytesIO()
    speech.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    pygame.mixer.init()
    sound = pygame.mixer.Sound(mp3_fp)
    sound.play()
    speech.save('doctor_voice.mp3')



