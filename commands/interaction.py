from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler
from time import time
from settings import BOT_OWNER, BOT_NAME, BOT_VERSION, BOT_LANG, BOT_TYPE, BOT_OWNER_ID
from random import randint, choice
from util.messages import delete_user_message
from util.anime import Anime

class Interaction:
    def __init__(self, app: Application):
        self.app = app
        self.anime = Anime()
        
        app.add_handler(CommandHandler("waifu", self.waifu))
        app.add_handler(CommandHandler("neko", self.neko))
        app.add_handler(CommandHandler("shinobu", self.shinobu))
        app.add_handler(CommandHandler("megumin", self.megumin))
        app.add_handler(CommandHandler("bully", self.bully))
        app.add_handler(CommandHandler("cuddle", self.cuddle))
        app.add_handler(CommandHandler("cry", self.cry))
        app.add_handler(CommandHandler("hug", self.hug))
        app.add_handler(CommandHandler("awoo", self.awoo))
        app.add_handler(CommandHandler("kiss", self.kiss))
        app.add_handler(CommandHandler("lick", self.lick))
        app.add_handler(CommandHandler("pat", self.pat))
        app.add_handler(CommandHandler("smug", self.smug))
        app.add_handler(CommandHandler("bonk", self.bonk))
        app.add_handler(CommandHandler("yeet", self.yeet))
        app.add_handler(CommandHandler("blush", self.blush))
        app.add_handler(CommandHandler("smile", self.smile))
        app.add_handler(CommandHandler("wave", self.wave))
        app.add_handler(CommandHandler("highfive", self.highfive))
        app.add_handler(CommandHandler("handhold", self.handhold))
        app.add_handler(CommandHandler("nom", self.nom))
        app.add_handler(CommandHandler("bite", self.bite))
        app.add_handler(CommandHandler("glomp", self.glomp))
        app.add_handler(CommandHandler("slap", self.slap))
        app.add_handler(CommandHandler("kill", self.kill))
        app.add_handler(CommandHandler("kick", self.kick))
        app.add_handler(CommandHandler("happy", self.happy))
        app.add_handler(CommandHandler("wink", self.wink))
        app.add_handler(CommandHandler("poke", self.poke))
        app.add_handler(CommandHandler("dance", self.dance))
        app.add_handler(CommandHandler("cringe", self.cringe))
        app.add_handler(CommandHandler("run", self.run))
        app.add_handler(CommandHandler("fbi", self.fbi))
        app.add_handler(CommandHandler("spank", self.spank))
        app.add_handler(CommandHandler("ship", self.ship))
        app.add_handler(CommandHandler("moan", self.moan))
        app.add_handler(CommandHandler("femboize", self.femboize))

    @delete_user_message
    async def waifu(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("waifu")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha pedido una waifu"
        )

    @delete_user_message
    async def neko(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("neko")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha pedido un neko"
        )

    @delete_user_message
    async def shinobu(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("shinobu")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha pedido una shinobu"
        )

    @delete_user_message
    async def megumin(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("megumin")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha pedido una megumin"
        )

    @delete_user_message
    async def bully(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("bully")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} le ha hecho bullying a {user}"
        )

    @delete_user_message
    async def cuddle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("cuddle")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} se ha acurrucado con {user} uwu"
        )

    @delete_user_message
    async def cry(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("cry")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} se ha puesto a llorar :("
        )

    @delete_user_message
    async def hug(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("hug")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha abrazado a {user}"
        )

    @delete_user_message
    async def awoo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("awoo")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} es un puto furro y ha pedido una foto de un furro"
        )

    @delete_user_message
    async def kiss(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("kiss")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha besado a {user} >///<"
        )

    @delete_user_message
    async def lick(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("lick")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha lamido a {user} OwO"
        )

    @delete_user_message
    async def pat(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("pat")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha acariciado a {user} >.<"
        )

    @delete_user_message
    async def smug(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("smug")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} se ha chuleado de {user}"
        )
        
    @delete_user_message
    async def bonk(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("bonk")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} le ha hecho bonk a {user}"
        )

    @delete_user_message
    async def yeet(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("yeet")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha lanzado a {user} a chuparla XD"
        )

    @delete_user_message
    async def blush(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("blush")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} se ha sonrojado >///<"
        )

    @delete_user_message
    async def smile(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("smile")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha sonreido"
        )

    @delete_user_message
    async def wave(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("wave")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha saludado a {user}"
        )

    @delete_user_message
    async def highfive(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("highfive")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} a chocado a {user} ;D"
        )

    @delete_user_message
    async def handhold(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("handhold")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} le ha cogido la manita a {user} u.u"
        )

    @delete_user_message
    async def nom(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("nom")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} se ha puesto a comer algo rico"
        )

    @delete_user_message
    async def bite(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("bite")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha mordido a {user} ùwú"
        )

    @delete_user_message
    async def glomp(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("glomp")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} se ha abalanzado sobre {user}"
        )

    @delete_user_message
    async def slap(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("slap")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} le ha dado una bofetada a {user}"
        )

    @delete_user_message
    async def kill(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("kill")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} ha matado a {user} 💀"
        )

    @delete_user_message
    async def kick(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("kick")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} le ha pegado una patada a {user}"
        )

    @delete_user_message
    async def happy(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("happy")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} está feliz :D"
        )

    @delete_user_message
    async def wink(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("wink")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} le ha guiñado el ojo a {user} ;)"
        )

    @delete_user_message
    async def poke(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        url = self.anime.sfw("poke")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} está molestando a {user} ù.ú"
        )

    @delete_user_message
    async def dance(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        url = self.anime.sfw("dance")
        await update.effective_chat.send_animation(
            animation=url,
            caption=f"{update.effective_sender.first_name} se ha puesto a bailar"
        )

    @delete_user_message
    async def cringe(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        caption=f"{update.effective_sender.first_name} le ha dado cringe lo que ha dicho {user}"
        with open("data/images/interaction/cringe.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=caption,
                disable_notification=True
            )
    
    
    @delete_user_message
    async def run(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        caption = f"{update.effective_sender.first_name} ha huido"
        with open("data/images/interaction/run.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=caption,
                disable_notification=True
            )
    
    @delete_user_message
    async def fbi(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        caption = f"{update.effective_sender.first_name} ha llamado al FBI! Corre {user}!!!!"
        with open("data/images/interaction/fbi.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=caption,
                disable_notification=True
            )
    
    @delete_user_message
    async def spank(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        caption = f"{update.effective_sender.first_name} le ha dado una nalgada a {user}"
        with open("data/images/interaction/spank.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=caption,
                disable_notification=True
            )
    
    @delete_user_message
    async def ship(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar dos usuarios"
            )
            return
        
        user1 = context.args[0]
        user2 = context.args[1]
        caption = f"{user1} x {user2} tienen una compatibilidad del {randint(0,100)}%"
        with open("data/images/interaction/ship.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=caption,
                disable_notification=True
            )
    
    @delete_user_message
    async def moan(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        caption = f"{update.effective_sender.first_name} ha gemido como una perra"
        with open("data/images/interaction/moan.gif", "rb") as gif:
            await update.effective_chat.send_animation(
                animation=gif,
                caption=caption,
                disable_notification=True
            )
        
    @delete_user_message
    async def femboize(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text=f"Debes especificar un usuario"
            )
            return
        
        
        user = context.args[0]
        caption = f"{update.effective_sender.first_name} ha convertido en femboy a {user}"
        with open("data/images/interaction/femboy.png", "rb") as png:
            await update.effective_chat.send_photo(
                photo=png,
                caption=caption,
                disable_notification=True
            )        