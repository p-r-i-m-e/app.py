from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Hi! I am Xiu.')

# Define a function to handle normal messages
def respond(update, context):
    user_mes issage = update.message.text.lower()
    
    # Define responses based on user messages
    if 'hi' in user_message:
        update.message.reply_text('Hi! ဘာလာရှာတာလည်း?')
    elif 'lee' in user_message:
        update.message.reply_text('Lee lar Kmkl')
    elif 'နေကောင်းလား'  in user_message:
        update.message.reply_text("ကောင်းတယ်")
    elif 'ဘယ်သူလည်း' in user_message:
        update.message.reply_text("မင်းဖေ")
    elif 'ကောင်မလေး' in user_message:
        update.message.reply_text(" S FA ကောင်")
    elif 'ကောင်လေး' in user_message:
        update.message.reply_text(" ဘဲပစ်မ ")
    elif 'စားပြီးပြီလား' in user_message:
        update.message.reply_text(" မစားရသေးဘူး၊ကျွေးမှာလား? ")
    elif 'ဘာလုပ်' in user_message:
        update.message.reply_text("စော်နဲ့ချက်")
    elif 'ေစာ်ရှိလား' in user_message:
        update.message.reply_text("သုံးယောက်တောင် ")
    elif 'ဘဲရှိလား' in user_message:
        update.message.reply_text(" သုံးကောင်ရှိ ")
    elif 'နာမည်ဘယ်လုိ‌ေခါ်လည်း' in user_message:
        update.message.reply_text(" ဆရာကြီး")
    elif '‌ေစာ်ရှာ‌ေပး' in user_message:
        update.message.reply_text(" ငှက်ပျောပင်စိုက်")
    elif 'ချစ်လား' in user_message:
        update.message.reply_text(" သေလိုက် ")
    elif 'ချစ်တယ်' in user_message:
        update.message.reply_text("ကောင်မလေးရှိတယ် ")
    elif 'ကောင်မလေးရှာ‌ေပး' in user_message:
        update.message.reply_text(" ငှက်ပျောပင်စိုက် ")
    else:
        update.message.reply_text("လူနားလည်အောင်ပြော")

# Function to send a direct message to the server
def send_to_server(update, context):
    server_chat_id = "1315703144"  # Replace SERVER_CHAT_ID with the actual chat ID of the server
    message = "This is a message sent from the bot to the server."
    context.bot.send_message(chat_id=server_chat_id, text=message)

def main():
    # Create the Updater and pass in your bot's token
    updater = Updater("7010824792:AAGX8uLjw1eN_d-TyxDHhXMTGlhtvgUADO4")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Add message handler for normal messages
    dp.add_handler(MessageHandler(Filters.text, respond))  # Filter messages using Filters.text

    # Add command lhandler for sending message to server
    dp.add_handler(CommandHandler("send_to_server", send_to_server))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
    