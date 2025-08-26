# My Chatbot
This is a simple end-to-end chatbot application built with Flask and vanilla JavaScript. This project demonstrates basic conversational AI functionality without using external AI APIs.  
  
You can access it at **[https://my-chatbot-0lpm.onrender.com/](https://my-chatbot-0lpm.onrender.com/)**.
  
![alt text](/img/my_chatbot.png)

## Features
- Clean, responsive web interface
- Real-time chat with mock responses instead of AI responses
- Interactive prompt buttons for quick conversation starters
- Session-based conversation history
- Input validation and error handling

## Project Structure
- `app.py` - main Flask app
- `chatbot.py` - Chatbot logic
- `requirements.txt` - Python dependencies for this project
- `/static/script.js` - Frontend JavaScript
- `/templates/index.html` - Main HTML template
- `/static/css/style.css` - CSS stylesheet

## Tech Stack
**Backend:**
- Python 3.13.7
- Flask's web framework and `sessions`

**Frontend:**
- HTML5
- CSS3 with Flexbox/Grid
- Vanilla JavaScript (ES6+)
- Google Fonts (Outfit)

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
   .venv\Scripts\activate
   ```
   *MacOS/Linux/Windows Git Bash Terminal:*
   ```bash
   source .venv/bin/activate
   ```
   If activation is successful, your terminal prompt will reflect `(venv)` or `(.venv)`.

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

## Development Notes
- Built as a prototype demonstrating full-stack development skills
- Uses mock responses instead of real AI services
- Designed for rapid deployment and testing

## Browser Compatibility
- Modern browsers with ES6+ support
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+
