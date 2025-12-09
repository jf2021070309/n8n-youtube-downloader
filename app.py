from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import subprocess
import os
import tempfile
from datetime import datetime
import re

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        'status': 'ok',
        'message': 'YouTube Downloader API (yt-dlp)',
        'endpoints': {
            '/download': 'GET - Download video/audio',
            '/info': 'GET - Get video info'
        },
        'version': '2.0.0'
    })

@app.route('/download', methods=['GET'])
def download():
    """
    Descarga un video de YouTube en MP3 o MP4 usando yt-dlp
    """
    try:
        url = request.args.get('url')
        format_type = request.args.get('format', 'mp4').lower()
        quality = request.args.get('quality', 'medium').lower()
        
        if not url:
            return jsonify({'error': 'URL parameter is required'}), 400
        
        # Limpiar URL
        if '?' in url and 'watch?v=' not in url:
            url = url.split('?')[0]
        
        print(f"Downloading: {url}, format: {format_type}, quality: {quality}")
        
        # Crear directorio temporal
        temp_dir = tempfile.mkdtemp()
        
        # Construir comando yt-dlp
        if format_type == 'mp3':
            output_template = os.path.join(temp_dir, '%(title)s.%(ext)s')
            cmd = [
                'yt-dlp',
                '-f', 'bestaudio',
                '-x',
                '--audio-format', 'mp3',
                '-o', output_template,
                url
            ]
        else:
            output_template = os.path.join(temp_dir, '%(title)s.%(ext)s')
            if quality == 'high':
                format_str = 'best[height<=1080]'
            elif quality == 'low':
                format_str = 'best[height<=480]'
            else:  # medium
                format_str = 'best[height<=720]'
            
            cmd = [
                'yt-dlp',
                '-f', format_str,
                '-o', output_template,
                url
            ]
        
        print(f"Running command: {' '.join(cmd)}")
        
        # Ejecutar yt-dlp
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode != 0:
            print(f"yt-dlp error: {result.stderr}")
            return jsonify({
                'error': 'Download failed',
                'details': result.stderr
            }), 500
        
        # Buscar archivo descargado
        files = os.listdir(temp_dir)
        if not files:
            return jsonify({'error': 'No file downloaded'}), 500
        
        downloaded_file = os.path.join(temp_dir, files[0])
        filename = files[0]
        
        print(f"Download complete: {downloaded_file}")
        
        # Determinar mimetype
        if format_type == 'mp3' or filename.endswith('.mp3'):
            mimetype = 'audio/mpeg'
        else:
            mimetype = 'video/mp4'
        
        # Enviar archivo
        return send_file(
            downloaded_file,
            as_attachment=True,
            download_name=filename,
            mimetype=mimetype
        )
        
    except subprocess.TimeoutExpired:
        return jsonify({
            'error': 'Download timeout',
            'message': 'Download took too long (>120s)'
        }), 504
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'error': str(e),
            'message': 'Failed to download video'
        }), 500

@app.route('/info', methods=['GET'])
def info():
    """
    Obtiene información de un video usando yt-dlp
    """
    try:
        url = request.args.get('url')
        
        if not url:
            return jsonify({'error': 'URL parameter is required'}), 400
        
        # Ejecutar yt-dlp para obtener info
        cmd = ['yt-dlp', '--dump-json', url]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            return jsonify({
                'error': 'Failed to get video info',
                'details': result.stderr
            }), 500
        
        import json
        video_info = json.loads(result.stdout)
        
        return jsonify({
            'title': video_info.get('title'),
            'uploader': video_info.get('uploader'),
            'duration': video_info.get('duration'),
            'view_count': video_info.get('view_count'),
            'thumbnail': video_info.get('thumbnail'),
            'description': video_info.get('description', '')[:200] + '...'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to get video info'
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    # Verificar que yt-dlp esté instalado
    try:
        result = subprocess.run(
            ['yt-dlp', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        yt_dlp_version = result.stdout.strip() if result.returncode == 0 else 'not installed'
    except:
        yt_dlp_version = 'not installed'
    
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'yt_dlp_version': yt_dlp_version
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
