# YouTube Downloader n8n - Build v2.0
# Forzar rebuild: 2025-12-09-02:00

FROM n8nio/n8n:latest

# Cambiar a usuario root
USER root

# Actualizar apk e instalar dependencias
RUN apk update && \
    apk add --no-cache \
    python3 \
    py3-pip \
    ffmpeg \
    curl

# Instalar yt-dlp usando el método recomendado (descarga directa)
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && \
    chmod a+rx /usr/local/bin/yt-dlp

# Verificar que yt-dlp esté instalado correctamente
RUN yt-dlp --version && \
    echo "yt-dlp installed successfully at: $(which yt-dlp)"

# Volver al usuario node
USER node

# Exponer puerto
EXPOSE 5678

# Usar el entrypoint original de n8n
ENTRYPOINT ["tini", "--", "/docker-entrypoint.sh"]
