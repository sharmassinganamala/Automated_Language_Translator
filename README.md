# Language Translation

This is a simple web-based application that translates user-provided text into different languages using Google Translate API.

## Features
- User-friendly interface
- Multiple language selection
- Instant text translation
- Error handling with supported languages list

## Technologies Used
- HTML
- CSS
- JavaScript
- Python (Flask)
- Google Translate API

## Folder Structure
```
translator_app/
├─ app.py              # Backend server code
├─ templates/
│  └─ index.html      # Frontend HTML file
└─ requirements.txt    # List of dependencies
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/username/translator_app.git
cd translator_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to:
```
http://localhost:5000
```

## API Endpoints
- `POST /translate`
    - Request Body:
      ```json
      {
        "text": "Hello",
        "dest_language": "fr"
      }
      ```
    - Response:
      ```json
      {
        "translated_text": "Bonjour"
      }
      ```

## Supported Languages
The supported languages are dynamically fetched using Google Translate API.


