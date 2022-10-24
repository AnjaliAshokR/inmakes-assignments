import os
from gtts import gTTS
text=open('demo.txt', 'r').read()
language="Hi"
out_text=gTTS(text=text,lang='en', slow=False)
out_text.save('file_out.mp3')
os.system("start file_out.mp3")