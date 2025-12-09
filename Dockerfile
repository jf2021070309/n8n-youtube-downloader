FROM n8nio/n8n:latest

# Cambiar a usuario root para instalar paquetes
USER root

# Instalar Python, pip, ffmpeg y yt-dlp
RUN apk add --no-cache \
    python3 \
    py3-pip \
    ffmpeg

# Instalar yt-dlp
RUN pip3 install --no-cache-dir --upgrade yt-dlp

# Volver al usuario n8n
USER node

# Exponer puerto
EXPOSE 5678

# Comando de inicio
CMD ["n8n"]
