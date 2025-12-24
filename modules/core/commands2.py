import requests
from modules.compress.video import VideoCompressor
from modules.core.queues import *
from modules.gvar import *
import os
from modules.utils import *
import asyncio
import threading as th
from modules.fuse import *


def comp(message:Message, command:str):
    args = command
    args:str = args.removeprefix("/comp ")


def ren(message:Message, command:str):
    args = command


def x265(message:Message, command:str):
    filename = command.removeprefix('/x265 ')
    message = await_exec(message.reply_text,["encoding..."])
    compressor = VideoCompressor(callback=progress,args=[None,message,"encoding..."])
    if not compressor.set_file(filename):
        await_exec(
            message.reply_text,
            ["File not found..."]
        )
        return
    
    if not compressor.compress():
        await_exec(
            message.reply_text,
            ["Error compressing..."]
        )
        return
    
    await_exec(
        message.reply_text
        ["video encoded"]
    )