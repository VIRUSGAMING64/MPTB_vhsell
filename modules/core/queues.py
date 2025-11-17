import threading as th 
import time


class Pool():
    """
    is a queue in format [function , args]
    """
    running = 0
    queue = [] 
    def __init__(self,threads = 4):
        self.threads = threads
        th.Thread(target = self.run).start()

    def run(self):
        while True:
            if self.running < self.threads and len(self.queue) > 0:
                th.Lock()
                self.running += 1
                func,args = self.queue.pop(0)
                th.Thread(target = self.execute,args = (func,args)).start()
                th.Unlock()
            else:
                time.sleep(1)
            if self.stop == 1:
                break;
    
    def destroy(self):
        self.stop = 1  

    def add(self,func,args):
        self.queue.append([func,args])
    

    
class MessageQueues():
    pass