from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, Application, CommandHandler, CallbackQueryHandler
from settings import VARIOS, INTERACCION, MATEMATICAS
from util.messages import delete_user_message

PAGES = [VARIOS, INTERACCION, MATEMATICAS]
ITEMS_PER_PAGE = 1

class Help:
    def __init__(self, app: Application):
        self.app = app
        app.add_handler(CommandHandler("help", self.help))
        app.add_handler(CallbackQueryHandler(self.callback, pattern="^help_"))
        
    @delete_user_message
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self.send_help(update, page=0)
        
    async def send_help(self, update: Update, page: int):
        start_idx = page * ITEMS_PER_PAGE
        end_idx = start_idx + ITEMS_PER_PAGE
        text = "\n".join(PAGES[start_idx:end_idx])

        keyboard = []
        if page > 0:
            keyboard.append(InlineKeyboardButton("⬅️ Anterior", callback_data=f"help_{page-1}"))
        if end_idx < len(PAGES):
            keyboard.append(InlineKeyboardButton("➡️ Siguiente", callback_data=f"help_{page+1}"))

        reply_markup = InlineKeyboardMarkup([keyboard]) if keyboard else None

        if update.message:
            await update.message.reply_text(f"**Ayuda {page+1}/{(len(PAGES)-1)//ITEMS_PER_PAGE + 1}**\n\n{text}", parse_mode="Markdown", reply_markup=reply_markup)
        elif update.callback_query:
            await update.callback_query.edit_message_text(f"**Ayuda {page+1}/{(len(PAGES)-1)//ITEMS_PER_PAGE + 1}**\n\n{text}", parse_mode="Markdown", reply_markup=reply_markup)
            await update.callback_query.answer()

    async def callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        page = int(query.data.split("_")[1])
        await self.send_help(update, page=page)