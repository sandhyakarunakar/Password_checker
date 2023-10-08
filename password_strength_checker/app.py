from flask import Flask, render_template, request

import re

app = Flask(__name__)

def check_password_strength(password):
    # Define regex patterns for different criteria
    length_pattern = r".{8,}"  # At least 8 characters
    uppercase_pattern = r"[A-Z]"  # At least one uppercase letter
    lowercase_pattern = r"[a-z]"  # At least one lowercase letter
    digit_pattern = r"\d"  # At least one digit
    special_char_pattern = r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]"  # At least one special character

    # List of criteria and their corresponding patterns
    criteria = [
        ("Minimum 8 characters", length_pattern),
        ("At least one uppercase letter", uppercase_pattern),
        ("At least one lowercase letter", lowercase_pattern),
        ("At least one digit", digit_pattern),
        ("At least one special character", special_char_pattern)
    ]

    # Check each criterion and provide feedback
    strength = 0
    feedback = []
    for criterion, pattern in criteria:
        if re.search(pattern, password):
            strength += 1
            feedback.append(f"✓ {criterion}")
        else:
            feedback.append(f"✗ {criterion}")

    # Determine password strength level
    if strength == 5:
        strength_level = "Strong 🙌"
    elif strength >= 3:
        strength_level = "Moderate 🤔"
    else:
        strength_level = "Weak 🙄"

    return strength_level, feedback

@app.route("/", methods=["GET", "POST"])
def index():
    strength_level = None
    feedback = []
    entered_password = None  # Initialize entered_password

    if request.method == "POST":
        entered_password = request.form["password"]  # Get the entered password
        strength_level, feedback = check_password_strength(entered_password)

    return render_template("index.html", strength_level=strength_level, feedback=feedback, entered_password=entered_password)

if __name__ == "__main__":
    app.run(debug=True)
