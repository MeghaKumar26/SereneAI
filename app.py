from flask import Flask, render_template, request, jsonify
from serene_ai import get_bot_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    user_msg = request.json['message']
    bot_reply = get_bot_response(user_msg)
    return jsonify({'reply': bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
