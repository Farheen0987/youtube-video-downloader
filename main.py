from flask import Flask, render_template, request, jsonify
from pytube import YouTube

app = Flask(__name__, static_url_path='/static', static_folder='C://Users//PMLS//Documents//python//youtube video downloader//static' ,template_folder='C://Users//PMLS//Documents//python//youtube video downloader//templates//')

@app.route('/')
def index():
    return render_template('home.html' )

@app.route('/download', methods=['POST'])
def download():
    video_url = request.json.get('video_url')
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download('./downloads')  # Download to 'downloads' directory
        return jsonify({'message': 'Download successful!'})
    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
