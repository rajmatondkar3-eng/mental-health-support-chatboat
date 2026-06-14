from flask import Flask, render_template, request, jsonify
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are MindCare AI, a warm and empathetic mental health support companion. Your role:
- Listen with compassion and validate feelings before anything else
- Offer brief, practical coping strategies when fitting (breathing, grounding, journaling)
- Keep replies concise — 2 to 4 sentences — and conversational
- Never diagnose or give medical advice
- If someone mentions self-harm, crisis, or severe distress, respond with care and clearly recommend
  they contact a crisis helpline (e.g. iCall in India: 9152987821, or international: findahelpline.com)
- Never minimise what someone shares"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    history = data.get("history", [])

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=history
    )

    reply = response.content[0].text
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
