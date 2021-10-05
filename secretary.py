import os
import schedule
import time

from playsound import playsound
from gtts import gTTS

# agendar com schedule a cada hora(s) e iniciar com o sitema

def adicionar_tarefa(tarefa):
    global tasks
    tasks = tasks + ', ' + tarefa

def ler_tarefas():
    global tasks
    global tasknum
    intro = 'Você tem ' + str(tasknum) + ' tarefas a fazer.'
    finish = 'Anda logo porra.' # frases ofensivas aleatórias (lista)
    total_phrase = intro + ' ' + tasks + ' ' + finish

    full_speech = gTTS(text=total_phrase, lang='pt', tld='com.br', slow=False)
    full_speech.save("fullspeech.mp3")

    playsound('fullspeech.mp3')

# exibir menu inicial

#schedule.every(2).hour.do(ler_tarefas)

tasks = 'Finalizar campos do cadastro, Refazer requisição POST, Remodelar banco de dados e backend.' # transformar em array, salvar e ler de arquivo
tasknum = 3
intro = 'Olá Clóvis, você tem ' + str(tasknum) + ' tarefas a fazer.'
finish = 'Anda logo porra.'
total_phrase = intro + ' ' + tasks + ' ' + finish

full_speech = gTTS(text=total_phrase, lang='pt', tld='com.br', slow=False)
full_speech.save("fullspeech.mp3")

playsound('fullspeech.mp3')

""" while True:
    schedule.run_pending()
    time.sleep(1) """