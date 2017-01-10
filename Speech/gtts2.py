from gtts import gTTS
import os

text="main hindi bol nahi sakti"
lang='hi'
tts= gTTS (text, lang)
tts.save('hindi.mp3')
#print os.getcwd() #get current working directory
os.system("mpg321 hindi.mp3") #install mpg321



