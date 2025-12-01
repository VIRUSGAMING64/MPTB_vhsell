
import base64
from modules.database import database
from random import *
base = database()

for x in range(10**6):
    print(f"\r{x}\r",end="")
    a = randint(0,1000000)
    b = randint(0,1000000)
    bl =randint(0,1)
    bl2 =randint(0,1)
    state = randint(0,65535)
    by = base64.b64encode(randbytes(16))
    s:str = f"{a},{b},{bl},{bl2},{by},{state}"
    #print(s)
    base.load_str(s)

base.save()