import os

from playsound import playsound
from gtts import gTTS


tasks = 'Finish form fields, Compose post request from the form, Remodel database and backend.'
tasknum = 3
intro = 'You have ' + str(tasknum) + ' tasks.'
finish = 'Do your fucking job.'

total_phrase = intro + ' ' + tasks + ' ' + finish

full_speech = gTTS(text=total_phrase, lang='en', slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
full_speech.save("fullspeech.mp3")

# Playing the converted file
playsound('fullspeech.mp3')