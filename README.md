# 🎬 YouTube Downloader con yt-dlp

## ✅ Solución Definitiva y Confiable

Este proyecto implementa un bot de Telegram que descarga videos de YouTube usando **yt-dlp** directamente en el servidor.

---

## 📦 Archivos Incluidos

1. **Dockerfile** - Imagen personalizada de n8n con yt-dlp
2. **youtube-downloader-ytdlp.json** - Workflow completo de n8n
3. **README.md** - Esta guía
4. **.gitignore** - Archivos a ignorar en Git

---

## 🚀 Paso 1: Desplegar en Railway

### **1.1 Crear Repositorio Git**

```bash
cd n8n-youtube-downloader
git init
git add .
git commit -m "Initial commit: YouTube Downloader con yt-dlp"
```

### **1.2 Subir a GitHub**

```bash
# Crear repositorio en GitHub primero
git remote add origin https://github.com/TU_USUARIO/n8n-youtube-downloader.git
git branch -M main
git push -u origin main
```

### **1.3 Conectar a Railway**

1. Ve a: https://railway.app
2. Haz clic en **"New Project"**
3. Selecciona **"Deploy from GitHub repo"**
4. Selecciona tu repositorio `n8n-youtube-downloader`
5. Railway detectará el Dockerfile automáticamente
6. Espera 5-10 minutos mientras se construye

### **1.4 Configurar Variables de Entorno**

En Railway, agrega estas variables:

```
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=tu_password_seguro
N8N_HOST=0.0.0.0
N8N_PORT=5678
N8N_PROTOCOL=https
WEBHOOK_URL=https://tu-app.railway.app/
```

---

## 🎯 Paso 2: Importar Workflow en n8n

### **2.1 Acceder a n8n**

1. Abre tu instancia de n8n en Railway
2. Inicia sesión con las credenciales que configuraste

### **2.2 Importar Workflow**

1. Menú (☰) → **Workflows** → **Import from File**
2. Selecciona: `youtube-downloader-ytdlp.json`
3. Haz clic en **Import**

### **2.3 Configurar Credenciales de Telegram**

1. Abre cada nodo de Telegram en el workflow
2. Selecciona tu credencial de Telegram existente
3. O crea una nueva con tu Bot Token

### **2.4 Activar Workflow**

1. Haz clic en **"Save"**
2. Activa el workflow (toggle ON)
3. ¡Listo!

---

## 🎮 Paso 3: Usar el Bot

### **Descargar MP3 (Audio):**

Envía al bot:
```
https://youtube.com/watch?v=dQw4w9WgXcQ mp3
```

### **Descargar MP4 (Video):**

Envía al bot:
```
https://youtu.be/dQw4w9WgXcQ video
```

---

## 📊 Workflow Explicado

### **Nodos (12 total):**

1. **Telegram Trigger** - Recibe mensajes
2. **Validate URL** - Valida URL de YouTube
3. **Should Stop?** - Verifica errores
4. **Send Error** - Envía mensaje de error
5. **Send Processing** - Envía "Descargando..."
6. **Switch Format** - Decide MP3 o MP4
7. **Download MP3** - Ejecuta yt-dlp para audio
8. **Download MP4** - Ejecuta yt-dlp para video
9. **Parse File Path** - Obtiene ruta del archivo
10. **Read File** - Lee el archivo descargado
11. **Send Document** - Envía archivo al usuario
12. **Cleanup File** - Elimina archivo temporal

---

## 🔧 Comandos yt-dlp Usados

### **Para MP3:**
```bash
yt-dlp -f 'bestaudio' -x --audio-format mp3 -o '/tmp/%(title)s.%(ext)s' 'URL'
```

### **Para MP4:**
```bash
yt-dlp -f 'best[height<=720]' -o '/tmp/%(title)s.%(ext)s' 'URL'
```

---

## ✅ Ventajas de esta Solución

- ✅ **100% Confiable** - yt-dlp siempre funciona
- ✅ **Gratis para Siempre** - Sin APIs de terceros
- ✅ **Sin Límites** - Descargas ilimitadas
- ✅ **Actualizado** - yt-dlp se actualiza constantemente
- ✅ **Todos los Formatos** - MP3, MP4, cualquier calidad
- ✅ **Rápido** - Descarga directa en el servidor

---

## ⚠️ Limitaciones

### **Telegram:**
- Tamaño máximo de archivo: 50 MB (bots)
- Tamaño máximo de archivo: 2 GB (con Telegram Premium)

### **Solución:**
- Limitar calidad de video a 720p
- Usar solo MP3 para videos largos

---

## 🔧 Personalización

### **Cambiar Calidad de Video:**

En el nodo "Download MP4", modifica:
```bash
# 480p
yt-dlp -f 'best[height<=480]' ...

# 1080p
yt-dlp -f 'best[height<=1080]' ...
```

### **Cambiar Formato de Audio:**

En el nodo "Download MP3", modifica:
```bash
# M4A
yt-dlp -f 'bestaudio' -x --audio-format m4a ...

# OGG
yt-dlp -f 'bestaudio' -x --audio-format ogg ...
```

---

## 🐛 Solución de Problemas

### **Error: "yt-dlp: command not found"**

**Solución:**
- Verifica que el Dockerfile se haya construido correctamente
- Reconstruye la imagen en Railway

### **Error: "Permission denied"**

**Solución:**
- Verifica que el directorio `/tmp` sea escribible
- Cambia la ruta a otro directorio si es necesario

### **Video muy grande**

**Solución:**
- Reduce la calidad del video
- Usa MP3 en lugar de MP4

---

## 📝 Mantenimiento

### **Actualizar yt-dlp:**

Railway reconstruirá la imagen automáticamente cuando hagas push a Git.

Para forzar actualización:
```bash
git commit --allow-empty -m "Rebuild: Update yt-dlp"
git push
```

---

## 💰 Costos

- **Railway:** Plan gratuito incluye $5/mes de créditos
- **n8n:** Gratis (self-hosted)
- **yt-dlp:** Gratis (open source)
- **Telegram:** Gratis

**Total: $0/mes** (dentro del plan gratuito de Railway)

---

## 🎉 ¡Felicidades!

Ahora tienes un bot de YouTube Downloader:
- ✅ 100% funcional
- ✅ Gratis
- ✅ Sin límites
- ✅ Confiable

**¡Disfrútalo!** 🎬✨

---

**Creado:** 09/12/2025  
**Versión:** 1.0  
**Estado:** ✅ Listo para producción
