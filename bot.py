from pyrogram import Client, filters
import re

api_id = 23502077  # --Add your Api Id here
api_hash = '559fb1f4ee7682b63a4ed3c54d3883b6'  # --Enter Api Hash Here
token = '7010824792:AAGX8uLjw1eN_d-TyxDHhXMTGlhtvgUADO4'  # --Enter Bot Token Here

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)

# Define a function to handle the /start command
@app.on_message(filters.command("start") & ~filters.me)
def start(client, message):
    message.reply_text('Hi! I am Ezikel.')  

# Function to get the first sentence from a message
def get_first_sentence(text):
    # Use regular expression to split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return sentences[0] if sentences else text

# Define a function to handle normal messages
@app.on_message(filters.text & ~filters.me)
def respond(client, message):
    user_message = message.text.lower()
    user_message = get_first_sentence(user_message)
    
    # Define responses based on user messages
    if 'hi' in user_message:
        message.reply_text('Hi! ဘာလာရှာတာလည်း?')
    elif 'lee' in user_message:
        message.reply_text('Lee lar Kmkl')
    elif 'နေကောင်းလား' in user_message:
        message.reply_text("ကောင်းတယ်")
    elif 'ဘယ်သူလည်း' in user_message:
        message.reply_text("မင်းဖေ")
    elif 'ကောင်မလေး' in user_message:
        message.reply_text("S FA ကောင်")
    elif 'ကောင်လေး' in user_message:
        message.reply_text("ဘဲပစ်မ")
    elif 'စားပြီးပြီလား' in user_message:
        message.reply_text("မစားရသေးဘူး၊ကျွေးမှာလား?")
    elif 'ဘာလုပ်' in user_message:
        message.reply_text("စော်နဲ့ချက်")
    elif 'ေစာ်ရှိလား' in user_message:
        message.reply_text("သုံးယောက်တောင်")
    elif 'ဘဲရှိလား' in user_message:
        message.reply_text("သုံးကောင်ရှိ")
    elif 'နာမည်ဘယ်လို‌ေခါ်လည်း' in user_message:
        message.reply_text("ဆရာကြီး")
    elif '‌ေစာ်ရှာ‌ေပး' in user_message:
        message.reply_text("ငှက်ပျောပင်စိုက်")
    elif 'ချစ်လား' in user_message:
        message.reply_text("သေလိုက်")
    elif 'ချစ်တယ်' in user_message:
        message.reply_text("ကောင်မလေးရှိတယ်")
    elif 'ကောင်မလေးရှာ‌ေပး' in user_message:
        message.reply_text("ငှက်ပျောပင်စိုက်")
    # Add more response conditions here...
    else:
        message.reply_text("လူနားလည်အောင်ပြော")

# Start the application
app.run()
