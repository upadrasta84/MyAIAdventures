#pip install gtts

from gtts import gTTS
import os
import sys

#pass all the text you want as tts as arguments to the program. ex: python textToSpeech.py how are you?
mytext = ""
for i in range(1, len(sys.argv)):
    mytext += sys.argv[i] + " "
       
 
myobj = gTTS(text=mytext, lang='en', slow=False)
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("start welcome.mp3")
