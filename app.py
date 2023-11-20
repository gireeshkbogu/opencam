from flask import Flask, render_template, request, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

# Define the folder where you want to move the images to
DATA_GRILL_FOLDER = 'data_grill'

# Ensure the folder exists, create it if it doesn't
if not os.path.exists(DATA_GRILL_FOLDER):
    os.makedirs(DATA_GRILL_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        # Generate a timestamp to include in the filename
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        
        # Create a unique filename with the timestamp
        filename = f"{timestamp}_{file.filename}"
        
        # Save the uploaded image to the DATA_GRILL_FOLDER
        file.save(os.path.join(DATA_GRILL_FOLDER, filename))
        
        return 'File uploaded successfully'

# Serve static files from the 'static' folder
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/data_grill/<filename>')
def get_image(filename):
    return send_from_directory(DATA_GRILL_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
