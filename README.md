# My Chatbot

This is a simple end-to-end chatbot application built with Flask and vanilla JavaScript. This project demonstrates basic conversational AI functionality without using external AI APIs.

![alt text](/img/my_chatbot.png)

## Features

- Clean, responsive web interface
- Real-time chat with mock AI responses
- Session-based conversation history
- Loading indicator with animated typing dots
- Interactive prompt buttons for quick conversation starters
- Input validation and error handling
- Mobile-friendly design

## Tech Stack

**Backend:**
- Python 3.13.17
- Flask web framework
- Flask sessions for state management

**Frontend:**
- HTML5
- CSS3 with Flexbox/Grid
- Vanilla JavaScript (ES6+)
- Google Fonts (Outfit)

## Project Structure

```
my-chatbot/
├── app.py                # Main Flask application
├── chatbot.py            # Chatbot response logic
├── chat_processing.py    # Input validation
├── requirements.txt      # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css    # Stylesheet
│   └── script.js        # Frontend JavaScript
├── templates/
│   └── index.html       # Main HTML template
└── README.md
```

## Requirements
- Python 3.9 or higher (needed for Flask 3.0)
- A code editor like Visual Studio Code, PyCharm, etc
- `virtualenv`
  - If you do not have `virtualenv` installed, you can install it using `pip install virtualenv` on your terminal

Please ensure these requirements are met before moving to **Installation and Setup**.

## Installation & Setup

1. **Clone this repository in your desired directory**
   ```bash
   git clone https://github.com/dorcasshee/my-chatbot
   cd my-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   virtualenv venv
   ```

3. **Activate virtual environment**  
   *Windows Command Prompt:*
   ```bash
   venv\Scripts\activate
   ```
   *MacOS/Linux/Windows Git Bash Terminal:*
   ```bash
   source venv/bin/activate
   ```
   If activation is successful, your terminal prompt will reflect `(venv)`.

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```
   If it runs successfully, you should see this:
   ![alt text](/img/successful_flask_app.png)

6. **Open development server in browser**  
   Navigate to `http://localhost:5000` (or whichever URL is indicated)

## Usage
1. **Welcome Screen**: Click on prompt buttons for quick conversation starters  
   ![alt text](/img/welcome-screen.gif)
2. **Chat Interface**: Type messages in the input box and press Enter or click Send  
   ![alt text](/img/chat-interface.gif)
3. **Conversation Types**:  
   The chatbot can respond to:
   - Greetings ("hello", "hi", "hey", "yo")
   - Joke requests ("Tell me a joke")
   - Fun fact requests ("Tell me a fun fact")
   - General company information ("Tell me about Visa")
   - General capabilities inquiry ("What can you do?")

## API Endpoints

- `GET /` - Serves the main chat interface
- `POST /chat` - Processes chat messages and returns responses

## Response Categories
The chatbot includes mock responses for:
- Greetings: Various friendly welcomes
- Jokes: Collection of clean, professional jokes
- Fun Facts: Interesting facts including fintech-related content
- Company Info: Information about Visa Inc.
- Capabilities: What the chatbot can help with

## Development Notes
- Built as a prototype demonstrating full-stack development skills
- Uses mock responses instead of real AI services
- Designed for rapid deployment and testing
- Follows separation of concerns principles

## Browser Compatibility
- Modern browsers with ES6+ support
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## License
This project is for demonstration purposes.