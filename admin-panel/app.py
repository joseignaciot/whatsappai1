# admin-panel/app.py
import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

CONFIG_PATH = 'config.json'
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}

def save_config(config):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

@app.route('/config', methods=['GET'])
def get_config():
    config = load_config()
    return jsonify(config)

@app.route('/config', methods=['POST'])
def update_config():
    new_config = request.json
    if not new_config:
        return jsonify({"error": "No config data provided"}), 400
    save_config(new_config)
    return jsonify({"status": "config updated"})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"status": "file uploaded", "filename": file.filename})

@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    headers = {
        "User-Agent": load_config().get("webscraping_config", {}).get("user_agent", "Mozilla/5.0")
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = "\n".join(p.get_text() for p in paragraphs)
        return jsonify({"status": "scraped", "text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists(CONFIG_PATH):
        default_config = {
            "model_prompt": "Eres un asistente de IA que solo debe responder usando la información contenida en los documentos internos. Responde de manera precisa y basada en evidencia.",
            "finetuning_instructions": "Para finetuning, asegúrate de proporcionar ejemplos claros y consistentes. Cada entrada debe incluir 'prompt' y 'completion'.",
            "webscraping_config": {
                "user_agent": "Mozilla/5.0 (compatible; MyScraperBot/1.0; +http://tuempresa.com/bot)"
            }
        }
        save_config(default_config)
    app.run(host='0.0.0.0', port=8080)
