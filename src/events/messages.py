from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

class MessageEvents:
    def __init__(self, app: Application):
        self.app = app