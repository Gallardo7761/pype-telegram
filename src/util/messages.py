from telegram import Update
from telegram.ext import ContextTypes

async def respond(context: ContextTypes.DEFAULT_TYPE, chat_id: int, message: str):
    await context.bot.send_message(
        chat_id=chat_id, 
        text="✅ Mensaje recibido",
        disable_notification=True
    )
    
def delete_user_message(func):
    async def wrapper(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await func(self, update, context)
        try:
            await context.bot.delete_message(update.effective_chat.id, update.message.message_id)
        except:
            pass
    return wrapper