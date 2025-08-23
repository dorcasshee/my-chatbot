from flask import Flask, request, render_template, jsonify, session
from chat_processing import validate
from chatbot import MyChatbot
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Endpoint 1: Via HTML
@app.route("/", methods=['GET'])
def home():
    return render_template('index.html') # shows initial chatbot homepage

# Endpoint 2: Via JSON/AJAX
@app.route('/chat', methods=['POST'])
def chat():
    question = request.json.get('question')
    
    # validate user's query
    errors = validate(question)
    if errors:
        return jsonify({'error': errors[0]}), 400 # show first error, change to show all later
    
    # generate a response from MyChatbot
    chatbot = MyChatbot() # shift to global later
    response = chatbot.generate_response(question)
    
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    session['chat_history'].append({'question': question, 'response': response})
    
    return jsonify({'response': response, 'chat_history': session['chat_history']})

# # Optional: endpoint to get chat history
# @app.route('/history', methods=['GET'])
# def get_history():
#     return jsonify({'chat_history': session.get('chat_history', [])})

if __name__ == '__main__':
    app.run(debug=True)