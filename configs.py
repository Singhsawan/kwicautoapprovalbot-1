from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21748181"))
    API_HASH = getenv("API_HASH", "b1d962414e186e0778911f3183feac33")
    BOT_TOKEN = getenv("BOT_TOKEN", "6160088499:AAFN8uclac9l2GPJwLeTRdupPLcR7TbDQTU")
    FSUB = getenv("FSUB", "New_Moviee_hindi")
    CHID = int(getenv("CHID", "-1001952663939"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Sawansingh24:Sawansingh24@cluster0.uiuhxxj.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
