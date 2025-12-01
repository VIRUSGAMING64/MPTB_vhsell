from modules.gvar import *
class FileUploader:
    def __init__(self, sender:ExtBot, message:Message):
        self.sender = sender
        self.mes = message