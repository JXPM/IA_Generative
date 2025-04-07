from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Authentification OpenRouter
openai.api_key = "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"  # ← Change ici par TA vraie clé
openai.api_base = "https://openrouter.ai/api/v1"

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        response_text = response["choices"][0]["message"]["content"]
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
