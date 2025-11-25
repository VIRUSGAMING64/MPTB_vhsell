from modules.core.queues import *
from modules.gvar import *
import os
from modules.utils import *
import asyncio
import threading as th
from modules.fuse import *

def start(message:Message):
    global loop
    asyncio.run_coroutine_threadsafe(message.reply_text("Hello! I am your bot. How can I assist you today?"),loop)


def kill(message:Message):
    global ADMINS_ID
    if not message.from_user.id in ADMINS_ID:
        message.reply_text("operation not available")
        return
    message.reply_text("Shutting down... Goodbye!")
    os._exit(0)


def upload(message:Message):
    args = message.text
    file = getfullpath(args)

def getid(message:Message):
    await_exec(message.reply_text,[f"Your ID: {message.from_user.id}"])

def help_bot(message:Message): 
    global loop
    asyncio.run_coroutine_threadsafe(message.reply_text("Hello! I am your bot. [work in progress]"),loop)

def ls(message:Message):
    args = message.text.removeprefix("/ls")
    user = message.from_user

def rm(message:Message):
    args = message.text

def mkdir(message:Message):
    args = message.text

def ren(message:Message):
    args = message.text

def size(message:Message):
    args = message.text

def comp(message:Message):
    args = message.text


commands            = {
    "/start": start,
    "/help": help_bot,
    "/upload": upload,
    "/kill": kill,
    "/ls": ls,
    "/mkdir": mkdir,
    "/rm": rm,
    "/ren": ren,
    "/comp": comp,
    "/size": size,
    "/getid": getid
}

COMMANDS = commands.keys()