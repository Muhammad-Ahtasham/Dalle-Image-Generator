from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, send_file, jsonify, send_from_directory
from generate_image import generate_image
import os
import traceback

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    if prompt:
        try:
            saved_files = generate_image(prompt)
            # Convert file paths to URLs for frontend display
            image_urls = [url_for('generated_image', filename=os.path.basename(f)) for f in saved_files]
            return jsonify({'image_urls': image_urls}), 200
        except Exception as e:
            print("Exception occurred:", e)
            traceback.print_exc()
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'No prompt provided'}), 400

@app.route('/generated_images/<filename>')
def generated_image(filename):
    return send_from_directory('Generated Images', filename)

@app.route('/gallery')
def gallery():
    # List all images in 'Generated Images' directory
    image_files = []
    try:
        image_files = [f for f in os.listdir('Generated Images') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    except Exception as e:
        image_files = []
    return render_template('gallery.html', image_files=image_files)

@app.route('/about')
def about():
    return render_template('about.html')


# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)  