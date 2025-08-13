import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27965918")
API_HASH = os.environ.get("API_HASH", "d5ca408334552615fa7e8f48c2dac999")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8305685426:AAFf4mTOULfYy46VyeoxoI2YqADfPgokTD0") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "")

CHANNEL = os.environ.get("CHANNEL", "daarotv") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","BYNF_TamilChat") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","ATL_Univers") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","viizet")
STRING = os.environ.get("STRING", "BAGqud4AspJrjkXrlVjsIyNFfesTMHQE3T_A9arnx1tcHDbFl7-ImWPMdDhEbxnIW6H1ZHp3Ya9Y9gi4--y3x2eoAsykBVl909FF1Ge5BiMlJC6VEukjrHbsIbk4CirYv3kUE4hTCqXRdu8x1TXDfddmJD1VrXHrQ4hVhyl7Q719X8XxwuZ0vq_zccPVVYrQpT3hcvN6AqplVBs5LtkIkHZXfW0vxhF8oFLEo7DZBJPHYVC8PDddsx_1RYHiQUnRTR90qtpPy16pPNYfjC7NrwMRDpTvsVge1VU7_0uLvwAkZ3_w5pLjtj5D4otb406c4rTayh_ncsLuzLWiEK3OOPt4qGme5wAAAAFOw4TnAA")

DB_NAME = os.environ.get("DB_NAME","kevyabdi20")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://kevyabdi20:kevyabdi20@kevyabdi.mymiztp.mongodb.net/?retryWrites=true&w=majority&appName=kevyabdi")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://graph.org/file/ad48ac09b1e6f30d2dae4.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1096693642').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002071039887"))