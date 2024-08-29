from flask import Flask, request, jsonify, render_template
import os
import spacy
import json

app = Flask(__name__)

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        result = process_transcript(file_path)
        return jsonify(result)

def process_transcript(file_path):
    # Add code to handle PDF/text processing and NLP here
    with open(file_path, 'r') as f:
        transcript = f.read()
    return extract_information(transcript)

def extract_information(text):
    doc = nlp(text)
    # Example extraction logic, modify according to your needs
    customer_requirements = {
        "Car Type": None,
        "Fuel Type": None,
        "Color": None,
        "Distance Travelled": None,
        "Make Year": None,
        "Transmission Type": None
    }
    company_policies = {
        "Free RC Transfer": None,
        "5-Day Money Back Guarantee": None,
        "Free RSA for One Year": None,
        "Return Policy": None
    }
    customer_objections = {
        "Refurbishment Quality": None,
        "Car Issues": None,
        "Price Issues": None,
        "Customer Experience Issues": None
    }

    # NLP-based entity extraction logic
    for sent in doc.sents:
        # Add your custom rules here to populate the dictionaries
        pass

    return {
        "Customer Requirements": customer_requirements,
        "Company Policies Discussed": company_policies,
        "Customer Objections": customer_objections
    }

if __name__ == '__main__':
    app.run(debug=True)
