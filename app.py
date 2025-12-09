from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from pytube import YouTube
import os
import tempfile
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permitir CORS para que n8n pueda llamar la API

@app.route('/')
def home():
    return jsonify({
        'status': 'ok',
        'message': 'YouTube Downloader API',
        'endpoints': {
            '/download': 'GET - Download video/audio',
            '/info': 'GET - Get video info'
        },
        'version': '1.0.0'
    })

@app.route('/download', methods=['GET'])
def download():
    """
    Descarga un video de YouTube en MP3 o MP4
    
    Parámetros:
    - url: URL del video de YouTube
    - format: 'mp3' o 'mp4' (default: mp4)
    - quality: 'low', 'medium', 'high' (default: medium)
    """
    try:
        # Obtener parámetros
        url = request.args.get('url')
        format_type = request.args.get('format', 'mp4').lower()
        quality = request.args.get('quality', 'medium').lower()
        
        if not url:
            return jsonify({'error': 'URL parameter is required'}), 400
        
        # Crear directorio temporal
        temp_dir = tempfile.mkdtemp()
        
        # Descargar video
        yt = YouTube(url)
        
        if format_type == 'mp3':
            # Descargar solo audio
            stream = yt.streams.filter(only_audio=True).first()
            filename = f"{yt.title}.mp3"
        else:
            # Descargar video
            if quality == 'high':
                stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            elif quality == 'low':
                stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first()
            else:  # medium
                streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
                stream = streams[len(streams)//2] if len(streams) > 1 else streams.first()
            
            filename = f"{yt.title}.mp4"
        
        # Descargar archivo
        output_path = stream.download(output_path=temp_dir, filename=filename)
        
        # Enviar archivo
        return send_file(
            output_path,
            as_attachment=True,
            download_name=filename,
            mimetype='audio/mpeg' if format_type == 'mp3' else 'video/mp4'
        )
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to download video'
        }), 500

@app.route('/info', methods=['GET'])
def info():
    """
    Obtiene información de un video de YouTube
    
    Parámetros:
    - url: URL del video de YouTube
    """
    try:
        url = request.args.get('url')
        
        if not url:
            return jsonify({'error': 'URL parameter is required'}), 400
        
        yt = YouTube(url)
        
        return jsonify({
            'title': yt.title,
            'author': yt.author,
            'length': yt.length,
            'views': yt.views,
            'rating': yt.rating,
            'thumbnail': yt.thumbnail_url,
            'description': yt.description[:200] + '...' if len(yt.description) > 200 else yt.description,
            'available_formats': {
                'audio': [
                    {
                        'itag': s.itag,
                        'mime_type': s.mime_type,
                        'abr': s.abr,
                        'filesize': s.filesize
                    } for s in yt.streams.filter(only_audio=True)
                ],
                'video': [
                    {
                        'itag': s.itag,
                        'mime_type': s.mime_type,
                        'resolution': s.resolution,
                        'fps': s.fps,
                        'filesize': s.filesize
                    } for s in yt.streams.filter(progressive=True, file_extension='mp4')
                ]
            }
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to get video info'
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
