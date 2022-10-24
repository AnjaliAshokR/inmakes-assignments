import os
from gtts import gTTS
input_text="Hi!  How are you?"
out_text=gTTS(text=input_text,lang='en', slow=False)
out_text.save('output_text.mp3')
os.system("start output_text.mp3")