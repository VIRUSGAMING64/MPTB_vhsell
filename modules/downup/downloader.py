from modules.entity import *
from modules.gvar import *
from modules.core import *
from modules.database import *
import requests as rq
from multiprocessing import Process
from telegram.ext import *

class url_downloader:
    def __init__(self,sender , user:peer, threads = 32):
        self.sender = sender
        self.user = user
        self.threads = threads

    def update_message(self):
        pass

    def getdata(self,url,l,r):
        pass
    
    def _download(self,url, l, r):
        BS = 16 * 1024
        while l <= r:
            if l + BS < r and l % BS == 0:
                self.getdata(url, l , l + BS)
                l += BS
            else:
                self.getdata(url, l , l)
                l += 1

    def getlenght(self,url):
        pass

    def download(self, url:str): 
        len = self.getlenght(url)    
        if len == None:
            pass
            return

        #! TODO dividir len entre cantidad de threads


class tg_downloader:
    def __init__(self,message:Message,sender:ExtBot):
        self.user = base.get(message.from_user.id)
        self.mess = message
    
    def updater(self):
        pass      