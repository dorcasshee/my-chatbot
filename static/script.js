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
            const text = this.textContent.trim();
            userInput.value = text == 'Say hello' ? 'Hello!' : text;
            form.dispatchEvent(new Event('submit'));
        });
    });

    userInput.addEventListener('input', autoResize);

    userInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            form.dispatchEvent(new Event('submit'));
        }
        setTimeout(autoResize, 0);
    });

    form.addEventListener('submit', async function(event) {
        event.preventDefault(); // don't reload page

        setTimeout(autoResize, 0);

        const message = userInput.value.trim();
        if (!message) return;

        if (isFirstMessage) {
            hideWelcomeScreen();
            showChatHistory();
            isFirstMessage = false;
        }

        addMessage(message, 'user');

        userInput.value = '';
        showLoading();
        hideError();

        const randomDelay = Math.random() * (1500 - 800) + 800;
        await new Promise(resolve => setTimeout(resolve, randomDelay));

        try {
            const response = await fetch ('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ question: message })
            });

            const data = await response.json();

            if (response.ok) {
                addMessage(data.response, 'chatbot');
            } else {
                showError(data.error);
            }
        } catch (error) {
            showError('Something went wrong. Please try again.');
        } finally {
            hideLoading();
        }
    });

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
                <strong>${config.username}:</strong><br>${message.replace(/\n/g, '<br>')}
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
        const loadingDiv = document.createElement('div')
        loadingDiv.className = 'chatbot-message';
        loadingDiv.id = 'loader';
        loadingDiv.innerHTML = `
            <div class="message-content">
                <em>My Chatbot is typing</em>
                <div class="dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        `;

        chatHistory.appendChild(loadingDiv);
        scrollToBottom();
    }
    
    function hideLoading() {
        const loader = document.getElementById('loader');

        if (loader) {
            loader.remove();
        }
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