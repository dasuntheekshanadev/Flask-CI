from flask import Flask, jsonify
import bcrypt

app = Flask(__name__)

# Serve a JSON file
@app.route('/')
def serve_json():
    try:
        with open('data.json', 'r') as file:
            data = file.read()
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
