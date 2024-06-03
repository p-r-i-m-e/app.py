from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from flask import Flask, request
import random
import re
import threading

api_id = 23502077  # Add your API ID here
api_hash = '559fb1f4ee7682b63a4ed3c54d3883b6'  # Enter API Hash here
token = '7010824792:AAGX8uLjw1eN_d-TyxDHhXMTGlhtvgUADO4'  # Enter Bot Token here

# Initialize the Telegram bot client
tg_app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token, workers=10)

# Initialize the Flask app
flask_app = Flask(__name__)

@flask_app.route('/start', methods=['POST'])
def start():
    return "Send any message to get a random emoji!"

@flask_app.route('/message', methods=['POST'])
def message():
    data = request.json
    message_text = data['message']['text']
    if any(char in message_text for char in ['😊', '🚀', '🎉', '🌟', '🐱', '🌈']):
        return "I recognized that emoji! 😊"
    else:
        emojis = ['😊', '🚀', '🎉', '🌟', '🐱', '🤪', '💠', '🔒', '🇲🇲', '😁', '🌚', '😶', '😅', '🐯', '😂', '😄', '🫤', '😠', '😡', '🥰', '🤤', '😛', '🥺', '😝', '🤭', '😎', '😸']
        random_emoji = random.choice(emojis)
        return random_emoji

@tg_app.on_message(filters.command("start") & filters.private)
def start_command(client, message):
    keyboard = [
        [InlineKeyboardButton("Chinese Anime", callback_data='1')],
        [InlineKeyboardButton("သီချင်း", callback_data='2')],
        [InlineKeyboardButton("ဘလာ 3", url='https://t.me/ongoingbyotakuzonemm/51')],
        [InlineKeyboardButton("ဘလာ 4", callback_data='4')],
        [InlineKeyboardButton("ဘလာ 5", callback_data='5')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message.reply_text('မဂ်လာပါ', reply_markup=reply_markup)

@tg_app.on_callback_query()
def button(client, query):
    query.answer()

    if query.data == '1':
        keyboard = [
            [InlineKeyboardButton("3D Anime", url='https://t.me/addlist/Ijx6HrpeLO5lNTNl')],
            [InlineKeyboardButton("2D Anime", url='https://t.me/addlist/Ijx6HrpeLO5lNTNl')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text="ရွေးပါ", reply_markup=reply_markup)
    elif query.data == '2':
        response_text = "2D Anime"
        query.message.edit_text(text=response_text)
    else:
        button_text = {
            '1': "Chinese Anime",
            '2': "သီချင်း",
            '4': "ဘလာ 4",
            '5': "ဘလာ 5"
        }.get(query.data, "တခုရွေးပါ")
        response_text = f"ဒီမှာ {button_text}: [နှိပ်ပါ](https://example.com/{button_text.lower().replace(' ', '_')})"
        query.message.edit_text(text=response_text)

def get_first_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return sentences[0] if sentences else text

@tg_app.on_message(filters.text & filters.private)
def respond(client, message):
    user_message = message.text.lower()
    user_message = get_first_sentence(user_message)

    responses = {
        'greetings': {
            'keywords': ['hi', 'hello', 'hey'],
            'response': 'ဘာလာရှာတာလည်း'
        },
        'lee': {
            'keywords': ['lee', 'လီး', 'kmkl', 'mml'],
            'response': 'Lee lar Kmkl'
        },
        'love': {
            'keywords': ['ချစ်လား', 'ချစ်တယ်'],
            'response': 'သေလိုက်'
        },
        'girl': {
            'keywords': ['ကောင်မလေးလိုချင်တယ်', 'girlfriend need', 'ကောင်လေးလိုချင်တယ်', 'boyfriend need'],
            'response': 'FA ကောင်'
        },
        'food': {
            'keywords': ['စားပြီးပြီလား'],
            'response': "မစားရသေးဘူး၊ကျွေးမှာလား?"
        },
        'doing': {
            'keywords': ['ဘာလုပ်'],
            'response': 'စော်နဲ့ချက်'
        },
        'girl_exists': {
            'keywords': ['စော်ရှိလား', 'ကောင်မလေးရှိလား'],
            'response': "သုံးယောက်တောင်"
        },
        'duck_exists': {
            'keywords': ['ဘဲရှိလား'],
            'response': 'သုံးကောင်ရှိတယ်'
        },
        'name': {
            'keywords': ['နာမည်', 'နာမည်ဘယ်လိုခေါ်လည်း', 'name'],
            'response': "ဆရာကြီး"
        },
        'find_girl': {
            'keywords': ['ေစာ်ရှာ‌ေပး', 'ကောင်မလေးရှာ‌ေပး'],
            'response': "ငှက်ပျောပင်စိုက်"
        },
    }

    for category, data in responses.items():
        if any(keyword in user_message for keyword in data['keywords']):
            message.reply_text(data['response'])
            return

    send_random_emoji(message)

def send_random_emoji(message):
    emojis = ['😊', '🚀', '🎉', '🌟', '🐱', '🌈']
    random_emoji = random.choice(emojis)
    message.reply_text(random_emoji)

def run_flask():
    flask_app.run(port=5000)

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    tg_app.run()
