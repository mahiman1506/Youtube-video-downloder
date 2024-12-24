from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import ffmpeg

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    video_url = data.get('url')

    if video_url:
        try:
            # Set the options for yt-dlp
            ydl_opts = {
                'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save video in "downloads" folder
                'format': 'best',  # Choose best quality
            }

            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
                ffmpeg.input('%(title)s.%(ext)s.mp4').output('%(title)s.%(ext)s.avi').run()

            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    return jsonify({'success': False, 'error': 'Invalid URL'})

if __name__ == '__main__':
    app.run(port=5000)
