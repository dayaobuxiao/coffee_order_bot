from flask import render_template, jsonify, request
from app import app
from app.utils import CoffeeOrderAssistant

assistant = CoffeeOrderAssistant()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def handle_input():
    user_input = request.json['user_input']
    response = assistant.process_input(user_input)
    return jsonify(response)