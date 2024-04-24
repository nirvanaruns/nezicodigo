import time
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent
import pyttsx3
from datetime import datetime
import os
import pygame

# Define una variable global para almacenar el último momento en que se usó el comando "_error"
last_error_time = 0
last_pedro_time = 0

# Inicializar Pygame
pygame.mixer.init()

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Variable global para controlar el estado de text-to-speech
tts_enabled = False  # Puedes ajustar el valor inicial según tus necesidades

# Lista de palabras a ignorar en el text-to-speech
excluded_words = {
    "arriba": "w",
    "abajo": "s",
    "izquierda": "a",
    "derecha": "d",
    "botona": "q",
    "botonb": "e",
    "botonl": "o",
    "botonr": "p",
    "carriba": "y",
    "cabajo": "h",
    "cizquierda": "g",
    "cderecha": "j",
    "start": "m",
    "select": "l",
    # Inglés
    "up": "w",
    "down": "s",
    "left": "a",
    "right": "d",
    "buttona": "q",
    "buttonb": "e",
    "buttonl": "o",
    "buttonr": "p",
    "cup": "y",
    "cdown": "h",
    "cleft": "g",
    "cright": "j",
    "start": "m",
    "select": "l"
}

def ignore_word(word):
    return word.startswith("_") and len(word) > 1 or word.lower() in excluded_words

def get_allowed_user():
    try:
        with open("tiktokchannel.txt", "r") as file:
            return file.read().strip().lower()
    except FileNotFoundError:
        print("El archivo tiktokchannel.txt no se ha encontrado.")
        return None

def play_wav(file_name):
    try:
        print(f"Reproduciendo {file_name}")
        pygame.mixer.Sound(file_name).play()
        pygame.time.delay(1000)  # Esperar 1 segundo antes de continuar
    except pygame.error as e:
        print(f"Error al reproducir el archivo {file_name}: {e}")

if __name__ == "__main__":
    allowed_user = get_allowed_user()

    if allowed_user:
        tiktok_username = "@" + allowed_user
        tiktok_client = TikTokLiveClient(unique_id=tiktok_username)

        # Corregir el manejo del evento de comentario
        @tiktok_client.on(CommentEvent)  # Utilizar el decorador adecuado
        async def on_ttcomment(comment_data):
            global tts_enabled, last_error_time, last_pedro_time

            username = comment_data.user.nickname
            comment_text = comment_data.comment

            # Verificar si comment_text es None antes de intentar llamar a lower()
            if comment_text is not None:
                comment_text = comment_text.lower()
            else:
                # Manejar el caso en que comment_text sea None
                pass

            username = username.lower()

            current_time = time.time()
            current_time_pedro = time.time()
            formatted_comment = f"[{datetime.now().strftime('%H:%M')}] {username}: {comment_text}"
            print(formatted_comment)
            
            # Verificar si ha pasado al menos 10 minutos desde el último uso del comando "_error"
            if "_error" in comment_text and current_time - last_error_time >= 600:  # 600 segundos = 10 minutos
                last_error_time = current_time
                # Lógica del comando "_error"
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/error.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/error.txt")
                except FileNotFoundError:
                    print("El archivo error.txt no existe.")
            elif "_error" in comment_text:
                print("El comando _error solo puede ser usado una vez cada 10 minutos.")
                
            # Verificar si ha pasado al menos 2 minutos 30 segundos desde el último uso del comando "_pedro"
            if "_pedro" in comment_text and current_time_pedro - last_pedro_time >= 150:  # 300 segundos = 2 minutos 30 segundos
                last_pedro_time = current_time_pedro
                # Lógica del comando "_pedro"
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/pedro.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos 30 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/pedro.txt")
                except FileNotFoundError:
                    print("El archivo pedro.txt no existe.")
            elif "_pedro" in comment_text:
                print("El comando _pedro solo puede ser usado una vez cada 5 minutos.")

            # Crear o eliminar el archivo jugar.txt si el comentario contiene "_jugar"
            if "_jugar" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/jugar.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/jugar.txt")
                except FileNotFoundError:
                    print("El archivo jugar.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_pregunta"
            if "_pregunta" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/pregunta.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/pregunta.txt")
                except FileNotFoundError:
                    print("El archivo pregunta.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_salir"
            if "_salir" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/salir.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/salir.txt")
                except FileNotFoundError:
                    print("El archivo pregunta.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_puntaje"
            if "_puntaje" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/puntaje.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/puntaje.txt")
                except FileNotFoundError:
                    print("El archivo puntaje.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_salirsi"
            if "_salirsi" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/salirsi.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/salirsi.txt")
                except FileNotFoundError:
                    print("El archivo salirsi.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_salirno"
            if "_salirno" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/salirno.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/salirno.txt")
                except FileNotFoundError:
                    print("El archivo salirno.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_opciona"
            if "_opciona" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/opciona.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/opciona.txt")
                except FileNotFoundError:
                    print("El archivo opciona.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_opcionb"
            if "_opcionb" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/opcionb.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/opcionb.txt")
                except FileNotFoundError:
                    print("El archivo opcionb.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_opcionc"
            if "_opcionc" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/opcionc.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/opcionc.txt")
                except FileNotFoundError:
                    print("El archivo opcionc.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_opciond"
            if "_opciond" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/opciond.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/opciond.txt")
                except FileNotFoundError:
                    print("El archivo opciond.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_50"
            if "_50" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/50.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/50.txt")
                except FileNotFoundError:
                    print("El archivo 50.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_otrapregunta"
            if "_otrapregunta" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/otrapregunta.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/otrapregunta.txt")
                except FileNotFoundError:
                    print("El archivo otrapregunta.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_siguiente"
            if "_siguiente" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/siguiente.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/siguiente.txt")
                except FileNotFoundError:
                    print("El archivo siguiente.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_reiniciar"
            if "_reiniciar" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/reiniciar.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/reiniciar.txt")
                except FileNotFoundError:
                    print("El archivo reiniciar.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_desaparece"
            if "_desaparece" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/desaparece.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/desaparece.txt")
                except FileNotFoundError:
                    print("El archivo desaparece.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_penita"
            if "_penita" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/penita.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/penita.txt")
                except FileNotFoundError:
                    print("El archivo penita.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_popin"
            if "_popin" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/popin.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 2 segundos y luego eliminar el archivo
                time.sleep(2)
                try:
                    os.remove("sammicomandos/popin.txt")
                except FileNotFoundError:
                    print("El archivo popin.txt no existe.")

            # Crear o eliminar el archivo a.txt si el comentario contiene "_krool"
            if "_krool" in comment_text:
                if not os.path.exists("sammicomandos"):
                    os.makedirs("sammicomandos")
                with open("sammicomandos/krool.txt", "w") as file:
                    file.write("Archivo creado por el usuario")

                # Esperar 5.5 segundos y luego eliminar el archivo
                time.sleep(5.5)
                try:
                    os.remove("sammicomandos/krool.txt")
                except FileNotFoundError:
                    print("El archivo krool.txt no existe.")

            words = comment_text.split()
            filtered_words = [word for word in words if not ignore_word(word)]

            if tts_enabled:
                # Crear una lista para contener las partes del comentario con los archivos wav
                final_output = []

                for word in words:
                    if ignore_word(word):
                        wav_file = f"Audios/{word}.wav"  # Modificado aquí, manteniendo el guion bajo
                        if os.path.exists(wav_file):
                            play_wav(wav_file)
                    else:
                        final_output.append(word)

                # Unir las partes del comentario y leer el resultado en el texto a voz
                final_comment = " ".join(final_output)

                nick_mapping = get_nick_mapping()
                if username in nick_mapping:
                    username = nick_mapping[username]

                engine.say(f"{username} dijo: {final_comment}")
                engine.runAndWait()

        print("Connected")
        tiktok_client.run()

        while True:
            time.sleep(1)
    else:
        print("No se ha especificado un nombre de usuario en tiktokchannel.txt.")
