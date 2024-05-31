from pyrogram import Client, filters
import requests
import random

api_id = 23502077 #--Add your Api Id here
api_hash = '559fb1f4ee7682b63a4ed3c54d3883b6' #--Enter Api Hash Here

token = '7010824792:AAGX8uLjw1eN_d-TyxDHhXMTGlhtvgUADO4' #--Enter Bot Token Here.

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)

# Define a function to handle the /start command
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text('Hi! I am Xiu.')

# Define a function to handle normal messages
@app.on_message(filters.text)
def respond(client, message):
    user_message = message.text.lower()
    
    # Define responses based on user messages
    if 'hi' in user_message:
        message.reply_text('Hi! ဘာလာရှာတာလည်း?')
    elif 'lee' in user_message:
        message.reply_text('Lee lar Kmkl')
    elif 'နေကောင်းလား'  in user_message:
        message.reply_text("ကောင်းတယ်")
    # Add more response conditions here...
    else:
        message.reply_text("လူနားလည်အောင်ပြော")

app.run()
