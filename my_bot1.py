from typing import Final
from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = ''       # You have to add yoru token here
BOT_USERNAME: Final = ''     # You have to add your username here


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اهلا بك في بوت تعلم اللغه الانجليزيه")


# Responses
def handle_response(text: str) -> str:
    if 'مرحبا' in text:
        return 'اهلا بك'
    if 'اريد تعلم اللغه الانجليزيه' in text:
        return 'يمكنني تعليمك اللغه الانجليزيه'
    
    
    return 'لا افهم ماذا تريد!!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    response: str = handle_response(text)
    await update.message.reply_text(response)



if __name__ == '__main__':
    print ("starting the bot ..")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("polling ..")
    app.run_polling(poll_interval=3)