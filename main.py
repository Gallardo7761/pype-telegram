import os
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# importing command classes
from commands.misc import Misc
from commands.math import Math
from commands.interaction import Interaction
from commands.help import Help

class PypeBot:
    def __init__(self):
        load_dotenv()
        self.app = ApplicationBuilder().token(os.getenv("TOKEN")).build()
        
        # command registering
        Misc(self.app)
        Math(self.app)
        Interaction(self.app)
        Help(self.app)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Tamo' activo B)")

def main() -> None:
    bot = PypeBot()
    bot.app.add_handler(CommandHandler("start", bot.start))
    bot.app.run_polling()
    
if __name__ == '__main__':
    main()