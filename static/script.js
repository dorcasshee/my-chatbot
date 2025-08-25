document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('chat-form')
    const userInput = document.getElementById('user-input')
    const welcomeScreen = document.getElementById('welcome-screen')
    const chatHistory = document.getElementById('chat-history')
    const loader = document.getElementById('loader')
    const errorDiv = document.getElementById('error-message')

    const SENDER_CONFIG = {
        user: {
            className: 'user-message',
            username: "You"
        },
        chatbot: {
            className: 'chatbot-message',
            username: 'My Chatbot'
        }
    };

    let isFirstMessage = true;

    document.querySelectorAll('.prompt-btn').forEach(button => {
        button.addEventListener('click', function() {
            const text = this.textContent.trim().replace(/^[^\s]+\s/, '');
            userInput.value = text;
            form.dispatchEvent(new Event('submit'));
        });
    });

    userInput.addEventListener('input', autoResize);

    userInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault(); // prevent new line
            form.dispatchEvent(new Event('submit')); // submit form
        }
        setTimeout(autoResize, 0);
    });

    form.addEventListener('submit', async function(event) {
        event.preventDefault(); // don't reload page

        setTimeout(autoResize, 0);

        const message = userInput.value.trim();
        if (!message) return; // do not send empty messages

        if (isFirstMessage) {
            hideWelcomeScreen();
            showChatHistory();
            isFirstMessage = false;
        }

        addMessage(message, 'user'); // add user message to current session history

        // clear user input from text box and show loader
        userInput.value = '';
        showLoading();
        hideError();

        try {
            const response = await fetch ('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ question: message })
            });

            const data = await response.json();

            if (response.ok) {
                addMessage(data.response, 'chatbot'); // successful response; chatbot response
            } else {
                showError(data.error);
            }
        } catch (error) {
            showError('Something went wrong. Please try again.');
        } finally {
            hideLoading();
        }
    });

    // helper functions
    function autoResize() {
        userInput.style.height = 'auto';
        userInput.style.overflow = 'hidden';

        const scrollHeight = userInput.scrollHeight;
        const minHeight = 40;
        const maxHeight = 150;

        if (scrollHeight <= maxHeight) {
            const newHeight = scrollHeight < minHeight ? minHeight : scrollHeight;

            userInput.style.height = newHeight + 'px';
            userInput.style.overflow = 'hidden';
        } else {
            userInput.style.height = maxHeight + 'px';
            userInput.style.overflow = 'auto';
        }
    }

    function addMessage(message, senderType) {
        const messageDiv = document.createElement('div');
        const config = SENDER_CONFIG[senderType];

        messageDiv.className = config.className;
        messageDiv.innerHTML = `
            <div class="message-content">
                <strong>${config.username}:</strong> ${message}
            </div>
        `;

        chatHistory.appendChild(messageDiv);
        scrollToBottom();
    }

    function hideWelcomeScreen() {
        welcomeScreen.style.display = 'none';
    }

    function showChatHistory() {
        chatHistory.style.display = 'flex';
        chatHistory.style.flexDirection = 'column';
    }

    function showLoading() {
        loader.style.display = 'block';
    }
    
    function hideLoading() {
        loader.style.display = 'none';
    }
    
    function showError(errorMessage) {
        errorDiv.textContent = errorMessage;
        errorDiv.style.display = 'block';
    }
    
    function hideError() {
        errorDiv.style.display = 'none';
    }
    
    function scrollToBottom() {
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    autoResize();
})