from flask import Flask, request, render_template, jsonify
from chat_processing import validate
from chatbot import MyChatbot

app = Flask(__name__)

sessions = {}

# Endpoint 1: Via HTML
@app.route("/", methods=['GET', 'POST'])

def home():
    session_id = request.remote_addr

    # Create new session if no existing sessions found
    if session_id not in sessions.keys():
        sessions[session_id] = []
    
    if request.method == 'POST':
        user_message = request.form.get('message', '')

        # Validate user's message (should not be empty)
        errors = validate(user_message)
        if errors:
            return render_template('index.html', errors=errors,
                                   chat_history = sessions[session_id],
                                   user_input = user_message)

        # Generate response from MyChatbot.
        chatbot = MyChatbot()
        response = chatbot.generate_response(user_message)
        sessions[session_id].append({'user': user_message, 'bot': response})

        return render_template('index.html',
                               chat_history = sessions[session_id])
    else: # GET request
        return render_template('index.html',
                               chat_history = sessions.get(session_id, {}))

# Endpoint 2: Via JSON/AJAX
@app.route('/ask', methods=['POST'])

def ask():
    question = request.json.get('question')
    
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    chatbot = MyChatbot()
    response = chatbot.generate_response(question)
    
    if 'history' not in sessions:
        sessions['history'] = []
    
    sessions['history'].append({'question': question, 'response': response})
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)