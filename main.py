import yt_dlp
import os

def descargar_musica(url, carpeta="descargas"):
    try:
        # Crear carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        
        # Opciones de descarga (sin conversión a MP3)
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
        }
        
        print("Descargando audio de YouTube...")
        
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        
        print("¡Descarga completada!")
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    url = input("Ingrese el enlace del video: ")
    descargar_musica(url)
