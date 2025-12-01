from modules.core.queues import *

def void(arg,q):
    for i in range(10**7):
        i = i + 12
    lock = th.Lock()    
    lock.acquire()
    print(arg)
    q.append(arg)
    lock.release()

q = []
pool = Pool(2)
for i in range(64):
    pool.add(void,[str(i+1),q])

time.sleep(10)

while pool.threads_running():
    print(pool.threads_running())
    time.sleep(1)

print(pool.running)
print(q)