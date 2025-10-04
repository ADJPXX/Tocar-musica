# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


def verificar_pacotes(NOME_PACOTE):
	import importlib
	import os
	PACOTE = importlib.util.find_spec(NOME_PACOTE)
	if PACOTE is not None:
		print("Pacote já está instalado.")

	else:
		os.system(f"pip install {NOME_PACOTE}")


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


def escolhermusica():
	from pygame import mixer
	import os

	verificar_pacotes("pygame")
	clear()

	path = (os.path.dirname(os.path.abspath(__file__)) + "\Músicas\\")

	musicas = []
	for a in os.listdir(path):
		musicas.append(a)

	mixer.init()
	while True:
		cont = 0
		print("-"*30)
		print("LISTA DE MÚSICAS!".center(30))
		print("-"*30)
		for m in musicas:
			cont += 1
			print(f'[ {cont} ] {m}')
		print("-"*30)
		print("\nDigite 0 para sair do programa\n")
		op = lerint('Qual música você gostaria de ouvir? ')

		if op == 0:
			clear()
			print("Obrigado por usar o programa!")
			break

		if op > len(musicas) or op < 0:
			clear()
			print("Digite uma opção válida\n")

		else:
			mixer.music.load(f"{path}{musicas[op - 1]}")
			clear()
			tocandomusica()
			break


def menu(volumeatual):
	print(f'''Pressione "P" para parar a música.
Pressione "E" para continuar a música.
Pressione "R" para reiniciar a música.
Pressione "W" para aumentar o volume.
Pressione "S" para diminuir o volume.
Pressione "X" para sair do programa.
Pressione "V" para trocar a música.\n\nVolume: {volumeatual}''')
	op = lerstring("Sua escolha: ").strip().lower()

	return op


def tocandomusica():
	from pygame import mixer

	mixer.music.play()
	volumepadrao = 0.2
	volumeatual = 0.2
	mixer.music.set_volume(volumepadrao)

	while True:
		global aumentarvolume,baixarvolume

		aumentarvolume = 0
		baixarvolume = 0
		op = menu(volumeatual)

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
			clear()
			volumeatual = mixer.music.get_volume()
			aumentarvolume = volumeatual + 0.02
			mixer.music.set_volume(aumentarvolume)
			print(f"Volume aumentado!\nVolume: {volumeatual}")
		elif op == 's':
			clear()
			volumeatual = mixer.music.get_volume()
			baixarvolume = volumeatual - 0.02
			mixer.music.set_volume(baixarvolume)
			print(f"Volume baixado!\nVolume: {volumeatual}")
		elif op == 'v':
			mixer.music.stop()
			escolhermusica()


def main():
	escolhermusica()


if __name__ == '__main__':
	main()