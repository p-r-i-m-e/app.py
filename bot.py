from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re

api_id = 23502077  # Add your API ID here
api_hash = '559fb1f4ee7682b63a4ed3c54d3883b6'  # Enter API Hash here
token = '7010824792:AAGX8uLjw1eN_d-TyxDHhXMTGlhtvgUADO4'  # Enter Bot Token here

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token, workers=10)

@app.on_message(filters.command("start") & filters.private)
def start(client, message):
    keyboard = [
        [InlineKeyboardButton("Chinese Anime", callback_data='1')],
        [InlineKeyboardButton("သီချင်း", callback_data='2')],
        [InlineKeyboardButton("ဘလာ 3", url='https://t.me/ongoingbyotakuzonemm/51')],
        [InlineKeyboardButton("ဘလာ 4", callback_data='4')],
        [InlineKeyboardButton("ဘလာ 5", callback_data='5')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message.reply_text('မဂ်လာပါ ', reply_markup=reply_markup)

@app.on_callback_query()
def button(client, query):
    query.answer()

    if query.data == '1':
        keyboard = [
            [InlineKeyboardButton("3D Anime", url='https://t.me/addlist/Ijx6HrpeLO5lNTNl')],
            [InlineKeyboardButton("2D Anime", url='https://t.me/addlist/Ijx6HrpeLO5lNTNl')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text="ရွေးပါ ", reply_markup=reply_markup)
    elif query.data == 'option_2':
        response_text = "2D Anime"
        query.message.edit_text(text=response_text)
    else:
        button_text = {
            '1': "Chinese Anime",
            '2': "သီချင်း",
            '4': "ဘလာ 4",
            '5': "ဘလာ 5"
        }.get(query.data, "တခုရွေးပါ")
        
        response_text = f"ဒီမှာ {button_text}: [ နှိပ်ပါ ](https://example.com/{button_text.lower().replace(' ', '_')})"
        
        # Check if the message is forwarded from another chat
        if query.message.forward_from_chat:
            response_text += "\n\nThis link is forwarded from another chat."
        
        query.message.edit_text(text=response_text, parse_mode='Markdown')

# Function to get the first sentence from a message
def get_first_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return sentences[0] if sentences else text

# Define a function to handle normal messages
@app.on_message(filters.text & filters.private)
def respond(client, message):
    user_message = message.text.lower()
    user_message = get_first_sentence(user_message)

    # Define responses based on user messages
    responses = {
        'greetings': {
            'keywords': ['hi', 'hello', 'hey', 'hi ', 'hello', 'xi', 'hey', 'xi '],
            'response': 'ဘာလာရှာတာလည်း'
        },
        'lee': {
            'keywords': ['lee'],
            'response': 'Lee lar Kmkl'
        }
            'love': {
            'keywords': ['ချစ်လား', 'ချစ်တယ်'],
            'response':   'သေလိုက်'
        },
         'girl':{
            'keywords': ['ကောင်မလေးလိုချင်တယ်','girlfriend need','ကောင်လေးလိုချင်တယ်, boyfriend need'],
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
            'keywords': ['စော်ရှိလား','ကောင်မလေးရှိလား' ],
            'response': "သုံးယောက်တောင်"
        },
        'duck_exists': {
            'keywords': ['ဘဲရှိလား'],
            'response': 'သုံးကောင်ရှိတယ်'
        },
        'name' :{
            'keywords': [ 'နာမည်' , 'နာမည်ဘယ်လိုခေါ်လည်း', 'name', 'Name' ],
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

    message.reply_text("နားမလည်ဘူး")

# Start the application
app.run()
