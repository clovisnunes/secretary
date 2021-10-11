import os
import schedule
import time

from random import randint

from playsound import playsound
from gtts import gTTS

def adicionar_tarefa(new_task):
    global tasks

    carregar_arquivo_tarefas()
    tasks.append(new_task)
    salvar_arquivo_tarefas()

def ler_tarefas():
    global tasks
    global finish
    taskstr = ''

    carregar_arquivo_tarefas()

    print('Tarefas a fazer: (' + str(len(tasks)) + ')')
    for task in tasks:
        print(task)
        taskstr = taskstr + task + ', '

    intro = 'Você tem ' + str(len(tasks)) + ' tarefas a fazer.'
    total_phrase = intro + ' ' + taskstr + '. ' + finish[randint(0, len(finish) - 1)]



    full_speech = gTTS(text=total_phrase, lang='pt', tld='com.br', slow=False)
    full_speech.save("fullspeech.mp3")

    playsound('fullspeech.mp3')

def carregar_arquivo_tarefas(): # esperado: uma tarefa por linha / parametro nome arquivo e arquivo padrão
    global tasks
    taskfile = open(os.getcwd() + "\\tasks.txt", "r")
    tasks = taskfile.read().strip().split("\n")
    taskfile.close()

def salvar_arquivo_tarefas():
    global tasks
    taskfile = open(".\\tasks.txt", "w")
    for task in tasks:
        taskfile.write(task + "\n")
    taskfile.close()
    
    

#def informar_clima():
    #...

tasks = []
finish = ['Anda logo porra.', 'Ta esperando o que meu anjo?'] # aleatorios

# exibir menu inicial
ler_tarefas()
print('\nSelecione uma opcao:')
print('1 - Ler tarefas')
print('2 - Adicionar tarefa')
print('3 - Excluir tarefa')

# agendar com schedule a cada hora(s) e iniciar com o sistema
#schedule.every(2).hour.do(ler_tarefas)

""" while True:
    schedule.run_pending()
    time.sleep(1) """