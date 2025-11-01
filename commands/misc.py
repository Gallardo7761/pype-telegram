from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler
from time import time
from settings import BOT_OWNER, BOT_NAME, BOT_VERSION, BOT_LANG, BOT_TYPE, BOT_OWNER_ID
from random import randint, choice
from util.messages import delete_user_message

class Misc:
    def __init__(self, app: Application):
        self.app = app
        app.add_handler(CommandHandler("ping", self.ping))
        app.add_handler(CommandHandler("info", self.info))
        app.add_handler(CommandHandler("say", self.say))
        app.add_handler(CommandHandler("banana", self.banana))
        app.add_handler(CommandHandler("dado", self.dice))
        app.add_handler(CommandHandler("moneda", self.coin))
        app.add_handler(CommandHandler("paredes", self.walls))
        app.add_handler(CommandHandler("oooh", self.oooh))
        app.add_handler(CommandHandler("beber", self.drink))
        app.add_handler(CommandHandler("bombardeen", self.bomb))
        
    @delete_user_message
    async def ping(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        before = update.message.date.timestamp()
        now = time()
        await update.effective_chat.send_message(
            text=f"<b>🏓 Pong!</b> Latency is <i>{round((now - before) * 1000, 2)} ms</i>",
            parse_mode="HTML",
            disable_notification=True
        )
       
    @delete_user_message 
    async def info(self, update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        group = update.effective_chat.title
        chat_id = update.effective_chat.id
        member_count = await context.bot.get_chat_member_count(chat_id)
        command_count = sum(1 for c in context.application.handlers[0] if isinstance(c, CommandHandler))
        info_text = f"""
<b>Grupo: {group}</b>
Miembros: {member_count}
Creador: {BOT_OWNER}
Nº Comandos: {command_count}

<b>Info técnica:</b>
Nombre: {BOT_NAME}
Lenguaje: {BOT_LANG}
Tipo: {BOT_TYPE}
Versión: {BOT_VERSION}
        """
        
        await update.effective_chat.send_message(
            text=info_text,
            parse_mode="HTML",
            disable_notification=True
        )

    @delete_user_message
    async def say(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text="Pero dime lo que tengo que decir puta",
                disable_notification=True
            )
            return
        await update.effective_chat.send_message(
            text=" ".join(arg for arg in context.args),
            disable_notification=True
        )

    @delete_user_message
    async def banana(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if update.effective_sender.id == BOT_OWNER_ID:
            await update.effective_chat.send_message(
                text=f"La banana de {update.effective_user.first_name} mide 21 cm 😳",
                disable_notification=True
            )
        else:
            await update.effective_chat.send_message(
                text=f"La banana de {update.effective_user.first_name} mide {randint(-5, 21)} cm 😳",
                disable_notification=True
            )    
         
    @delete_user_message
    async def dice(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.effective_chat.send_dice(
            emoji='🎲',
            disable_notification=True
        )
        
    @delete_user_message
    async def coin(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        html =f"""
<b>🪙 Se ha lanzado la moneda</b>
Resultado: {choice(("Cara 😀", "Cruz ❌"))}
        """
        await update.effective_chat.send_message(
            text=html,
            parse_mode="HTML",
            disable_notification=True
        )
    
    @delete_user_message
    async def walls(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text="Debes especificar un usuario",
                disable_notification=True
            )
            return
        
        if not context.args[0].startswith("@"):
            await update.effective_chat.send_message(
                text="Debes mencionar a un usuario",
                disable_notification=True
            )
            return

        user = context.args[0]
        caption = f"{user} está por las paredes"
        
        with open("data/images/interaction/paredes.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=caption,
                disable_notification=True
            )
            
    @delete_user_message
    async def oooh(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        with open("data/images/interaction/oooh.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                disable_notification=True
            )
            
    @delete_user_message
    async def drink(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        drinks = ["cerveza", "vino", "whisky", "ron", "vodka", "tequila", "ginebra", "sidra", "champán", "cava", "sake", "absenta", "brandy", "licor", "vermut", "mezcal", "pacharán", "anís", "aguardiente", "coñac", "cóctel", "cubata", "cóctel", "cubalibre"]
        with open("data/images/interaction/beber.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=f"@{update.effective_sender.username} ha bebido {choice(drinks)}",
                disable_notification=True
            )
        
    @delete_user_message
    async def bomb(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text="Debes especificar algo que bombardear",
                disable_notification=True
            )
            return
        
        with open("data/images/interaction/bombardeen.gif") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=f"Bombardeen {context.args[0]}",
                disable_notification=True
            )
    
    