# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
from time import sleep


def verificar_pacotes(nome_pacote):
	try:
		import os
		import sys
		import importlib

		PACOTE = importlib.util.find_spec(nome_pacote)

		if PACOTE is not None:
			os.system("cls")
			print(f'[✓] O pacote "{nome_pacote}" já está instalado.\nVou verificar as atualizações e se necessario atualizar.')
			os.system(f'pip install --upgrade {nome_pacote}')

		else:
			try:
				os.system("cls")
				print(f"[+]Instalando o pacote {nome_pacote}...")
				os.system(f"pip install {nome_pacote}")

			except Exception as e:
				os.system("cls")
				print("Ocorreu um erro ao instalar o pacote: ", e)

	except Exception as e:
		print(e)


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
	import ffmpeg
	import os

	musicas = []

	clear()

	path = (os.path.dirname(os.path.abspath(__file__)) + "\Musicas\\")

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
			try:
				mixer.music.load(f"{path}{musicas[op - 1]}")
				clear()
				tocandomusica()
				break

			except:
				print("SEU ARQUIVO NÃO É COMPATÍVEL, ESTOU CONVERTENDO ELE PARA VOCÊ PODER OUVIR A MÚSICA")
				print("CONVERTENDO ARQUIVO...")
				try:
					input_file = f"{path}{musicas[op - 1]}"
					output_file = f"{path}{musicas[op - 1]}.mp3"
					ffmpeg.input(input_file).output(output_file, **{'c:a': 'libmp3lame', 'b:a': '320k'}).run(overwrite_output=True)

					sleep(1.5)

					indice = f'{musicas[op - 1]}'
					nome_antigo = f"{path}{musicas[op - 1]}.mp3"
					novo_nome = f"{path}{indice.replace('.mp3', '_convertido.mp3')}"

					os.rename(nome_antigo, novo_nome)

					mixer.music.load(f"{novo_nome}")
					clear()
					tocandomusica()

					arquivo_excluir = f"{path}{novo_nome}"
					os.remove(f"{arquivo_excluir}")
					break

				except Exception as e:
					print(f"ERRO AO CONVERTER SEU ARQUIVO: {e}")
					sleep(3)


def menu(volumeatual):
	print(f'''Pressione "P" para parar a música.
Pressione "E" para continuar a música.
Pressione "R" para reiniciar a música.
Pressione "W" para aumentar o volume.
Pressione "S" para diminuir o volume.
Pressione "X" para sair do programa.
Pressione "V" para trocar a música.\n\nVolume: {volumeatual}\n''')
	op = lerstring("Sua escolha: ").strip().lower()

	return op


def tocandomusica():
	from pygame import mixer

	mixer.music.play()
	volumepadrao = 0.2
	volumeatual = 0.2
	mixer.music.set_volume(volumepadrao)

	while True:
		aumentarvolume = 0
		baixarvolume = 0
		op = menu(volumeatual)

		if op == 'x':
			mixer.music.stop()
			clear()
			print('Obrigado por usar o programa!')
			break
		elif op == 'p':
			clear()
			mixer.music.pause()
			print("Musica parada!")
		elif op == 'e':
			clear()
			mixer.music.unpause()
			print("Música continuada!")
		elif op == 'r':
			clear()
			mixer.music.rewind()
			print("Música reiniciada!")
		elif op == 'w':
			clear()
			volumeatual = mixer.music.get_volume()
			aumentarvolume = volumeatual + 0.02
			mixer.music.set_volume(aumentarvolume)
			print(f"Volume aumentado!\n")
		elif op == 's':
			clear()
			volumeatual = mixer.music.get_volume()
			baixarvolume = volumeatual - 0.02
			mixer.music.set_volume(baixarvolume)
			print(f"Volume baixado!\n")
		elif op == 'v':
			clear()
			mixer.music.stop()
			escolhermusica()
			break


def main():
	verificar_pacotes("pygame")
	verificar_pacotes("ffmpeg-python")

	escolhermusica()


if __name__ == '__main__':
	main()