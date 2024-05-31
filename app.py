from flask import Flask, request
from bot import create_app

# Create a Flask application
app = Flask(__name__)

# Initialize the bot application
bot_token = "010824792:AAGX8uLjw1eN_d-TyxDHhXMTGlhtvgUADO4"  # Replace with your actual bot token
telegram_bot_app = create_app(bot_token)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'This Bot is made by Ezikel'

# Define a route for Telegram webhook
@app.route('/webhook', methods=['POST'])
def webhook() -> str:
    update = telegram_bot_app.update_queue.get_update(request.get_json(force=True))
    telegram_bot_app.process_update(update)
    return 'ok'

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
