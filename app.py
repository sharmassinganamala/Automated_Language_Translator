# app.py
from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    """Render the home page with supported languages."""
    languages = LANGUAGES
    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['POST'])
def translate():
    """Translate text from English to a selected language and show supported languages if needed."""
    data = request.get_json()
    text = data.get('text')
    dest_language = data.get('dest_language')

    if dest_language not in LANGUAGES:
        # Include supported languages in the response if an invalid code is provided
        return jsonify({
            'error': 'Invalid language code',
            'supported_languages': LANGUAGES
        }), 400

    try:
        translated = translator.translate(text, dest=dest_language)
        return jsonify({'translated_text': translated.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
