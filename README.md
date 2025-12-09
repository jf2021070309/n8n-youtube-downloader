# 🎬 YouTube Downloader API

API simple para descargar videos de YouTube en MP3 o MP4 usando **pytube**.

## ✅ Características

- 🎵 **Descarga MP3** - Solo audio
- 🎬 **Descarga MP4** - Video completo
- 📊 **Info del video** - Metadata completa
- 🚀 **Sin dependencias externas** - Solo Python puro
- 🌐 **CORS habilitado** - Funciona desde cualquier origen

---

## 🚀 Endpoints

### **1. GET /**
Información de la API

**Response:**
```json
{
  "status": "ok",
  "message": "YouTube Downloader API",
  "endpoints": {...},
  "version": "1.0.0"
}
```

### **2. GET /download**
Descarga un video de YouTube

**Parámetros:**
- `url` (required): URL del video de YouTube
- `format` (optional): `mp3` o `mp4` (default: `mp4`)
- `quality` (optional): `low`, `medium`, `high` (default: `medium`)

**Ejemplo:**
```
GET /download?url=https://youtube.com/watch?v=dQw4w9WgXcQ&format=mp3
```

**Response:**
- Archivo MP3 o MP4 para descargar

### **3. GET /info**
Obtiene información del video

**Parámetros:**
- `url` (required): URL del video de YouTube

**Ejemplo:**
```
GET /info?url=https://youtube.com/watch?v=dQw4w9WgXcQ
```

**Response:**
```json
{
  "title": "Video Title",
  "author": "Channel Name",
  "length": 213,
  "views": 1000000,
  "thumbnail": "https://...",
  "available_formats": {...}
}
```

### **4. GET /health**
Health check

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-12-09T02:40:00"
}
```

---

## 🛠️ Instalación Local

### **Requisitos:**
- Python 3.11+
- pip

### **Pasos:**

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Ejecutar:**
```bash
python app.py
```

3. **Probar:**
```
http://localhost:5000/
```

---

## 🚀 Desplegar en Render.com

### **Paso 1: Push a GitHub**
```bash
git add .
git commit -m "Add YouTube API"
git push
```

### **Paso 2: Crear Web Service en Render**
1. New Web Service
2. Conectar repositorio
3. Render detectará `render.yaml` automáticamente
4. Deploy

### **Paso 3: Probar**
```
https://tu-api.onrender.com/download?url=VIDEO_URL&format=mp3
```

---

## 📊 Uso desde n8n

### **Nodo HTTP Request:**

**URL:**
```
https://tu-api.onrender.com/download
```

**Query Parameters:**
```
url: {{$json.youtubeUrl}}
format: {{$json.formato}}
```

**Response Format:** File

---

## ⚡ Ventajas

- ✅ **Sin yt-dlp** - Solo Python puro
- ✅ **Sin ffmpeg** - No necesita binarios externos
- ✅ **Ligero** - Imagen Docker pequeña
- ✅ **Rápido** - pytube es muy eficiente
- ✅ **Funciona en cualquier lugar** - Render, Railway, Vercel, etc.

---

## 🔧 Tecnologías

- **Flask** - Framework web
- **pytube** - Librería para descargar de YouTube
- **gunicorn** - Servidor WSGI
- **Docker** - Containerización

---

## 📝 Notas

- Tamaño máximo de archivo: Depende del hosting
- Timeout: 120 segundos
- Workers: 2 (configurable en Dockerfile)

---

## 🎯 Próximos Pasos

1. Desplegar en Render
2. Obtener URL de la API
3. Configurar n8n para usar la API
4. ¡Disfrutar!

---

**Creado:** 09/12/2025  
**Versión:** 1.0.0  
**Estado:** ✅ Listo para producción
