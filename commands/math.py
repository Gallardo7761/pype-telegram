from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler
from random import randint, choice
from util.messages import delete_user_message
import matplotlib.pyplot as plt
import numpy as np
from util.numbers import is_even, is_prime
from settings import GRAPH_PATH
from matplotlib.patches import Circle

class Math:
    def __init__(self, app: Application):
        self.app = app
        app.add_handler(CommandHandler("calcular", self.calc))
        app.add_handler(CommandHandler("par", self.even))
        app.add_handler(CommandHandler("primo", self.prime))
        app.add_handler(CommandHandler("grafseno", self.grafseno))
        app.add_handler(CommandHandler("grafcoseno", self.grafcoseno))
        app.add_handler(CommandHandler("grafrecta", self.grafrecta))
        app.add_handler(CommandHandler("grafparabola", self.grafparabola))
        app.add_handler(CommandHandler("grafcircunferencia", self.grafcircunferencia))
        app.add_handler(CommandHandler("graflog", self.graflog))
        app.add_handler(CommandHandler("grafexp", self.grafexp))

    @delete_user_message
    async def calc(self, update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text="Debes especificar una expresión matemática",
                disable_notification=True
            )
            return

        expression = " ".join(context.args)
        try:
            result = eval(expression)
            await update.effective_chat.send_message(
                text=f"El resultado de {expression} es {result}",
                disable_notification=True
            )
        except Exception as e:
            await update.effective_chat.send_message(
                text=f"Error al calcular la expresión: {e}",
                disable_notification=True
            )
            
    @delete_user_message
    async def even(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text="Debes especificar un número",
                disable_notification=True
            )
            return

        number = int(context.args[0])
        await update.effective_chat.send_message(
            text=f"{number} es un número par." if is_even(number) else f"{number} es un número impar.",
            disable_notification=True
        )
        
    @delete_user_message
    async def prime(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await update.effective_chat.send_message(
                text="Debes especificar un número",
                disable_notification=True
            )
            return

        number = int(context.args[0])
        await update.effective_chat.send_message(
            text=f"{number} es un número primo." if is_prime(number) else f"{number} es un número compuesto.",
            disable_notification=True
        )
        
    async def send_graph(self, update: Update):
        await update.effective_chat.send_photo(open(GRAPH_PATH, "rb"))
        plt.clf()

    @delete_user_message
    async def grafseno(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) < 2:
            await update.effective_chat.send_message("Debes dar a y k: /grafseno a k")
            return
        a, k = map(int, context.args[:2])
        x = np.linspace(0, 2*np.pi, 400)
        y = a * np.sin(k*x)
        plt.axhline(0, color="black")
        plt.plot(x, y, color="#b2122f")
        plt.savefig(GRAPH_PATH)
        await self.send_graph(update)

    @delete_user_message
    async def grafcoseno(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) < 2:
            await update.effective_chat.send_message("Debes dar a y k: /grafcoseno a k")
            return
        a, k = map(int, context.args[:2])
        x = np.linspace(0, 2*np.pi, 400)
        y = a * np.cos(k*x)
        plt.axhline(0, color="black")
        plt.plot(x, y, color="#b2122f")
        plt.savefig(GRAPH_PATH)
        await self.send_graph(update)

    @delete_user_message
    async def grafrecta(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) < 2:
            await update.effective_chat.send_message("Debes dar m y n: /grafrecta m n")
            return
        m, n = map(int, context.args[:2])
        x = np.linspace(-10, 10, 400)
        y = m*x + n
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.plot(x, y, color="#b2122f")
        plt.savefig(GRAPH_PATH)
        await self.send_graph(update)

    @delete_user_message
    async def grafparabola(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) < 3:
            await update.effective_chat.send_message("Debes dar a, b, c: /grafparabola a b c")
            return
        a, b, c = map(int, context.args[:3])
        x = np.linspace(-10, 10, 400)
        y = a*x**2 + b*x + c
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.plot(x, y, color="#b2122f")
        plt.savefig(GRAPH_PATH)
        await self.send_graph(update)

    @delete_user_message
    async def grafcircunferencia(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.effective_chat.send_message("Debes dar el radio: /grafcircunferencia r")
            return
        r = int(context.args[0])
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.add_artist(Circle((0, 0), r, color='r'))
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.savefig(GRAPH_PATH)
        await self.send_graph(update)

    @delete_user_message
    async def graflog(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) < 2:
            await update.effective_chat.send_message("Debes dar a y b: /graflog a b")
            return
        a, b = map(int, context.args[:2])
        x = np.linspace(0.01, 10, 400)
        y = a*np.log(x) + b
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.plot(x, y, color="#b2122f")
        plt.savefig(GRAPH_PATH)
        await self.send_graph(update)

    @delete_user_message
    async def grafexp(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) < 2:
            await update.effective_chat.send_message("Debes dar a y b: /grafexp a b")
            return
        a, b = map(int, context.args[:2])
        x = np.linspace(-10, 10, 400)
        y = a*np.exp(b*x)
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.plot(x, y, color="#b2122f")
        plt.savefig(GRAPH_PATH)
        await self.send_graph(update)