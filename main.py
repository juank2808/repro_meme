import pygame
import os

def repro_audio():
    route = os.getcwd() 
    audio_route = os.path.join(route,'audio','vamos_a_tomar_cafe.mp3')
    print(audio_route)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_route)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
repro_audio()
def main():
    while True:
        print("Elige una Opcion:")
        print("1. Reproducir audio")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            repro_audio()
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()