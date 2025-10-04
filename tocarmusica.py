# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
def clear():
    from os import system, name
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def lerstring(msg):
    while True:
        try:
            string = str(input(msg))
        except:
            pass
        else:
            return string


def lerint(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except:
            pass
        else:
            return inteiro


path = "D:\Codigos\Codigos Python\Tocar música\Músicas"


def escolhermusica():
    clear()
    mixer.init()
    while True:
        print("Digite 0 para sair do programa")
        op = lerint('''Qual música você gostaria de ouvir?
1, 2, 3, 4 ou 5? ''')
        if op == 0:
            clear()
            print("Obrigado por usar o programa!")
            break
        if op == 1:
            mixer.music.load(f'{path}\desafio6-1.mp3')
            break
        elif op == 2:
            mixer.music.load(f'{path}\desafio6-2.mp3')
            break
        elif op == 3:
            mixer.music.load(f'{path}\desafio6-3.mp3')
            break
        elif op == 4:
            mixer.music.load(f'{path}\desafio6-4.mp3')
            break
        elif op == 5:
            mixer.music.load(f'{path}\desafio6-5.mp3')
            break
        else:
            continue
    mixer.music.play()


from pygame import mixer

volumeup = volumedown = 0
volumepadrao = 0.2
escolhermusica()
mixer.music.set_volume(volumepadrao)

while True:
    clear()
    print('''Pressione "P" para parar a música.
Pressione "E" para continuar a música.
Pressione "R" para reiniciar a música.
Pressione "W" para aumentar o volume.
Pressione "S" para diminuir o volume.
Pressione "X" para sair do programa.
Pressione "V" para trocar a música.''')
    op = lerstring("Sua escolha: ").strip().lower()

    if op == 'x':
        mixer.music.stop()
        clear()
        print('Obrigado por usar o programa!')
        break
    elif op == 'p':
        mixer.music.pause()
        print("Musica parada!")
    elif op == 'e':
        mixer.music.unpause()
        print("Música continuada!")
    elif op == 'r':
        mixer.music.rewind()
        print("Música reiniciada!")
    elif op == 'w':
        volumeatual = mixer.music.get_volume()
        volumeup = volumeatual + 0.02
        mixer.music.set_volume(volumeup)
    elif op == 's':
        volumeatual = mixer.music.get_volume()
        volumedown = volumeatual - 0.02
        mixer.music.set_volume(volumedown)
    elif op == 'v':
        mixer.music.stop()
        escolhermusica()
