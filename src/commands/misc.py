from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler
from time import time
from settings import BOT_OWNER, BOT_NAME, BOT_VERSION, BOT_LANG, BOT_TYPE, BOT_OWNER_ID
from random import randint
from util.messages import delete_user_message

class Misc:
    def __init__(self, app: Application):
        self.app = app
        app.add_handler(CommandHandler("ping", self.ping))
        app.add_handler(CommandHandler("info", self.info))
        app.add_handler(CommandHandler("say", self.say))
        app.add_handler(CommandHandler("banana", self.banana))
        app.add_handler(CommandHandler("dado", self.dice))
    
    @delete_user_message
    async def ping(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        before = update.message.date.timestamp()
        now = time()
        await update.effective_chat.send_message(text=f"<b>🏓 Pong!</b> Latency is <i>{round((now - before) * 1000, 2)}</i>", parse_mode="HTML", disable_notification=True)
       
    @delete_user_message 
    async def info(self, update:Update, context: ContextTypes.DEFAULT_TYPE):
        group = update.effective_chat.title
        chat_id = update.effective_chat.id
        member_count = await context.bot.get_chat_member_count(chat_id)
        command_count = sum(1 for c in context.application.handlers[0] if isinstance(c, CommandHandler))
        info_text = f"""
<b>Grupo:</b>
Miembros: {member_count}
Creador: {BOT_OWNER}
Nº Comandos: {command_count}

<b>Info técnica:</b>
Nombre: {BOT_NAME}
Lenguaje: {BOT_LANG}
Tipo: {BOT_TYPE}
Versión: {BOT_VERSION}
        """
        
        await update.effective_chat.send_message(text=info_text, parse_mode="HTML", disable_notification=True)
        
    @delete_user_message
    async def say(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.args:
            await update.effective_chat.send_message(" ".join(arg for arg in context.args))
        else:
            await update.effective_chat.send_message("Pero dime lo que tengo que decir puta")
          
    @delete_user_message
    async def banana(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_sender.id == BOT_OWNER_ID:
            await update.effective_chat.send_message(f"La banana de {update.effective_user.first_name} mide 21 cm 😳")
        else:
            await update.effective_chat.send_message(f"La banana de {update.effective_user.first_name} mide {randint(-5, 21)} cm 😳")    
         
    @delete_user_message
    async def dice(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.effective_chat.send_dice(emoji='🎲', disable_notification=True)