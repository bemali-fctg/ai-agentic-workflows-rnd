from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-zodiac', methods=['POST'])
def get_zodiac():
    data = request.json
    age = data.get('age')
    if not age or not str(age).isdigit():
        return jsonify({"error": "Invalid age"}), 400

    zodiac = random.choice(zodiac_signs)
    return jsonify({"age": age, "zodiac": zodiac})

if __name__ == '__main__':
    app.run(debug=True)
