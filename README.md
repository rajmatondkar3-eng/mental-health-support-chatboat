# MindCare AI

A mental health support chatbot powered by Flask and Claude AI.

## Project structure

```
mindcare/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

## Setup

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Anthropic API key**
   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here   # Mac/Linux
   set ANTHROPIC_API_KEY=your_api_key_here      # Windows
   ```
   Get your key at: https://console.anthropic.com

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```
