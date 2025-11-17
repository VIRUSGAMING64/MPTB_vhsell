
import os
from core import *

TOKEN        = os.getenv("TOKEN")
API_HASH     = os.getenv("API_HASH")
API_ID       = int(os.getenv("API_ID"))



from modules.database import *
from modules.utils import *