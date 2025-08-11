from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        use_uppercase = "uppercase" in request.form
        use_numbers = "numbers" in request.form
        use_symbols = "symbols" in request.form
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
