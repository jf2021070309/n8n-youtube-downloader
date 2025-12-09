FROM n8nio/n8n:latest

# Cambiar a usuario root para instalar paquetes
USER root

# Instalar Python, pip, ffmpeg y yt-dlp
RUN apk add --no-cache \
    python3 \
    py3-pip \
    ffmpeg && \
    pip3 install --no-cache-dir --break-system-packages --upgrade yt-dlp

# Volver al usuario node
USER node

# Exponer puerto
EXPOSE 5678

# Usar el entrypoint original de n8n
ENTRYPOINT ["tini", "--", "/docker-entrypoint.sh"]
