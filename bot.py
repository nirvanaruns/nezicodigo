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
    # Inglés
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
