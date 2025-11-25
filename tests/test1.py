
from modules.database import database
from random import *
base = database()

for x in range(100):
    a = randint(0,1000000)
    b = randint(0,1000000)
    bl =randint(0,1)
    bl2 =randint(0,1)

    s:str = f"{a},{b},{bl},{bl2},{randbytes(16)}"
    print(s)
    base.load_str(s)

base.save()