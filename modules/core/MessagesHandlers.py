from telegram import *
from telegram.ext import *


async def on_message(update:Update,context):
    message = update.message
    if message != None:
        """filtrar por tipo de mensage"""
        await message.reply_text("Hello from on_message handler!")
    

def direct_message():
    pass

def group_message():
    pass

def channel_message():
    pass